from Model.Student import Student
from Database.database import Base

class StudentRepository:
    def __init__(self, db):
        self.db = db

    def get_all_students(self):
        return self.db.query(Student).all()

    def add_student(self, student: Student):
        self.db.add(student)
        self.db.commit()
        self.db.refresh(student)
        return student
