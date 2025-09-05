from sqlalchemy import Column, Integer, String
from .db import Base

class producto(Base):
    __tablename__ = "producto"
    ID_Producto = Column(Integer, primary_key=True, index=True)
    Precio = Column(float, index=True)
    Cantidad = Column(Integer, index=True)  