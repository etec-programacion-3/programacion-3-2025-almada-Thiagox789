# backend/app/routes/producto_routes.py

from fastapi import APIRouter

router = APIRouter(
    prefix="/productos",
    tags=["productos"]
)

# Endpoint de prueba
@router.get("/")
def leer_productos():
    return {"mensaje": "Servidor funcionando y ruta de productos OK"}
