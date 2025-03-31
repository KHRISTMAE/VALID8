from pydantic import BaseModel, EmailStr

class OrganizerBase(BaseModel):
    organizerName: str
    email: EmailStr

class OrganizerCreate(OrganizerBase):
    password: str

class OrganizerLogin(BaseModel):
    email: EmailStr
    password: str

class OrganizerResponse(OrganizerBase):
    organizerID: int

    class Config:
        from_attributes = True
