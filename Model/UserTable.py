from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from Database.database import Base

class UserTable(Base):
    __tablename__ = 'user_table'
    
    userID = Column(Integer, primary_key=True, index=True)
    roleID = Column(Integer, ForeignKey('role.roleID'))  # Correct FK reference
    
    role = relationship('Role', back_populates='users')  # Ensure this matches Role.users
    students = relationship("Student", back_populates="user")
    user_roles = relationship("UserRoles", back_populates="user")  # Keep this for Many-to-Many
