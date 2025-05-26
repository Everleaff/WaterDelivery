from typing import List, Optional
from pydantic import BaseModel, EmailStr, constr
from app.schemas.orders import OrderOut  # Импорт OrderOut для вложенных заказов

# ─── Базовая схема пользователя ─────────────────────────

class UserBase(BaseModel):
    email: EmailStr  # ✅ Валидация email
    full_name: constr(min_length=1)  # ✅ Имя с мин длиной 1 символ

# ─── Для создания пользователя ──────────────────────────

class UserCreate(UserBase):
    password: constr(min_length=6)  # 🔑 Добавляем пароль (не храним в UserOut)

# ─── Для обновления пользователя ────────────────────────
# 💡 Можно сделать поля Optional если нужно частичное обновление
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[constr(min_length=1)] = None
    password: Optional[constr(min_length=6)] = None

# ─── Для вывода пользователя ────────────────────────────

class UserOut(UserBase):
    id: int
    orders: Optional[List[OrderOut]] = []  # Показываем заказы (по желанию)

    class Config:
        from_attributes = True
