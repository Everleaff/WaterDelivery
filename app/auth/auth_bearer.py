from fastapi.security import OAuth2PasswordBearer

# URL для логина (куда фронт/постман будет отправлять логин-запрос)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
