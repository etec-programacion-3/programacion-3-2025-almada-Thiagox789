# backend/app/routes/producto_routes.py

from fastapi import APIRouter

router = APIRouter(
    ##Definir un prefijo para todsas las rutas en este router es como iniciar con /Pruebas
    prefix="/Prueba"
)

# Endpoint de prueba acceder mediante localhost:8000/Prueba
@router.get("/")
def leer_productos():
    return {"mensaje": "Servidor funcionando y ruta de productos OK"}
# Endpoint de prueba acceder mediante localhost:8000/Prueba/probando/otras/barras
@router.get("/probando/otras/barras")
def leer_productos():
    return {"mensaje": "Si estas viendo esto es porque anda lo que  pensaba ? "}