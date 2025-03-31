from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship
from Database.database import Base

class Program(Base):
    __tablename__ = 'program'

    programID = Column(Integer, primary_key=True, autoincrement=True)
    programName = Column(String(100), nullable=False, unique=True)  # Unique program name
    college = Column(String(100), nullable=False)

    __table_args__ = (
        UniqueConstraint('programName', name='uq_programName'),  # Explicit unique constraint
    )

    # Relationship to Student
    students = relationship("Student", back_populates="program", cascade="all, delete-orphan")

    def __init__(self, programName, college):
        self.programName = programName
        self.college = college
