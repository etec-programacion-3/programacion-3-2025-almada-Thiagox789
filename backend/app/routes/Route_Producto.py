# backend/app/routes/Route_Producto.py

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session, joinedload # Importar joinedload
from typing import List

from app.database.db import get_db
from app.models.ORM_Producto import Producto as ORMProducto
from app.models.ORM_User import Usuario as ORMUsuario
from app.schemas.Producto import Producto, ProductoCreate, ProductoUpdate
from auth import Obtener_Ususario_Actual

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

# Endpoint para listar todos los productos (sin autenticación)
@router.get("/", response_model=List[Producto])
def leer_productos(
    db: Session = Depends(get_db),
    min_price: float = None,
    max_price: float = None
):
    query = db.query(ORMProducto).options(joinedload(ORMProducto.usuario)) # Eager-load user
    if min_price is not None:
        query = query.filter(ORMProducto.precio_producto >= min_price)
    if max_price is not None:
        query = query.filter(ORMProducto.precio_producto <= max_price)
    
    productos = query.all()
    return productos

# Endpoint para obtener un producto por ID (sin autenticación)
@router.get("/{producto_id}", response_model=Producto)
def leer_producto_por_id(
    producto_id: int, 
    db: Session = Depends(get_db)):
        producto = db.query(ORMProducto).options(joinedload(ORMProducto.usuario)).filter(ORMProducto.id_producto == producto_id).first() # Eager-load user
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
    current_user: dict = Depends(Obtener_Ususario_Actual) # Verifica que el usuario esté autenticado
):
    # Buscar usuario en base al token (current_user contiene email_usuario)
    usuario = db.query(ORMUsuario).filter(ORMUsuario.email_usuario == getattr(current_user, 'email_usuario', None)).first()
    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario no encontrado o no autorizado")

    # Crear producto y asignar el id del usuario que lo crea
    data = producto.dict()
    data['id_usuario'] = usuario.id_usuario
    db_producto = ORMProducto(**data)
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

#Ia #
@router.put("/{producto_id}", response_model=Producto)
def actualizar_producto(
    producto_id: int,
    producto_update: ProductoUpdate, # Usamos ProductoUpdate para la actualización
    db: Session = Depends(get_db),
    current_user: dict = Depends(Obtener_Ususario_Actual)
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
    current_user: dict = Depends(Obtener_Ususario_Actual)
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

class StockUpdate(BaseModel):
    quantity: int

@router.put("/{producto_id}/stock", response_model=Producto)
def actualizar_stock(
    producto_id: int,
    stock_update: StockUpdate,
    db: Session = Depends(get_db)
):
    db_producto = db.get(ORMProducto, producto_id)
    if db_producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado :("
        )
    
    if db_producto.cantidad_producto < stock_update.quantity:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No hay suficiente stock para completar la compra."
        )
    
    db_producto.cantidad_producto -= stock_update.quantity
    db.commit()
    db.refresh(db_producto)
    return db_producto
