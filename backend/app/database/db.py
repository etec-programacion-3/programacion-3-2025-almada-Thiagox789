# backend/app/database/db.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la URL de la base de datos SQLite.
SQLALCHEMY_DATABASE_URL = "sqlite:///./mundodeporte.db"

# `connect_args` es necesario para SQLite.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# `sessionmaker` es una clase que nos permite crear sesiones de base de datos.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# `declarative_base` nos permite crear modelos ORM.
Base = declarative_base()