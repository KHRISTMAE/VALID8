from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from CRUD import create_role, get_roles, get_role, update_role, delete_role
from schemas import RoleCreate, RoleUpdate, RoleResponse
from Database.database import SessionLocal

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new Role
@router.post("/", response_model=RoleResponse)
def create_role_route(role: RoleCreate, db: Session = Depends(get_db)):
    return create_role(db=db, role=role)

# Get all Roles
@router.get("/", response_model=list[RoleResponse])
def get_roles_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_roles(db=db, skip=skip, limit=limit)

# Get a Role by roleID
@router.get("/{roleID}", response_model=RoleResponse)
def get_role_route(roleID: int, db: Session = Depends(get_db)):
    db_role = get_role(db=db, roleID=roleID)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

# Update a Role by roleID
@router.put("/{roleID}", response_model=RoleResponse)
def update_role_route(roleID: int, role: RoleUpdate, db: Session = Depends(get_db)):
    db_role = update_role(db=db, roleID=roleID, role=role)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

# Delete a Role by roleID
@router.delete("/{roleID}", response_model=RoleResponse)
def delete_role_route(roleID: int, db: Session = Depends(get_db)):
    db_role = delete_role(db=db, roleID=roleID)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role
