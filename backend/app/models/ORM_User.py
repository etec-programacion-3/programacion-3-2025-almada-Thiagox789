from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..database.db import Base


class Usuario(Base): # Renombrado a Usuario para mayor claridad
    __tablename__ = "usuario"
   
    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre_usuario = Column(String, index=True) 
    apellido_usuario = Column(String, index=True) 
    email_usuario = Column(String, unique=True, index=True) 
    hashed_password = Column(String, index=True)
    
    # Un usuario puede tener varios productos (back_populates coincide con el atributo `usuario` en Producto)
    productos = relationship("Producto", back_populates="usuario")

    # Relación con compras: un usuario puede tener varias compras
    compras = relationship("Compra", back_populates="usuario")
