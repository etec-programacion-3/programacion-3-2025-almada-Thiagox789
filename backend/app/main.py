from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def Ruta_De_Pruebas():
    return "Si ves esto anda :)"