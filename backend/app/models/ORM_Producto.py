from sqlalchemy import *
from ..database.db import Base

class Producto(Base): # Renombrado a Producto para mayor claridad
    __tablename__ = "producto"
   
    id_producto = Column(Integer, primary_key=True, index=True)
    nombre_producto = Column(String, index=True)
    descripcion_producto = Column(String, index=True) 
    cantidad_producto = Column(Integer, index=True)
    precio_producto = Column(Float, index=True)
    image_url = Column(String, nullable=True)
