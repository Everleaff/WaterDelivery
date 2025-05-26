from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.database import SessionLocal
from app.db.models.users import User
from app.db.models.orders import Order
from app.schemas.user import UserCreate, UserUpdate, UserOut
from app.schemas.orders import OrderOut

router = APIRouter(prefix="/users", tags=["Users"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED, summary="Создать пользователя")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Создаёт нового пользователя."""
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/", response_model=List[UserOut], summary="Получить всех пользователей")
def get_all_users(db: Session = Depends(get_db)):
    """Возвращает список всех пользователей."""
    return db.query(User).all()


@router.get("/{user_id}", response_model=UserOut, summary="Получить пользователя по ID")
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Возвращает пользователя по его ID."""
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserOut, summary="Обновить пользователя")
def update_user(user_id: int, updated: UserUpdate, db: Session = Depends(get_db)):
    """Обновляет данные пользователя по его ID."""
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in updated.dict().items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Удалить пользователя")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Удаляет пользователя по его ID."""
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted"}


@router.get("/{user_id}/orders", response_model=List[OrderOut], summary="Получить все заказы пользователя")
def get_user_orders(user_id: int, db: Session = Depends(get_db)):
    """Возвращает список всех заказов указанного пользователя."""
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    orders = db.query(Order).filter(Order.user_id == user_id).all()
    return orders
