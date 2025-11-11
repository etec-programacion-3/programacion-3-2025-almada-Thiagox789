from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Esquema para el registro de un usuario
class RegistroUsuario(BaseModel):
    email_usuario: EmailStr
    nombre_usuario: str = Field(min_length=3, max_length=15)
    apellido_usuario: str = Field(min_length=3, max_length=15)
    password: str = Field(min_length=8, max_length=16)

# Esquema para el inicio de sesión de un usuario
class LoginUsuario(BaseModel):
    email_usuario: EmailStr
    password: str

# Esquema para el token JWT
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email_usuario: Optional[str] = None

class UsuarioBase(BaseModel):
    email_usuario: EmailStr
    nombre_usuario: str
    apellido_usuario: str

    class Config:
        from_attributes = True
