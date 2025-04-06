from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from Database.database import Base, SessionLocal

class UserRoles(Base):
    __tablename__ = 'user_roles'
    
    userRoleID = Column(Integer, primary_key=True, autoincrement=True)
    userID = Column(Integer, ForeignKey('user_table.userID'), primary_key=True)
    roleID = Column(Integer, ForeignKey('role.roleID'), primary_key=True)
    
    # Relationship to UserTable and Role
    user = relationship('UserTable', back_populates='user_roles')  # Connects to UserTable
    role = relationship('Role', back_populates='user_roles')  # Connects to Role

    @property
    def formatted_id(self):
        return f"UR{self.userRoleID}"

@classmethod
def fetch_userRoles(cls):
    """Fetches the first officer and prints their formatted ID."""
    with SessionLocal() as session:
        userRoles = session.query(UserRoles).first()
        if userRoles:
            print(userRoles.formatted_id)  # Expected: 'UR1', 'U2', etc.
        else:
            print("No officer records found.")

# Run function safely in the main script
if __name__ == "__main__":
    UserRoles.fetch_userRoles()
