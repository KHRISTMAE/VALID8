from sqlalchemy import Column, Integer, String
from Database.database import Base, SessionLocal
from sqlalchemy.orm import relationship
from Model import OfficerEvent  # Correct import
import bcrypt

class SSGOfficer(Base):
    __tablename__ = 'ssg_officer'

    officerID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    position = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(128), nullable=False)  # bcrypt hashes are 60+ chars

    # Relationship with OfficerEvent
    officer_event = relationship("OfficerEvent", back_populates="officer")

    def __init__(self, name, position, email, password):
        self.name = name
        self.position = position
        self.email = email
        self.password = self.hash_password(password)

    def hash_password(self, plain_password):
        hashed = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())
        return hashed.decode('utf-8')

    def set_password(self, new_password):
        self.password = self.hash_password(new_password)

    def check_password(self, password_to_check):
        return bcrypt.checkpw(password_to_check.encode('utf-8'), self.password.encode('utf-8'))

    @property
    def formatted_id(self):
        return f"O{self.officerID}" if self.officerID is not None else "Pending ID"

    
def fetch_officer():
        """Fetches the first officer and prints their formatted ID."""
        with SessionLocal() as session:
            officer = session.query(SSGOfficer).first()
            if officer:
                print(officer.formatted_id)  # Expected: 'O1', 'O2', etc.
            else:
                print("No officer records found.")

# Run function safely
if __name__ == "__main__":
    fetch_officer()

