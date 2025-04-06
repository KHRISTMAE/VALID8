from pydantic import BaseModel

class UserRoleBase(BaseModel):
    userID: int
    roleID: int

class UserRoleCreate(UserRoleBase):
    pass

class UserRoleUpdate(UserRoleBase):
    pass

class UserRoleInDB(UserRoleBase):
    userRoleID: int

    class Config:
        from_attributes = True
