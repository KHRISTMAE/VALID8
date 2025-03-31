from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    userID: int
    username: str
    email: EmailStr

    class Config:
        from_Attributes = True
