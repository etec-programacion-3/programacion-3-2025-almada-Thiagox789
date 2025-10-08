from fastapi import FastAPI
from backend.app.routes.Route_Producto import router as producto_router
from backend.app.routes.Route_Auth import router as auth_router
from backend.app.database.db import Base, engine
# Crear la aplicacion FastAPI
app = FastAPI()

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app.include_router(producto_router)
app.include_router(auth_router)
