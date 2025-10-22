# backend/app/routes/Route_Producto.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database.db import get_db
from app.models.ORM_Producto import Producto as ORMProducto
from app.schemas.Producto import Producto, ProductoCreate, ProductoUpdate
from backend.auth import get_current_user

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
def leer_producto_por_id(
    producto_id: int, 
    db: Session = Depends(get_db)):
        producto = db.get(ORMProducto, producto_id)
        if producto is None:    # Si el producto no se encuentra, devolver un producto no encontrado y el famoso error 404
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Producto no encontrado :("
            )
        return producto

# Endpoint para crear un nuevo producto (con autenticación)
@router.post("/", response_model=Producto, status_code=status.HTTP_201_CREATED)
def crear_producto(
    producto: ProductoCreate,                     # Recibe los datos del producto en formato JSON según el esquema ProductoCreate
    db: Session = Depends(get_db),                # Conectarse a la base de datos
    current_user: dict = Depends(get_current_user) # Verifica que el usuario esté autenticado
):
    db_producto = ORMProducto(**producto.dict())  # Crea un objeto ORMProducto con los datos recibidos
    db.add(db_producto)                           # Agrega el producto a la sesión de la base de datos
    db.commit()                                   # Confirma los cambios en la base de datos
    db.refresh(db_producto)                       # Actualiza el objeto con valores generados automáticamente (como id)
    return db_producto                            # Devuelve el producto creado al cliente

#Ia #
@router.put("/{producto_id}", response_model=Producto)
def actualizar_producto(
    producto_id: int,
    producto_update: ProductoUpdate, # Usamos ProductoUpdate para la actualización
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    db_producto = db.get(ORMProducto, producto_id)
    if db_producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado :("
        )
    
    for key, value in producto_update.dict(exclude_unset=True).items():
        setattr(db_producto, key, value)
    
    db.commit()
    db.refresh(db_producto)
    return db_producto

@router.delete("/{producto_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_producto(
    producto_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    db_producto = db.get(ORMProducto, producto_id)
    if db_producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado :("
        )
    
    db.delete(db_producto)
    db.commit()
    return {"mensaje": "Producto eliminado exitosamente"}
