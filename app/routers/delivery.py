from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db.models.delivery import Courier, DeliveryLog
from app.schemas.delivery import CourierCreate, CourierOut, DeliveryLogCreate, DeliveryLogOut

router = APIRouter(prefix="/delivery", tags=["Delivery"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/couriers", response_model=CourierOut)
def create_courier(courier: CourierCreate, db: Session = Depends(get_db)):
    db_courier = Courier(**courier.dict())
    db.add(db_courier)
    db.commit()
    db.refresh(db_courier)
    return db_courier

@router.get("/couriers", response_model=list[CourierOut])
def list_couriers(db: Session = Depends(get_db)):
    return db.query(Courier).all()

@router.delete("/couriers/{courier_id}")
def delete_courier(courier_id: int, db: Session = Depends(get_db)):
    courier = db.query(Courier).get(courier_id)
    if not courier:
        raise HTTPException(status_code=404, detail="Courier not found")
    db.delete(courier)
    db.commit()
    return {"message": "Courier deleted"}

@router.post("/log", response_model=DeliveryLogOut)
def create_delivery_log(delivery: DeliveryLogCreate, db: Session = Depends(get_db)):
    db_log = DeliveryLog(**delivery.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

@router.get("/log", response_model=list[DeliveryLogOut])
def list_delivery_logs(db: Session = Depends(get_db)):
    return db.query(DeliveryLog).all()
