from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.schemas.Usuario import TokenData

# Configuración para hashing de contraseñas
Cifrador = CryptContext(schemes=["bcrypt"]) # Usar bcrypt para hashear las contraseñas

# Configuración para JWT
SECRET_KEY = "CONTRASEÑA_ULTRA_SEGURRRA"
ALGORITHM = "HS256"
Expiracion_Token = 30 #Expiracion del token en minutos

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # tokenUrl es la URL donde el cliente puede obtener un token

# Funciones para hashing de contraseñas
def hashear_contraseña(password):
    return Cifrador.hash(password)

def verificar_haseho(plain_password, hashed_password):
    return Cifrador.verify(plain_password, hashed_password)

# Funciones para JWT
def crear_token_JWT(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=Expiracion_Token)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def Verificar_Token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email_usuario: str = payload.get("sub")
        if email_usuario is None:
            raise credentials_exception
        token_data = TokenData(email_usuario=email_usuario)
    except JWTError:
        raise credentials_exception
    return token_data

async def Obtener_Ususario_Actual(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return Verificar_Token(token, credentials_exception)
