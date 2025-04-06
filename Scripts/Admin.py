from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import Model
from Model import User
from Database.database import Base  # Make sure to import your database connection

DATABASE_URL = "postgresql://postgres:ladyzoy@localhost/ABCC"  # i-edit sa imo actual DB

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables
Base.metadata.create_all(bind=engine)

def create_default_admin():
    db = SessionLocal()

    # Check if the admin user exists by email
    admin = db.query(User).filter(User.email == "admin@example.com").first()
    if not admin:
        # If admin doesn't exist, create a new admin user
        admin = User(
            email="admin@example.com",
            hashed_password="hashed_password_here",  # Make sure to hash the password securely
            full_name="Admin User",
        )
        db.add(admin)
        db.commit()
        db.refresh(admin)
        print("Default admin account created successfully.")
    else:
        print("Admin account already exists.")
    
    db.close()

if __name__ == "__main__":
    create_default_admin()
