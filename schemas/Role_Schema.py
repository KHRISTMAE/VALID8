from pydantic import BaseModel

class RoleBase(BaseModel):
    role_name: str

class RoleCreate(RoleBase):
    pass

class RoleResponse(RoleBase):
    roleID: int

    class Config:
        from_attributes = True
