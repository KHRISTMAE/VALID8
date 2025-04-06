from typing import Optional
from sqlalchemy.orm import Session
from Model import Student as StudentModel
from schemas import StudentCreate, StudentUpdate, StudentBase

# Create a new student
def create_student(db: Session, student_name: str, email: str, password: str, program_id: int, year_level: int):
    db_student = StudentModel(
        studentName=student_name,
        email=email,
        password=password,  # Make sure you hash the password here
        programID=program_id,
        yearLevel=year_level,
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return StudentBase.from_orm(db_student)  # Return Pydantic model

# Get student by ID
def get_student_by_id(db: Session, student_id: int):
    return db.query(StudentModel).filter(StudentModel.studentID == student_id).first()

# Get all students
def get_students(db: Session, skip: int = 0, limit: int = 10):
    return db.query(StudentModel).offset(skip).limit(limit).all()

# Update a student
def update_student(db: Session, student_id: int, student_name: Optional[str], email: Optional[str], program_id: Optional[int], year_level: Optional[int]):
    db_student = db.query(StudentModel).filter(StudentModel.studentID == student_id).first()
    if db_student:
        if student_name:
            db_student.studentName = student_name
        if email:
            db_student.email = email
        if program_id:
            db_student.programID = program_id
        if year_level:
            db_student.yearLevel = year_level
        db.commit()
        db.refresh(db_student)
        return StudentBase.from_orm(db_student)  # Return Pydantic model
    return None

# Delete student
def delete_student(db: Session, student_id: int):
    db_student = db.query(StudentModel).filter(StudentModel.studentID == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
        return StudentBase.from_orm(db_student)  # Return Pydantic model
    return None
