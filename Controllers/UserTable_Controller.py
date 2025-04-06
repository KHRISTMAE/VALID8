from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from CRUD import UserTable_CRUD as crud_user_table
from schemas import UserTable as UserTableSchema
from Database.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=UserTableSchema)
def create_user(user: UserTableSchema, db: Session = Depends(get_db)):
    db_user = crud_user_table.create_user(db, user.roleID, user.role)
    return db_user

@router.get("/users/", response_model=list[UserTableSchema])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_user_table.get_users(db, skip=skip, limit=limit)

@router.get("/users/{userID}", response_model=UserTableSchema)
def read_user(userID: int, db: Session = Depends(get_db)):
    db_user = crud_user_table.get_user_by_id(db, userID)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/users/{userID}", response_model=UserTableSchema)
def update_user(userID: int, user: UserTableSchema, db: Session = Depends(get_db)):
    db_user = crud_user_table.update_user(db, userID, user.roleID, user.role)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/users/{userID}", response_model=UserTableSchema)
def delete_user(userID: int, db: Session = Depends(get_db)):
    db_user = crud_user_table.delete_user(db, userID)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
