# backend/app/routes/Route_Producto.py

from fastapi import APIRouter

router = APIRouter(
    ##Definir un prefijo para todsas las rutas en este router es como iniciar con /productos
    prefix="/productos"
)
##no terminado solo borrador de pruba, todavia falta logica
# Endpoint de prueba acceder mediante localhost:8000/prueba
@router.get("/")
def leer_productos():
    return {"mensaje": "Servidor funcionando y ruta de productos OK"}
@router.get("/{producto_id}")
def leer_productos_por_id(producto_id):
    return {"mensaje": "Servidor funcionando y ruta de productos por id OK"}
@router.post("/")
def crear_producto():
    return {"mensaje": "Servidor funcionando y ruta de productos crear OK"}
@router.put("/{producto_id}")
def actualizar_producto(producto_id):
    return {"mensaje": "Servidor funcionando y ruta de productos actualizar OK"}
@router.delete("/{producto_id}")
def eliminar_producto(producto_id):
    return {"mensaje": "Servidor funcionando y ruta de productos eliminar OK"}
