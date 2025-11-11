from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..database.db import Base


class Compra(Base):
    __tablename__ = "compras"

    id_compra = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id_usuario"))
    producto_id = Column(Integer, ForeignKey("producto.id_producto"))
    cantidad = Column(Integer, default=1)

    # Relaciones: back_populates para que la relación sea bidireccional
    usuario = relationship("Usuario", back_populates="compras")
    producto = relationship("Producto", back_populates="compras")
