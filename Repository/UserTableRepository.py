from sqlalchemy.orm import Session 
from Model.UserTable import UserTable

class UserTableRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> UserTable | None:
        return self.db.query(UserTable).filter(UserTable.email == email).first()

    def get_by_username(self, username: str) -> UserTable | None:
        return self.db.query(UserTable).filter(UserTable.username == username).first()

    def get_by_id(self, user_id: int) -> UserTable | None:
        return self.db.query(UserTable).filter(UserTable.userID == user_id).first()

    def create(self, user: UserTable) -> UserTable:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user: UserTable):
        self.db.delete(user)
        self.db.commit()
