from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database.db import get_db
from app.models.ORM_Compras import Compra as ORMCompra
from app.models.ORM_Producto import Producto as ORMProducto
from app.models.ORM_User import Usuario as ORMUsuario
from auth import Obtener_Ususario_Actual
from pydantic import BaseModel
from typing import List


class PurchaseItem(BaseModel):
    producto_id: int
    cantidad: int


class PurchaseCreate(BaseModel):
    items: List[PurchaseItem]

router = APIRouter(
    prefix="/purchases",
    tags=["purchases"]
)


@router.get("/me")
def obtener_compras_mias(current_user = Depends(Obtener_Ususario_Actual), db: Session = Depends(get_db)):
    # current_user contains TokenData with email_usuario
    if not current_user or not getattr(current_user, 'email_usuario', None):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No autorizado")

    usuario = db.query(ORMUsuario).filter(ORMUsuario.email_usuario == current_user.email_usuario).first()
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

    compras = db.query(ORMCompra).filter(ORMCompra.usuario_id == usuario.id_usuario).all()

    # Construir respuesta enriquecida incluyendo datos del producto cuando estén disponibles
    resultado = []
    for c in compras:
        producto = db.get(ORMProducto, c.producto_id)
        producto_data = None
        if producto is not None:
            producto_data = {
                "id_producto": producto.id_producto,
                "nombre_producto": producto.nombre_producto,
                "descripcion_producto": producto.descripcion_producto,
                "cantidad_producto": producto.cantidad_producto,
                "precio_producto": producto.precio_producto,
                "image_url": getattr(producto, 'image_url', None)
            }

        resultado.append({
            "id_compra": c.id_compra,
            "usuario_id": c.usuario_id,
            "producto_id": c.producto_id,
            "cantidad": c.cantidad,
            "producto": producto_data
        })

    return resultado


@router.post("/")
def crear_compras(purchase: PurchaseCreate, current_user = Depends(Obtener_Ususario_Actual), db: Session = Depends(get_db)):
    # Verificar usuario
    if not current_user or not getattr(current_user, 'email_usuario', None):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No autorizado")

    usuario = db.query(ORMUsuario).filter(ORMUsuario.email_usuario == current_user.email_usuario).first()
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

    created = []

    # Procesar todas las items: validar stock y crear Compra
    for item in purchase.items:
        producto = db.get(ORMProducto, item.producto_id)
        if producto is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Producto {item.producto_id} no encontrado")
        if producto.cantidad_producto < item.cantidad:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"No hay suficiente stock para el producto {producto.nombre_producto}")

        # Reducir stock
        producto.cantidad_producto -= item.cantidad

        # Crear registro de compra
        compra = ORMCompra(usuario_id=usuario.id_usuario, producto_id=producto.id_producto, cantidad=item.cantidad)
        db.add(compra)
        db.add(producto)  # producto ya está en sesión, esto asegura cambios en commit
        db.commit()
        db.refresh(compra)

        created.append({
            "id_compra": compra.id_compra,
            "producto_id": compra.producto_id,
            "cantidad": compra.cantidad
        })

    return {"created": created}
