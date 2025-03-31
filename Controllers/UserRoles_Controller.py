from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from Database.database import get_db
from Model.UserRoles import UserRoles
from Repository.UserRolesRepository import UserRolesRepository
from schemas import UserRolesCreate, UserRolesResponse, UserRolesUpdate  # i-define nato ni sa schemas.py

router = APIRouter(
    prefix="/user_roles",
    tags=["UserRoles"]
)

# Create UserRole
@router.post("/", response_model=UserRolesResponse)
def create_user_role(user_role_data: UserRolesCreate, db: Session = Depends(get_db)):
    repo = UserRolesRepository(db)
    user_role = UserRoles(**user_role_data.dict())
    created_user_role = repo.create(user_role)
    return created_user_role

# Get All UserRoles
@router.get("/", response_model=List[UserRolesResponse])
def get_all_user_roles(db: Session = Depends(get_db)):
    repo = UserRolesRepository(db)
    return repo.get_all()

# Get UserRoles by User ID
@router.get("/user/{user_id}", response_model=List[UserRolesResponse])
def get_user_roles_by_user_id(user_id: int, db: Session = Depends(get_db)):
    repo = UserRolesRepository(db)
    return repo.get_by_user_id(user_id)

# Get UserRoles by Role ID
@router.get("/role/{role_id}", response_model=List[UserRolesResponse])
def get_user_roles_by_role_id(role_id: int, db: Session = Depends(get_db)):
    repo = UserRolesRepository(db)
    return repo.get_by_role_id(role_id)

# Update UserRole
@router.put("/{user_role_id}", response_model=UserRolesResponse)
def update_user_role(user_role_id: int, update_data: UserRolesUpdate, db: Session = Depends(get_db)):
    repo = UserRolesRepository(db)
    existing_user_role = db.query(UserRoles).filter(UserRoles.id == user_role_id).first()
    if not existing_user_role:
        raise HTTPException(status_code=404, detail="UserRole not found")
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(existing_user_role, key, value)
    db.commit()
    db.refresh(existing_user_role)
    return existing_user_role

# Delete UserRole
@router.delete("/{user_role_id}")
def delete_user_role(user_role_id: int, db: Session = Depends(get_db)):
    repo = UserRolesRepository(db)
    user_role = db.query(UserRoles).filter(UserRoles.id == user_role_id).first()
    if not user_role:
        raise HTTPException(status_code=404, detail="UserRole not found")
    db.delete(user_role)
    db.commit()
    return {"message": "UserRole deleted successfully"}
