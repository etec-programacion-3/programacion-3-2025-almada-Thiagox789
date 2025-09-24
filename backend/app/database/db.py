# backend/app/database/db.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
# Decir donde estoy
Dir_Donde_Estoy=os.path.dirname(os.path.abspath(__file__))
# Configuración de la URL de la base de datos SQLite.
Ruta_DB = os.path.join(Dir_Donde_Estoy, "mundodeporte.db")


# Configuración de la URL de la base de datos SQLite.
SQLALCHEMY_DATABASE_URL = f"sqlite:///{Ruta_DB}"

# `connect_args` es necesario para SQLite.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# `sessionmaker` es una clase que nos permite crear sesiones de base de datos.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# `declarative_base` nos permite crear modelos ORM.
Base = declarative_base()