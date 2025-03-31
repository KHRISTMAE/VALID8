from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import BYTEA
from Database.database import Base
from passlib.context import CryptContext

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Student(Base):
    __tablename__ = 'student'

    studentID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    studentName = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String, nullable=False)  # Hashed password
    programID = Column(Integer, ForeignKey("program.programID"), nullable=False)
    yearLevel = Column(Integer, nullable=False)
    userID = Column(Integer, ForeignKey("user_table.userID"), nullable=True)  # Auto-generated from UserTable
    photo = Column(BYTEA)  # For storing face photos

    # Relationships
    program = relationship("Program", back_populates="students")
    user = relationship("UserTable", back_populates="students")
    attendances = relationship("Attendance", back_populates="student", cascade="all, delete-orphan")

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
        return pwd_context.hash(password)

    def verify_password(self, plain_password):
        return pwd_context.verify(plain_password, self.password)

    def generate_user_id(self):
        # Logic to auto-generate userID (fetch the max existing userID + 1)
        from sqlalchemy.orm import Session
        from Database.database import get_db

        db: Session = next(get_db())
        last_user = db.query(Student).order_by(Student.userID.desc()).first()
        new_user_id = (last_user.userID + 1) if last_user else 1  # If no users, start from 1
        return new_user_id
