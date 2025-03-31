from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Database.database import get_db
from Model.Attendance import Attendance
from schemas.Attendance_Schema import AttendanceCreate, AttendanceResponse
from Repository.AttendanceRepository import AttendanceRepository

router = APIRouter(prefix="/attendances", tags=["Attendances"])

@router.post("/", response_model=AttendanceResponse)
def create_attendance(att_create: AttendanceCreate, db: Session = Depends(get_db)):
    repo = AttendanceRepository(db)
    new_att = Attendance(user_id=att_create.user_id, event_id=att_create.event_id)
    created = repo.create(new_att)
    return created

@router.get("/", response_model=list[AttendanceResponse])
def get_all_attendances(db: Session = Depends(get_db)):
    repo = AttendanceRepository(db)
    return repo.get_all()

@router.get("/{attendance_id}", response_model=AttendanceResponse)
def get_attendance(attendance_id: int, db: Session = Depends(get_db)):
    repo = AttendanceRepository(db)
    attendance = repo.get_by_id(attendance_id)
    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance not found")
    return attendance

@router.delete("/{attendance_id}")
def delete_attendance(attendance_id: int, db: Session = Depends(get_db)):
    repo = AttendanceRepository(db)
    attendance = repo.get_by_id(attendance_id)
    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance not found")
    repo.delete(attendance)
    return {"message": "Attendance deleted successfully"}
