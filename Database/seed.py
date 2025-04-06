from sqlalchemy.orm import Session
from Database.database import get_db  # Adjust this import if necessary
from Model import UserTable, Role  # Adjust this import according to your project structure
import bcrypt  # For hashing passwords

def hash_password(password: str) -> str:
    """Hashes a password using bcrypt."""
    salt = bcrypt.gensalt()  # Generate salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)  # Hash the password
    return hashed_password.decode('utf-8')  # Return the hashed password as a string

def create_admin_user(db: Session):
    """Creates the ADMIN role and admin user if not existing."""
    # Check if "admin" role exists
    admin_role = db.query(Role).filter(Role.role_name == "ADMIN").first()
    if not admin_role:
        admin_role = Role(role_name="ADMIN")
        db.add(admin_role)
        db.commit()
        db.refresh(admin_role)
        print("✅ ADMIN role created.")
    else:
        print("ℹ️ ADMIN role already exists.")

    # Check if admin user exists
    admin_user = db.query(UserTable).filter(UserTable.username == "admin").first()
    if admin_user:
        print(f"ℹ️ Admin user already exists: {admin_user.username}")
    else:
        print("Admin user does not exist, creating...")
        hashed_password = hash_password("admin123")  # Hash the password
        admin_user = UserTable(
            email="admin@example.com", 
            username="admin", 
            password=hashed_password,
            roleID=admin_role.roleID
        )
        db.add(admin_user)
        db.commit()
        db.refresh(admin_user)
        print("✅ Admin user created successfully.")

def seed():
    """Standalone seed function that handles creating the admin user and role."""
    from Database.database import get_db  # Lazy import to avoid circular import
    db = next(get_db())  # Open a new session
    create_admin_user(db)  # Create the admin user and role
    db.close()  # Close the session

def main():
    """Main function to call the seed process."""
    print("Starting seed script...")
    seed()  # Run the seeding process
    print("Seed script completed.")

# I-modify ang seed.py aron pwede nimo i-run directly

# Sa bottom sa file, idugang kini:
if __name__ == "__main__":
    from Database.database import get_db
    db = next(get_db())
    create_admin_user(db)
    print("Admin creation script completed.")
