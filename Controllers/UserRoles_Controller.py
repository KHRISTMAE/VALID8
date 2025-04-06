# controllers/user_roles_controller.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Database.database import SessionLocal
from schemas import UserRoleCreate, UserRoleUpdate, UserRoleInDB
from CRUD  import UserRoles_CRUD as crud

router = APIRouter(
    prefix="/user_roles",
    tags=["User Roles"]
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserRoleInDB)
def create_user_role(user_role: UserRoleCreate, db: Session = Depends(get_db)):
    return crud.create_user_role(db, user_role)

@router.get("/{userRoleID}", response_model=UserRoleInDB)
def read_user_role(userRoleID: int, db: Session = Depends(get_db)):
    user_role = crud.get_user_role(db, userRoleID)
    if user_role is None:
        raise HTTPException(status_code=404, detail="UserRole not found")
    return user_role

@router.get("/", response_model=list[UserRoleInDB])
def read_all_user_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_all_user_roles(db, skip, limit)

@router.put("/{userRoleID}", response_model=UserRoleInDB)
def update_user_role(userRoleID: int, user_role_update: UserRoleUpdate, db: Session = Depends(get_db)):
    user_role = crud.update_user_role(db, userRoleID, user_role_update)
    if user_role is None:
        raise HTTPException(status_code=404, detail="UserRole not found")
    return user_role

@router.delete("/{userRoleID}", response_model=UserRoleInDB)
def delete_user_role(user_role_id: int, db: Session = Depends(get_db)):
    user_role = crud.delete_user_role(db, user_role_id)
    if user_role is None:
        raise HTTPException(status_code=404, detail="UserRole not found")
    return user_role
