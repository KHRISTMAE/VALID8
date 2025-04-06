from pydantic import BaseModel

class UserTableBase(BaseModel):
    roleID: int
    role: str

class UserTableCreate(UserTableBase):
    pass

class UserTable(UserTableBase):
    userID: int

    class Config:
        from_attributes = True  # This allows Pydantic to work with SQLAlchemy models directly
