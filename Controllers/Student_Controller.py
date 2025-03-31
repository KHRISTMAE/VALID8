from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Model.Student import Student
from schemas.Student_Schema import StudentCreate, StudentResponse, StudentUpdate, PasswordUpdate
from Database.database import get_db
from typing import List
import logging
from passlib.context import CryptContext

router = APIRouter(
    prefix="/student",
    tags=["Student"]
)

# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Logger setup
logging.basicConfig(level=logging.INFO)

# ✅ Create a new student (without requiring userID, password hashed)
@router.post("/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    try:
        logging.info(f"Received student data: {student.dict()}")

        # Check if email already exists
        existing = db.query(Student).filter(Student.email == student.email).first()
        if existing:
            raise HTTPException(status_code=400, detail="Email already registered")

        # Hash the password before storing
        hashed_password = pwd_context.hash(student.password)

        # Get the latest userID from UserTable
        last_user = db.query(Student).order_by(Student.userID.desc()).first()
        new_user_id = (last_user.userID + 1) if last_user else 1  # Auto-increment logic

        new_student = Student(
            studentName=student.studentName,
            email=student.email,
            password=hashed_password,  # Hashed password
            programID=student.programID,
            yearLevel=student.yearLevel
        )
        new_student.userID = new_user_id  # Assign generated userID

        db.add(new_student)
        db.commit()
        db.refresh(new_student)

        return new_student

    except Exception as e:
        logging.error(f"Error creating student: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


# ✅ Get all students
@router.get("/", response_model=List[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    if not students:
        raise HTTPException(status_code=404, detail="No students found")
    return students


# ✅ Get single student by ID
@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.studentID == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


# ✅ Delete student
@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.studentID == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()
    logging.info(f"Student {student_id} deleted successfully.")
    return {"message": "Student deleted successfully"}


# ✅ Update student info (only name, email, year level, and programID)
@router.put("/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, updated_data: StudentUpdate, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.studentID == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Ensure email is not used by another student
    email_exists = db.query(Student).filter(Student.email == updated_data.email, Student.studentID != student_id).first()
    if email_exists:
        raise HTTPException(status_code=400, detail="Email already in use by another student")

    student.studentName = updated_data.studentName
    student.email = updated_data.email
    student.yearLevel = updated_data.yearLevel
    student.programID = updated_data.programID

    db.commit()
    db.refresh(student)

    return student


# ✅ Update student password (separate route for security)
@router.put("/{student_id}/password", status_code=status.HTTP_200_OK)
def update_student_password(student_id: int, password_update: PasswordUpdate, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.studentID == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Hash new password
    student.password = pwd_context.hash(password_update.new_password)

    db.commit()
    db.refresh(student)

    return {"message": "Password updated successfully"}
