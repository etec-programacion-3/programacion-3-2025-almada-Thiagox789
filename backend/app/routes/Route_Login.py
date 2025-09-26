# backend/app/routes/Route_Login.py

from fastapi import APIRouter

router = APIRouter(
    ##Definir un prefijo para todsas las rutas en este router es como iniciar con /prueba
    prefix="/prueba"
)