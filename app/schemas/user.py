from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    full_name: str

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True  
