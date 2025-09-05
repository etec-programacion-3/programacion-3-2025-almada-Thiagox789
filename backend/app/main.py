from fastapi import FastAPI
from app.routes.Route_Producto import router as producto_router
app = FastAPI()

app.include_router(producto_router)
