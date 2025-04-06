from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Database.database import Base, SessionLocal
from .UserRoles import UserRoles
 
class Role(Base):
    __tablename__ = 'role'
    
    roleID = Column(Integer, primary_key=True, index=True)
    role_name = Column(String, nullable = False)

    # One-to-many relationship with UserTable
    # This will allow you to access users from the role directly
    user = relationship('UserTable', back_populates='role')  # Reference to UserTable

    # Many-to-many relationship with UserTable via UserRoles
    # This allows you to access the user-role mapping directly
    user_roles = relationship('UserRoles', back_populates="role")  # Reference to UserRoles

    def __init__(self, role_name):
        self.role_name = role_name

    @property
    def formatted_id(self):
        """Returns a formatted ID combining roleID."""
        return f"R{self.roleID}" if self.roleID is not None else "Pending ID"
    
def fetch_role():
    """Fetches the first role and prints its formatted ID."""
    with SessionLocal() as session:
        role = session.query(Role).first()
        if role:
            print(role.formatted_id)  # Expected: 'R1', 'R2', etc.
        else:
            print("No role records found.")

# Run function safely
if __name__ == "__main__":
    fetch_role()

