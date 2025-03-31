from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Database.database import Base

class Role(Base):
    __tablename__ = 'role'
    
    roleID = Column(Integer, primary_key=True)
    role_name = Column(String)

    users = relationship('UserTable', back_populates='role')  # Ensure correct reference to UserTable
    user_roles = relationship("UserRoles", back_populates="role")
