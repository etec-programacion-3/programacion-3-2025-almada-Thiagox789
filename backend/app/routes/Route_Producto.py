# backend/app/routes/Route_Producto.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database.db import get_db
from app.models.ORM_Producto import Producto as ORMProducto
from app.schemas.Producto import Producto

router = APIRouter(
    prefix="/productos",
    tags=["productos"]
)

# Endpoint para listar todos los productos (sin autenticación)
@router.get("/", response_model=List[Producto])
def leer_productos(db: Session = Depends(get_db)): # Conectarse a la db
    productos = db.query(ORMProducto).all() # Consulta todos los productos registrados en la db
    return productos

# Endpoint para obtener un producto por ID (sin autenticación)
@router.get("/{producto_id}", response_model=Producto)
def leer_producto_por_id(producto_id: int, db: Session = Depends(get_db)):
    producto = db.get(ORMProducto, producto_id)
    if producto is None:    # Si el producto no se encuentra, devolver un producto no encontrado y el famoso error 404
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado :("
        )
    return producto

@router.post("/")
def crear_producto():
    return {"mensaje": "Servidor funcionando y ruta de productos crear OK"}
@router.put("/{producto_id}")
def actualizar_producto(producto_id):
    return {"mensaje": "Servidor funcionando y ruta de productos actualizar OK"}
@router.delete("/{producto_id}")
def eliminar_producto(producto_id):
    return {"mensaje": "Servidor funcionando y ruta de productos eliminar OK"}
