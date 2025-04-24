from pydantic import BaseModel

class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    price: float
    image_url: str | None = None

    class Config:
        from_attributes = True 
