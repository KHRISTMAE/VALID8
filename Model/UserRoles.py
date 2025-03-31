from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from Database.database import Base  # or wherever Base is defined

class UserRoles(Base):
    __tablename__ = 'user_roles'

    userID = Column(Integer, ForeignKey('user_table.userID'), primary_key=True)
    roleID = Column(Integer, ForeignKey('role.roleID'), primary_key=True)

    user = relationship("UserTable", back_populates="user_roles")
    role = relationship("Role", back_populates="user_roles")
