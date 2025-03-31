from pydantic import BaseModel

class OfficerEventBase(BaseModel):
    officer_id: int
    event_id: int

class OfficerEventCreate(OfficerEventBase):
    pass

class OfficerEventResponse(OfficerEventBase):
    class Config:
        from_attributes = True
