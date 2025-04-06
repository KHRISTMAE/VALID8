from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import BYTEA
from passlib.context import CryptContext
from Database.database import Base, SessionLocal
from Model.Program import Program  # Correct import for the Program model
from Model.UserTable import UserTable  # Correct import for the UserTable model

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Student(Base):
    __tablename__ = 'student'

    studentID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    studentName = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)  # Hashed password
    programID = Column(Text, ForeignKey("program.programID"), nullable=False)
    yearLevel = Column(Integer, nullable=False)
    userID = Column(Integer, ForeignKey('user_table.userID'), nullable=True)  # Auto-generated from UserTable
    photo = Column(BYTEA)  # For storing face photos

    # Relationships
    program = relationship("Program", back_populates="student")
    user_table = relationship('UserTable', back_populates='student')
    attendance = relationship('Attendance', back_populates='student')

    def __init__(self, studentName, email, password, programID, yearLevel, userID=None):
        self.studentName = studentName
        self.email = email
        self.password = self.hash_password(password)  # Hash password before storing
        self.programID = programID
        self.yearLevel = yearLevel
        if userID is None:
            self.userID = self.generate_user_id()  # Auto-generate userID if not passed
        else:
            self.userID = userID

    def hash_password(self, password):
        """Hashes a plain password using bcrypt."""
        return pwd_context.hash(password)

    def verify_password(self, plain_password):
        """Verifies if the plain password matches the stored hash."""
        return pwd_context.verify(plain_password, self.password)

    def generate_user_id(self, db):
        """Auto-generate a new userID based on the latest user."""
        try:
            last_user = db.query(UserTable).order_by(UserTable.userID.desc()).first()  # Fetch from UserTable, not Student
            new_user_id = (last_user.userID + 1) if last_user else 1  # If no users, start from 1
            return new_user_id
        except Exception as e:
            db.rollback()  # Rollback in case of error
            raise ValueError(f"Error generating user ID: {e}")

    @property
    def formatted_id(self):
        """Returns the formatted student ID."""
        return f"S{self.studentID}" if self.studentID is not None else "Pending ID"

# Usage Example with Dependency Injection
def create_student(db, studentName, email, password, programID, yearLevel, userID=None):
    """Function to create a student with dependency injection for the session."""
    student = Student(studentName, email, password, programID, yearLevel, userID)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

# Example for fetching and handling sessions
if __name__ == "__main__":
    with SessionLocal() as session:
        student = session.query(Student).first()
        if student:
            print(student.formatted_id)  # Outputs 'S1', 'S2', etc.
        else:
            print("No student records found.")
