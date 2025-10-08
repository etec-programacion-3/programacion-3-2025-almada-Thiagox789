from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.database.db import SessionLocal
from backend.app.models.ORM_User import Usuario
from backend.app.schemas.Usuario import RegistroUsuario, LoginUsuario, Token, TokenData
from backend.auth import get_password_hash, verify_password, create_access_token, get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["Autenticación"]
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=dict)
def register_user(user: RegistroUsuario, db: Session = Depends(get_db)):
    db_user = db.query(Usuario).filter(Usuario.email_usuario == user.email_usuario).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El email ya está registrado")
    
    hashed_password = get_password_hash(user.password)
    
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
def login_for_access_token(user_credentials: LoginUsuario, db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.email_usuario == user_credentials.email_usuario).first()
    if not user or not verify_password(user_credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.email_usuario}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/protected", response_model=dict)
async def protected_route(current_user: TokenData = Depends(get_current_user)):
    return {"mensaje": f"Bienvenido, {current_user.email_usuario}! Has accedido a una ruta protegida."}
