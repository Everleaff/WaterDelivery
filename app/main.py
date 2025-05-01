from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.users import router as users_router
from app.routers.products import router as products_router
from app.routers.orders import router as orders_router
from app.routers.delivery import router as delivery_router

app = FastAPI(
    title="Сервис доставки воды",
    description="API для управления пользователями, продуктами, заказами и доставкой.",
    version="1.0.0",
)

# Добавляем CORS (важно для Swagger и фронта)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Здесь можно указать ['http://localhost:3000'] и т.д.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "API работает!"}

# Подключаем все роутеры
app.include_router(users_router)
app.include_router(products_router)
app.include_router(orders_router)
app.include_router(delivery_router)
