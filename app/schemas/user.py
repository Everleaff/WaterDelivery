from pydantic import BaseModel
from typing import List, Optional
from app.schemas.orders import OrderOut  # обязательно импортируем OrderOut

class UserBase(BaseModel):
    email: str
    full_name: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserOut(UserBase):
    id: int
    orders: Optional[List[OrderOut]] = []

    class Config:
        from_attributes = True
