from pydantic import BaseModel
from .Usuario import UsuarioBase # Importar el esquema de usuario

class ProductoBase(BaseModel):
    nombre_producto: str
    descripcion_producto: str
    cantidad_producto: int
    precio_producto: float
    image_url: str | None = None

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    nombre_producto: str | None = None
    descripcion_producto: str | None = None
    cantidad_producto: int | None = None
    precio_producto: float | None = None
    image_url: str | None = None

class Producto(ProductoBase):
    id_producto: int
    id_usuario: int | None = None  # Make id_usuario optional
    image_url: str | None = None
    usuario: UsuarioBase | None = None # Añadir el usuario asociado
    
    class Config:
        from_attributes = True
