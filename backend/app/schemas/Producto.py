from pydantic import BaseModel

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
    image_url: str | None = None
    
    class Config:
        orm_mode = True
