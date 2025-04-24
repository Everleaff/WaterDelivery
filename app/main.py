from fastapi import FastAPI
from app.routers.users import router as users_router
from app.routers.products import router as products_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API работает!"}

app.include_router(users_router)
app.include_router(products_router)
