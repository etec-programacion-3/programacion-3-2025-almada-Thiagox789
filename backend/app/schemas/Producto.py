class ProductoBase(BaseModel):
    nombre_producto: str
    descripcion_producto: str
    cantidad_producto: int
    precio_producto: float

class ProductoCreate(ProductoBase):
    pass

class Producto(ProductoBase):
    id_producto: int
    
    class Config:
        orm_mode = True