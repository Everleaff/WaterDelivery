from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# ─── Курьеры ─────────────────────────────

class CourierBase(BaseModel):
    name: str
    phone: str

class CourierCreate(CourierBase):
    pass

class CourierUpdate(CourierBase):
    pass  # если вдруг нужно будет редактировать

class CourierOut(CourierBase):
    id: int

    class Config:
        from_attributes = True

# ─── Лог доставки ────────────────────────

class DeliveryLogCreate(BaseModel):
    order_id: int
    courier_id: int

class DeliveryLogOut(BaseModel):
    id: int
    order_id: int
    courier_id: int
    delivered_at: datetime

    class Config:
        from_attributes = True
