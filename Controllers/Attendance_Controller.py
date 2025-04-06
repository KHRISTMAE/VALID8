# controllers.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from CRUD import create_attendance, get_attendance, get_attendance_by_id, update_attendance, delete_attendance
from schemas import AttendanceCreate, AttendanceUpdate, AttendanceOut
from Database.database import get_db

router = APIRouter()

# Create a new Attendance record
@router.post("/createAttendances/", response_model=AttendanceOut)
def create_attendance_record(attendance: AttendanceCreate, db: Session = Depends(get_db)):
    return create_attendance(db, attendance)


# Get all Attendance records
@router.get("/readAttendances/", response_model=list[AttendanceOut])
def read_attendances(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_attendance(db, skip=skip, limit=limit)


# Get an Attendance record by ID
@router.get("/readAllAttendances/{attendanceID}", response_model=AttendanceOut)
def read_attendance(attendanceID: int, db: Session = Depends(get_db)):
    attendance = get_attendance_by_id(db, attendanceID)
    if attendance is None:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return attendance


# Update an Attendance record
@router.put("/updateAttendances/{attendanceID}", response_model=AttendanceOut)
def update_attendance_record(attendanceID: int, attendance: AttendanceUpdate, db: Session = Depends(get_db)):
    updated_attendance = update_attendance(db, attendanceID, attendance)
    if updated_attendance is None:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return updated_attendance


# Delete an Attendance record
@router.delete("/deleteAttendances/{attendanceID}", response_model=AttendanceOut)
def delete_attendance_record(attendanceID: int, db: Session = Depends(get_db)):
    deleted_attendance = delete_attendance(db, attendanceID)
    if deleted_attendance is None:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return deleted_attendance
