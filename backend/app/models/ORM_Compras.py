from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from backend.app.database.db import Base

class Compra(Base):
    __tablename__ = "compras"

    id_compra = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id_usuario"))
    producto_id = Column(Integer, ForeignKey("producto.id_producto"))
    cantidad = Column(Integer, default=1)
