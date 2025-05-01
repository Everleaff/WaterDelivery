from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from app.db.database import SessionLocal
from app.db.models.orders import Order, OrderItem
from app.schemas.orders import OrderCreate, OrderOut
from typing import List

router = APIRouter(prefix="/orders", tags=["Orders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=OrderOut, summary="Создать заказ")
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = Order(user_id=order.user_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    for item in order.items:
        db_item = OrderItem(order_id=db_order.id, **item.dict())
        db.add(db_item)
    db.commit()

    return db_order

@router.get("/", response_model=List[OrderOut], summary="Получить все заказы")
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()

@router.get("/{order_id}", response_model=OrderOut, summary="Получить заказ по ID")
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.get("/{order_id}/full", summary="Получить заказ + пользователь + позиции")
def get_order_full(order_id: int, db: Session = Depends(get_db)):
    order = (
        db.query(Order)
        .options(
            joinedload(Order.user),
            joinedload(Order.items)
        )
        .filter(Order.id == order_id)
        .first()
    )
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return {
        "order_id": order.id,
        "status": order.status,
        "created_at": order.created_at,
        "user": {
            "id": order.user.id,
            "email": order.user.email,
            "full_name": order.user.full_name
        },
        "items": [
            {
                "id": item.id,
                "product_id": item.product_id,
                "quantity": item.quantity,
                "price": item.price
            }
            for item in order.items
        ],
        "total_amount": sum(item.price * item.quantity for item in order.items)
    }
