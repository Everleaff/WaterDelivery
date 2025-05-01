from pydantic import BaseModel, conint, confloat
from typing import List
from datetime import datetime

# ─── OrderItem ──────────────────────────────

class OrderItemBase(BaseModel):
    product_id: int
    quantity: conint(gt=0)
    price: confloat(gt=0)

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemOut(OrderItemBase):
    id: int

    class Config:
        from_attributes = True

# ─── Order ──────────────────────────────────

class OrderCreate(BaseModel):
    user_id: int
    items: List[OrderItemCreate]

class OrderOut(BaseModel):
    id: int
    user_id: int
    status: str  # Можно добавить constr(min_length=1) если нужно
    created_at: datetime
    items: List[OrderItemOut]

    class Config:
        from_attributes = True
