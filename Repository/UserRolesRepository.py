from sqlalchemy.orm import Session #type:ignore
from Model.UserRoles import UserRoles # type: ignore

class UserRolesRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_user_id(self, user_id: int) -> list[UserRoles]:
        return self.db.query(UserRoles).filter(UserRoles.user_id == user_id).all()

    def get_by_role_id(self, role_id: int) -> list[UserRoles]:
        return self.db.query(UserRoles).filter(UserRoles.role_id == role_id).all()

    def get_all(self) -> list[UserRoles]:
        return self.db.query(UserRoles).all()

    def create(self, user_role: UserRoles) -> UserRoles:
        self.db.add(user_role)
        self.db.commit()
        self.db.refresh(user_role)
        return user_role
