from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime

class Courier(Base):
    __tablename__ = "couriers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    phone = Column(String(20))

    deliveries = relationship("DeliveryLog", back_populates="courier")


class DeliveryLog(Base):
    __tablename__ = "delivery_log"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    courier_id = Column(Integer, ForeignKey("couriers.id"))
    delivered_at = Column(DateTime, default=datetime.utcnow)

    courier = relationship("Courier", back_populates="deliveries")
