from pydantic import BaseModel, EmailStr

class SSGOfficerBase(BaseModel):
    name: str
    position: str
    email: EmailStr

class SSGOfficerCreate(SSGOfficerBase):
    password: str

class SSGOfficerLogin(BaseModel):
    email: EmailStr
    password: str

class SSGOfficerResponse(SSGOfficerBase):
    officerID: int

    class Config:
        from_attributes = True
