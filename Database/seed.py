# database/seed.py
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from Model import UserTable
from Model.Role import Role

# Initialize password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def create_admin_user(db: Session):
    """Creates the ADMIN role and admin user if not existing."""
    # Check if "admin" role exists
    admin_role = db.query(Role).filter(Role.role_name == "ADMIN").first()
    if not admin_role:
        admin_role = Role(role_name="ADMIN")
        db.add(admin_role)
        db.commit()
        db.refresh(admin_role)

    # Check if admin user exists
    admin_user = db.query(UserTable).filter(UserTable.username == "admin").first()
    if not admin_user:
        hashed_password = hash_password("admin123")
        admin_user = UserTable(
            email="admin@example.com", 
            username="admin", 
            password=hashed_password,
            role_id=admin_role.id
        )
        db.add(admin_user)
        db.commit()
        db.refresh(admin_user)
        print("✅ Admin user created successfully.")
    else:
        print("ℹ️ Admin user already exists.")

# Optional standalone seed function for quick usage
def seed():
    from Database.database import get_db  # Lazy import to avoid circular import
    db = next(get_db())
    create_admin_user(db)
    db.close()


