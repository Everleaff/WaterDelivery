from pydantic import BaseModel, constr, condecimal, HttpUrl
from typing import Optional

class ProductBase(BaseModel):
    name: constr(min_length=1, max_length=100)
    description: constr(min_length=1)
    price: condecimal(gt=0)
    image_url: Optional[HttpUrl] = None  # Строгое соответствие URL

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int

    class Config:
        from_attributes = True
