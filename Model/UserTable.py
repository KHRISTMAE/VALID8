from sqlalchemy import Column, Enum, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from Database.database import Base, SessionLocal
from passlib.context import CryptContext
from Model.Role import Role  # Import Role bago ito gamitin sa relationship


class UserTable(Base):
    __tablename__ = 'user_table'
    
    userID = Column(Integer, primary_key=True, index=True)
    roleID = Column(Integer, ForeignKey('role.roleID'))  # Foreign Key reference to Role table
    role = Column(Enum("student", "officer", "organizer", name="user_roles"), nullable=False)  # Role-based access
    

    # Define a one-to-many relationship between UserTable and Role
    role = relationship('Role', back_populates='user', lazy='joined')
    
    # One-to-many relationship with students (one user can have many students)
    student = relationship('Student', back_populates='user_table')
    
    # Many-to-many relationship with roles, using a junction table (UserRoles)
    user_roles = relationship('UserRoles', back_populates='user')  # UserRoles is the junction table

    @property
    def formatted_id(self):
        return f"UT{self.userID}"
# Usage
if __name__ == "__main__":
    with SessionLocal() as session:
        user_table = session.query(UserTable).first()
        if user_table:
            print(user_table.formatted_id)  # Outputs 'UT1', 'UT2', etc.
        else:
            print("No user records found.")
