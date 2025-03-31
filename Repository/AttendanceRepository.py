from sqlalchemy.orm import Session
from Model.Attendance import Attendance

class AttendanceRepository:
    def __init__(self, db):
        self.db = db

    def create(self, attendance):
        self.db.add(attendance)
        self.db.commit()
        self.db.refresh(attendance)
        return attendance

    def get_all(self):
        return self.db.query(Attendance).all()

    def get_by_id(self, attendance_id):
        return self.db.query(Attendance).filter(Attendance.id == attendance_id).first()

    def delete(self, attendance):
        self.db.delete(attendance)
        self.db.commit()
