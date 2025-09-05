from sqlalchemy import *
from .db import Base

class productos(Base):
    __tablename__ = "producto"
   
    id_producto = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    precio = Column(Float, index=True)
    cantidad = Column(Integer, index=True)