from sqlalchemy import *
from .db import Base

class Usuario(Base): # Renombrado a Usuario para mayor claridad
    __tablename__ = "usuario"
   
    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre_usuario = Column(String, index=True) 
    apellido_usuario = Column(String, index=True) 
    email_usuario = Column(String, unique=True, index=True) 
    contraseña_hasheada = Column(String, index=True) 
