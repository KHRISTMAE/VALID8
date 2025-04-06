from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import CRUD
from Database.database import SessionLocal
from schemas import StudentCreate, StudentUpdate, StudentBase
from Model import Student as StudentModel  # Make sure you import the correct model

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new student
@router.post("/students/", response_model=StudentBase)
def create_student_view(student: StudentCreate, db: Session = Depends(get_db)):
    return CRUD.create_student(db, student.studentName, student.email, student.password, student.programID, student.yearLevel)

# Get student by ID
@router.get("/students/{studentID}", response_model=StudentBase)
def get_student_view(studentID: int, db: Session = Depends(get_db)):
    db_student = CRUD.get_student_by_id(db, studentID)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return StudentBase.from_orm(db_student)  # Ensure it returns the Pydantic model

# Get a list of students
@router.get("/students/", response_model=list[StudentBase])
def get_students_view(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = CRUD.get_students(db, skip=skip, limit=limit)
    return [StudentBase.from_orm(student) for student in students]  # Return a list of Pydantic models

# Update student information
@router.put("/students/{studentID}", response_model=StudentBase)
def update_student_view(studentID: int, student: StudentUpdate, db: Session = Depends(get_db)):
    db_student = CRUD.update_student(db, studentID, student.studentName, student.email, student.programID, student.yearLevel)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

# Delete student by ID
@router.delete("/students/{studentID}", response_model=StudentBase)
def delete_student_view(studentID: int, db: Session = Depends(get_db)):
    db_student = CRUD.delete_student(db, studentID)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student
