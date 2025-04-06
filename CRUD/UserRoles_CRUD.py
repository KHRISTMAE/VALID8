# crud/user_roles.py
from sqlalchemy.orm import Session
from Model.UserRoles import UserRoles
from schemas import UserRoleCreate, UserRoleUpdate

def create_user_role(db: Session, user_role: UserRoleCreate):
    db_user_role = UserRoles(**user_role.dict())
    db.add(db_user_role)
    db.commit()
    db.refresh(db_user_role)
    return db_user_role

def get_user_role(db: Session, user_role_id: int):
    return db.query(UserRoles).filter(UserRoles.userRoleID == user_role_id).first()

def get_all_user_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(UserRoles).offset(skip).limit(limit).all()

def update_user_role(db: Session, user_role_id: int, user_role_update: UserRoleUpdate):
    db_user_role = db.query(UserRoles).filter(UserRoles.userRoleID == user_role_id).first()
    if db_user_role:
        db_user_role.userID = user_role_update.userID
        db_user_role.roleID = user_role_update.roleID
        db.commit()
        db.refresh(db_user_role)
    return db_user_role

def delete_user_role(db: Session, user_role_id: int):
    db_user_role = db.query(UserRoles).filter(UserRoles.userRoleID == user_role_id).first()
    if db_user_role:
        db.delete(db_user_role)
        db.commit()
    return db_user_role
