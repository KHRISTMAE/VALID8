from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Database.database import get_db
from Model.UserTable import UserTable
from schemas.UserTable_schema import UserCreate, UserResponse
from Repository.UserTableRepository import UserTableRepository

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", response_model=UserResponse)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    repo = UserTableRepository(db)

    existing_user = repo.get_by_email(user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = UserTable(
        username=user_data.username,
        email=user_data.email,
        password=user_data.password  # Note: Hash ni sa real app
    )
    created_user = repo.create(new_user)
    return created_user

@router.get("/", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    repo = UserTableRepository(db)
    return repo.get_all()

@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    repo = UserTableRepository(db)
    user = repo.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    repo = UserTableRepository(db)
    user = repo.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    repo.delete(user)
    return {"message": "User deleted successfully"}
