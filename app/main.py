from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.users import router as users_router
from app.routers.products import router as products_router
from app.routers.orders import router as orders_router
from app.routers.delivery import router as delivery_router
from app.routers.auth import router as auth_router  # ✅ Подключаем auth

app = FastAPI(
    title="Сервис доставки воды",
    description="API для управления пользователями, продуктами, заказами, доставкой и аутентификацией.",
    version="1.0.0",
    contact={
        "name": "Ваша команда",
        "email": "support@example.com",
    },
)

# ─── Настройка CORS ─────────────────────────────
origins = [
    "http://localhost:3000",  # 🔄 Адрес фронтенда
    "http://127.0.0.1:3000",
    # "https://your-production-site.com",  # 👈 Добавь для продакшн
    # "*"  # 👈 Использовать только на этапе разработки!
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Тестовый роут ──────────────────────────────
@app.get("/", tags=["Health"])
def read_root():
    return {"message": "✅ API работает!"}

# ─── Подключение роутеров ──────────────────────
app.include_router(users_router)
app.include_router(products_router)
app.include_router(orders_router)
app.include_router(delivery_router)
app.include_router(auth_router)  # ✅ Обязательно подключить
