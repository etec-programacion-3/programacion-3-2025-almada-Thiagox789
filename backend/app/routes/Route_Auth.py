from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.models.ORM_User import Usuario
from app.schemas.Usuario import RegistroUsuario, LoginUsuario, Token, TokenData, UsuarioBase
from auth import hashear_contraseña, verificar_haseho, crear_token_JWT, Obtener_Ususario_Actual


router = APIRouter(
    prefix="/auth",
)

# Obtener la sesión de la base de datos
def Ontener_Sesion_DB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
#cerrar la sesion de la base de datos cuando se termine. 

@router.post("/register", response_model=dict)
def registrar_usuario(user: RegistroUsuario, db: Session = Depends(Ontener_Sesion_DB)):
    db_user = db.query(Usuario).filter(Usuario.email_usuario == user.email_usuario).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El email ya está registrado")
    
    hashed_password = hashear_contraseña(user.password)
    
    new_user = Usuario(
        email_usuario=user.email_usuario,
        nombre_usuario=user.nombre_usuario,
        apellido_usuario=user.apellido_usuario,
        hashed_password=hashed_password # Guardar la contraseña hasheada
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"mensaje": "Usuario registrado exitosamente"}

@router.post("/login", response_model=Token)
def iniciar_sesion_para_token_acceso(user_credentials: LoginUsuario, db: Session = Depends(Ontener_Sesion_DB)):
    user = db.query(Usuario).filter(Usuario.email_usuario == user_credentials.email_usuario).first()
    if not user or not verificar_haseho(user_credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = crear_token_JWT(
        data={"sub": user.email_usuario}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/protected", response_model=dict)
async def ruta_protegida(current_user: TokenData = Depends(Obtener_Ususario_Actual)):
    return {"mensaje": f"Bienvenido, {current_user.email_usuario}! Has accedido a una ruta protegida."}

@router.get("/me", response_model=UsuarioBase)
def get_current_user(current_user: TokenData = Depends(Obtener_Ususario_Actual), db: Session = Depends(Ontener_Sesion_DB)):
    user = db.query(Usuario).filter(Usuario.email_usuario == current_user.email_usuario).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado",
        )
    return user
