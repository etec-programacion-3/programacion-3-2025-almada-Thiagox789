from pydantic import BaseModel, EmailStr, FIeld


#Crear valicaciones para el registro de un usuario
class RegistroUsuario(BaseModel):
    email_usuario: EmailStr
    nombre_usuario: str(FIeld(min_length=3, max_length=15))
    apellido_usuario: str(FIeld(min_length=3, max_length=15))
    password: str(FIeld(min_length=8, max_length=16))

class LogearUsuario(BaseModel):
    email_usuario: EmailStr
    nombre_usuario: str
    password: str



