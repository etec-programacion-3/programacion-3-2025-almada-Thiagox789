# Proyecto Backend con FastAPI

## Descripción del Proyecto

Este proyecto es el backend de un e-commerce dedicado a la venta de productos deportivos, llamado "MundoDeporte". Está desarrollado con FastAPI y utiliza SQLAlchemy como ORM para interactuar con una base de datos SQLite.

La estructura del proyecto está organizada para ser escalable y modular.
## Estructura del Proyecto
```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database/
│   │   ├── __init__.py
│   │   └── db.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── ORM_Producto.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── Route_Producto.py
│   └── schemas/
│       └── Producto.py
└── requirements.txt
└── README.md
```

### Explicación de Carpetas y Archivos

*   **`backend/`**: Directorio raíz del proyecto backend.
    *   **`app/`**: Contiene la lógica principal de la aplicación FastAPI.
        *   **`main.py`**: Es el punto de entrada de la aplicación FastAPI. 
        *   **`database/`**: Contiene la configuración de la base de datos.
            *   **`db.py`**: Define la conexión a la base de datos SQLite, el motor (engine) de SQLAlchemy, la clase `SessionLocal` para crear sesiones de base de datos y la `Base` declarativa para los modelos ORM.
        *   **`models/`**: Contiene las definiciones de los modelos ORM de SQLAlchemy.
            *   **`ORM_Producto.py`**: Define el modelo `productos` que se mapea a la tabla `producto` en la base de datos, especificando sus columnas y tipos de datos.
        *   **`routes/`**: Contiene los módulos que definen las rutas (endpoints) de la API.
            *   **`Route_Producto.py`**: Define un `APIRouter` para las operaciones relacionadas con productos, incluyendo un endpoint de prueba.
        *   **`schemas/`**: Contiene los esquemas de datos Pydantic.
            *   **`Producto.py`**: Define los modelos Pydantic para la validación de datos de entrada y salida de los endpoints de productos.
    *   **`requirements.txt`**: Lista todas las dependencias de Python necesarias para el proyecto (FastAPI, Uvicorn, SQLAlchemy, Pydantic).
    *   **`README.md`**: Este archivo, que describe el proyecto.
## Cómo Ejecutar el Proyecto

Sigue estos pasos para levantar el servidor FastAPI:

1.  **Navega al directorio backend del repositorio**:
  
2.  **Crea y activa un entorno virtual**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instala las dependencias**:
    Asegúrate de que tu entorno virtual esté activado y luego instala los paquetes listados en `requirements.txt`.
    ```bash
    ```

4.  **Inicia el servidor FastAPI**:
    Asegúrate de estar en el directorio raíz del proyecto y con el entorno virtual activado.
    ```bash
    uvicorn backend.app.main:app --reload --port 8000
    ```
    *   `backend.app.main:app`: Indica a Uvicorn que busque la instancia `app` dentro del módulo `main` que está en el paquete `app` dentro de `backend`.
    *   `--reload`: Permite que el servidor se reinicie automáticamente cuando detecta cambios en el código.
    *   `--port 8000`: Especifica que el servidor se ejecutará en el puerto 8000.

5.  **Verificar el endpoint de prueba**:
    Una vez que el servidor esté en funcionamiento, puedes abrir tu navegador y visitar `http://localhost:8000/prueba/`
    Deberías ver una respuesta JSON similar a: `{"mensaje": "Servidor funcionando y ruta de productos OK"}`.
