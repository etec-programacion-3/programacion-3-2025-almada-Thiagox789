# backend/app/routes/Route_usuario.py
from fastapi import APIRouter

# Definir el router
router = APIRouter
@router.post("/registro")
def RegistrarUsuario(usuario: Usuario):
    return {"mensaje": "Usuario registrado correctamente", "usuario": usuario}
