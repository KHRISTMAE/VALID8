from pydantic import BaseModel
from typing import Optional

# Schema for creating a new student
class StudentCreate(BaseModel):
    studentName: str
    email: str
    password: str
    programID: int
    yearLevel: int

    class Config:
        from_attributes = True

# Schema for updating an existing student
class StudentUpdate(BaseModel):
    studentName: Optional[str] = None
    email: Optional[str] = None
    programID: Optional[str] = None
    yearLevel: Optional[int] = None

# Response model for Student
class StudentBase(BaseModel):
    studentID: int
    studentName: str
    email: str
    programID: int
    yearLevel: int

# Combined Schema for Response
class Student(StudentBase):
    pass

class Config:
    from_attributes = True
