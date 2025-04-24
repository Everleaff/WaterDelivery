from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.product import ProductOut
from app.crud import product as crud_product

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/products", response_model=list[ProductOut])
def read_products(db: Session = Depends(get_db)):
    return crud_product.get_products(db)
