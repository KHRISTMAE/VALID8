from sqlalchemy.orm import Session
from Model.UserTable import UserTable
from Model.Role import Role

def create_user(db: Session, roleID: int, role: str):
    """Create a new user."""
    db_user = UserTable(roleID=roleID, role=role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 10):
    """Get a list of users."""
    return db.query(UserTable).offset(skip).limit(limit).all()

def get_user_by_id(db: Session, userID: int):
    """Get a user by ID."""
    return db.query(UserTable).filter(UserTable.userID == userID).first()

def update_user(db: Session, userID: int, roleID: int, role: str):
    """Update a user's role."""
    user = db.query(UserTable).filter(UserTable.userID == userID).first()
    if user:
        user.roleID = roleID
        user.role = role
        db.commit()
        db.refresh(user)
        return user
    return None

def delete_user(db: Session, userID: int):
    """Delete a user."""
    user = db.query(UserTable).filter(UserTable.userID == userID).first()
    if user:
        db.delete(user)
        db.commit()
        return user
    return None
