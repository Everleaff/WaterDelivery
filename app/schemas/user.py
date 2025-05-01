from pydantic import BaseModel
from typing import List, Optional
from app.schemas.orders import OrderOut  # обязательно импортируем OrderOut
from pydantic import BaseModel, EmailStr, constr

class UserBase(BaseModel):
    email: EmailStr  # Проверка правильного email-адреса
    full_name: constr(min_length=1)  # Строка с минимум 1 символом
    
class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserOut(UserBase):
    id: int
    orders: Optional[List[OrderOut]] = []

    class Config:
        from_attributes = True
