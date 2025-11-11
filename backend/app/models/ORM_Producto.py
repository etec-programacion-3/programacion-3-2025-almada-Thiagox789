from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..database.db import Base

class Producto(Base): # Renombrado a Producto para mayor claridad
    __tablename__ = "producto"
   
    id_producto = Column(Integer, primary_key=True, index=True)
    nombre_producto = Column(String, index=True)
    descripcion_producto = Column(String, index=True) 
    cantidad_producto = Column(Integer, index=True)
    precio_producto = Column(Float, index=True)
    image_url = Column(String, nullable=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"))

    # Relación hacia el usuario que creó el producto
    usuario = relationship("Usuario", back_populates="productos")
    # Relación hacia compras donde aparece este producto
    compras = relationship("Compra", back_populates="producto", cascade="all, delete-orphan")
