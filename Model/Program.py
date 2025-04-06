from sqlalchemy import Column, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import relationship
from Database.database import Base,SessionLocal

class Program(Base):
    __tablename__ = 'program'

    programID = Column(Text, primary_key=True)
    programName = Column(String(100), nullable=False, unique=True)  # Unique program name
    college = Column(String(100), nullable=False)

    # Relationship to Student
    student = relationship("Student", back_populates="program")

    def __init__(self, programName, college):
        self.programName = programName
        self.college = college

    @property
    def formatted_id(self):
        """Returns a formatted ID combining programID."""
        return f"P{self.programID}" if self.programID is not None else "Pending ID"

    from Database.database import SessionLocal

def fetch_program():
    """Fetches the first program and prints its formatted ID."""
    with SessionLocal() as session:
        program = session.query(Program).first()
        if program:
            print(program.formatted_id)  # Expected: 'P1', 'P2', etc.
        else:
            print("No program records found.")
