from sqlalchemy.orm import Session
from Model import Role
from schemas import RoleCreate, RoleUpdate

# Create a new Role
def create_role(db: Session, role: RoleCreate):
    db_role = Role(role_name=role.role_name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

# Get all Roles
def get_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Role).offset(skip).limit(limit).all()

# Get a Role by roleID
def get_role(db: Session, role_id: int):
    return db.query(Role).filter(Role.roleID == role_id).first()

# Update a Role by roleID
def update_role(db: Session, role_id: int, role: RoleUpdate):
    db_role = db.query(Role).filter(Role.roleID == role_id).first()
    if db_role:
        for key, value in role.dict(exclude_unset=True).items():
            setattr(db_role, key, value)
        db.commit()
        db.refresh(db_role)
        return db_role
    return None

# Delete a Role by roleID
def delete_role(db: Session, role_id: int):
    db_role = db.query(Role).filter(Role.roleID == role_id).first()
    if db_role:
        db.delete(db_role)
        db.commit()
        return db_role
    return None
