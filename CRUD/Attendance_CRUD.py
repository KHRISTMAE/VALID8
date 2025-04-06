from sqlalchemy.orm import Session
from Model import Attendance, Student, Event
from schemas import AttendanceCreate, AttendanceUpdate

def create_attendance(db: Session, attendance: AttendanceCreate):
    """
    Create a new attendance record.
    """
    # Validate if student exists
    student = db.query(Student).filter(Student.studentID == attendance.studentID).first()
    if not student:
        raise ValueError(f"Student with ID {attendance.studentID} not found.")

    # Validate if event exists
    event = db.query(Event).filter(Event.eventID == attendance.eventID).first()
    if not event:
        raise ValueError(f"Event with ID {attendance.eventID} not found.")

    # Create new attendance record
    db_attendance = Attendance(
        studentID=attendance.studentID,
        eventID=attendance.eventID,
        checkInTime=attendance.checkInTime,
        status=attendance.status
    )
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance


def get_attendance(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieve a list of attendance records with pagination.
    """
    return db.query(Attendance).offset(skip).limit(limit).all()


def get_attendance_by_id(db: Session, attendanceID: int):
    """
    Retrieve an attendance record by its ID.
    """
    return db.query(Attendance).filter(Attendance.attendanceID == attendanceID).first()


def update_attendance(db: Session, attendanceID: int, attendance: AttendanceUpdate):
    """
    Update an attendance record.
    """
    # Find the attendance record to update
    db_attendance = db.query(Attendance).filter(Attendance.attendanceID == attendanceID).first()
    
    if not db_attendance:
        return {"message": f"Attendance record with ID {attendanceID} not found."}

    # Update the attendance record
    db_attendance.studentID = attendance.studentID
    db_attendance.eventID = attendance.eventID
    db_attendance.checkInTime = attendance.checkInTime
    db_attendance.status = attendance.status
    
    db.commit()
    db.refresh(db_attendance)
    
    return db_attendance


def delete_attendance(db: Session, attendanceID: int):
    """
    Delete an attendance record by ID.
    """
    # Find the attendance record to delete
    db_attendance = db.query(Attendance).filter(Attendance.attendanceID == attendanceID).first()
    
    if not db_attendance:
        return {"message": f"Attendance record with ID {attendanceID} not found."}
    
    db.delete(db_attendance)
    db.commit()
    
    return {"message": f"Attendance record with ID {attendanceID} deleted."}
