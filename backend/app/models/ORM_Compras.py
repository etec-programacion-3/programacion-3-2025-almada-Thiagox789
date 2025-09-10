from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Compra(Base):
    __tablename__ = "compras"

    id_compra = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id_usuario"))
    producto_id = Column(Integer, ForeignKey("productos.id_producto"))
    cantidad = Column(Integer, default=1)
