# Proyecto Backend con FastAPI - MundoDeporte

## Descripción del Proyecto

Este proyecto es el backend de un e-commerce dedicado a la venta de productos deportivos, llamado "MundoDeporte". Está desarrollado con FastAPI y utiliza SQLAlchemy como ORM para interactuar con una base de datos SQLite.

La estructura del proyecto está organizada para ser escalable y modular, incluyendo funcionalidades de autenticación de usuarios mediante JSON Web Tokens (JWT).

## Estructura del Proyecto
```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── db.py
│   │   └── mundodeporte.db
│   ├── models/
│   │   ├── __init__.py
│   │   ├── ORM_Compras.py
│   │   ├── ORM_Producto.py
│   │   └── ORM_User.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── Route_Auth.py
│   │   ├── Route_Producto.py
│   │   ├── Route_usuario.py
│   │   └── Routes_Pruebas.py
│   └── schemas/
│       ├── Producto.py
│       └── Usuario.py
├── auth.py
├── alembic/
├── alembic.ini
├── requirements.txt
└── README.md
```

### Explicación de Carpetas y Archivos Clave

*   **`backend/`**: Directorio raíz del proyecto backend.
    *   **`app/`**: Contiene la lógica principal de la aplicación FastAPI.
        *   **`main.py`**: Es el punto de entrada de la aplicación FastAPI. Aquí se inicializa la aplicación, se configuran las rutas y se crea la base de datos.
        *   **`database/`**: Contiene la configuración de la base de datos.
            *   **`db.py`**: Define la conexión a la base de datos SQLite, el motor (engine) de SQLAlchemy, la clase `SessionLocal` para crear sesiones de base de datos y la `Base` declarativa para los modelos ORM.
            *   **`mundodeporte.db`**: El archivo de la base de datos SQLite.
        *   **`models/`**: Contiene las definiciones de los modelos ORM de SQLAlchemy.
            *   **`ORM_Compras.py`**: Modelo ORM para las compras.
            *   **`ORM_Producto.py`**: Modelo ORM para los productos.
            *   **`ORM_User.py`**: Modelo ORM para los usuarios, incluyendo campos para email, nombre, apellido y contraseña hasheada.
        *   **`routes/`**: Contiene las rutas (endpoints) de la API.
            *   **`Route_Auth.py`**: Define los endpoints para el registro de usuarios (`/auth/register`), inicio de sesión (`/auth/login`) y una ruta protegida de prueba (`/auth/protected`).
            *   **`Route_Producto.py`**: Define un `APIRouter` para las operaciones relacionadas con productos.
            *   **`Route_usuario.py`**: Define rutas para la gestión de usuarios (adicionales a la autenticación).
            *   **`Routes_Pruebas.py`**: Contiene rutas de prueba o ejemplo.
        *   **`schemas/`**: Contiene los esquemas de datos Pydantic para validación.
            *   **`Producto.py`**: Define los modelos Pydantic para la validación de datos de productos.
            *   **`Usuario.py`**: Define los modelos Pydantic para la validación de datos de usuarios (registro, login, token).
    *   **`auth.py`**: Contiene la lógica para el hashing de contraseñas (bcrypt) y la gestión de JSON Web Tokens (JWT), incluyendo la creación y verificación de tokens.
    *   **`alembic/`**: Directorio para las migraciones de base de datos con Alembic.
    *   **`alembic.ini`**: Archivo de configuración de Alembic.
    *   **`requirements.txt`**: Lista todas las dependencias de Python necesarias para el proyecto.
    *   **`README.md`**: Este archivo.
## Cómo Ejecutar el Proyecto

Sigue estos pasos para levantar el servidor FastAPI:

1.  **Navega al directorio `backend` del repositorio**:
    ```bash
    cd backend
    ```

2.  **Crea y activa un entorno virtual (recomendado)**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instala las dependencias**:
    Asegúrate de que tu entorno virtual esté activado y luego instala los paquetes listados en `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Inicia el servidor FastAPI**:
    Asegúrate de estar en el directorio `backend` y con el entorno virtual activado.
    ```bash
    uvicorn app.main:app --reload --port 8000
    ```
    *   `app.main:app`: Indica a Uvicorn que busque la instancia `app` dentro del módulo `main` que está en el paquete `app`.
    *   `--reload`: Permite que el servidor se reinicie automáticamente cuando detecta cambios en el código.
    *   `--port 8000`: Especifica que el servidor se ejecutará en el puerto 8000.
