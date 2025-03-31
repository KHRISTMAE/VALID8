from sqlalchemy.orm import Session
from Model.Role import Role

class RoleRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, role: Role):
        self.db.add(role)
        self.db.commit()
        self.db.refresh(role)
        return role

    def get_all(self):
        return self.db.query(Role).all()

    def get_by_id(self, role_id: int):
        return self.db.query(Role).filter(Role.roleID == role_id).first()

    def delete(self, role: Role):
        self.db.delete(role)
        self.db.commit()
