from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Database.database import get_db
from Model.Role import Role
from schemas.Role_Schema import RoleCreate, RoleResponse
from Repository import RoleRepository

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.post("/", response_model=RoleResponse)
def create_role(role_create: RoleCreate, db: Session = Depends(get_db)):
    repo = RoleRepository(db)
    new_role = Role(role_name=role_create.role_name)
    created_role = repo.create(new_role)
    return created_role

@router.get("/", response_model=list[RoleResponse])
def get_all_roles(db: Session = Depends(get_db)):
    repo = RoleRepository.RoleRepository(db)
    return repo.get_all()

@router.get("/{role_id}", response_model=RoleResponse)
def get_role(role_id: int, db: Session = Depends(get_db)):
    repo = RoleRepository.RoleRepository(db)
    role = repo.get_by_id(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

@router.delete("/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    repo = RoleRepository.RoleRepository(db)
    role = repo.get_by_id(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    repo.delete(role)
    return {"message": "Role deleted successfully"}
