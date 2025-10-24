from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.Route_Producto import router as producto_router
from app.routes.Route_Auth import router as auth_router
from app.database.db import Base, engine
# Crear la aplicacion FastAPI
app = FastAPI()

# Configurar CORS
origins = [
    "http://localhost",
    "http://localhost:5173",  # El origen de tu frontend de Vite
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app.include_router(producto_router)
app.include_router(auth_router)
