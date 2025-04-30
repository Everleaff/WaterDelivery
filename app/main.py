from fastapi import FastAPI
from app.routers.users import router as users_router
from app.routers.products import router as products_router
from app.routers.orders import router as orders_router
from app.routers.delivery import router as delivery_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API работает!"}

# Подключаем все роутеры
app.include_router(users_router)
app.include_router(products_router)
app.include_router(orders_router)
app.include_router(delivery_router)
