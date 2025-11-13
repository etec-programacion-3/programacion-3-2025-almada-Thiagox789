from pydantic import BaseModel
from datetime import datetime
from typing import List

class CompraBase(BaseModel):
    usuario_id: int
    producto_id: int
    cantidad: int

class CompraCreate(CompraBase):
    pass

class Compra(CompraBase):
    id_compra: int
    # Puedes añadir más campos si tu modelo de Compra los tiene, como fecha de compra, etc.

    class Config:
        from_attributes = True

class ProductoComprado(BaseModel):
    nombre_producto: str
    descripcion_producto: str
    precio_producto: float
    cantidad: int
    image_url: str | None = None

    class Config:
        from_attributes = True

class CompraDetalle(BaseModel):
    id_compra: int
    producto: ProductoComprado
    cantidad: int
    # Agrega aquí cualquier otro detalle de la compra que quieras mostrar

    class Config:
        from_attributes = True
