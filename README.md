# Aplicación de E-commerce Mundo Deporte

Este repositorio contiene una aplicación de e-commerce full-stack llamada "Mundo Deporte", desarrollada como un proyecto para Programación 3 - 2025. La aplicación cuenta con un catálogo de productos, autenticación de usuarios, un carrito de compras y una simulación de pago con gestión de stock.

## Tabla de Contenidos

- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Configuración e Instalación](#configuración-e-instalación)
  - [Configuración del Backend](#configuración-del-backend)
  - [Configuración del Frontend](#configuración-del-frontend)
- [Ejecutando la Aplicación](#ejecutando-la-aplicación)
- [Endpoints de la API](#endpoints-de-la-api)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Características

- **Autenticación de Usuarios:** Funcionalidad de registro, inicio y cierre de sesión.
- **Catálogo de Productos:** Navegar y ver detalles de varios productos.
- **Carrito de Compras:** Añadir, eliminar y actualizar cantidades de productos en el carrito.
- **Gestión de Stock:** Las cantidades de los productos se actualizan después de una compra exitosa.
- **Simulación de Pago:** Un paso de confirmación antes de finalizar una compra.
- **Diseño Responsivo:** Una interfaz de usuario moderna y limpia.

## Tecnologías Utilizadas

### Frontend
- **React:** Una biblioteca de JavaScript para construir interfaces de usuario.
- **Vite:** Una herramienta de construcción rápida para proyectos web modernos.
- **React Router DOM:** Para enrutamiento declarativo en aplicaciones React.
- **Axios:** Para realizar peticiones HTTP.
- **CSS:** Para estilizar la aplicación.

### Backend
- **FastAPI:** Un framework web moderno y rápido (de alto rendimiento) para construir APIs con Python 3.7+ basado en las anotaciones de tipo estándar de Python.
- **SQLAlchemy:** Un kit de herramientas SQL y Mapeador Objeto-Relacional (ORM) que brinda a los desarrolladores de aplicaciones todo el poder y la flexibilidad de SQL.
- **SQLite:** Una biblioteca en lenguaje C que implementa un motor de base de datos SQL pequeño, rápido, autónomo, de alta fiabilidad y con todas las funciones.
- **Uvicorn:** Un servidor ASGI para Python.
- **Alembic:** Una herramienta de migración de bases de datos para SQLAlchemy.
- **PyJWT:** Para la implementación de JSON Web Token (JWT) para autenticación.
- **Passlib:** Para el hashing de contraseñas.

## Estructura del Proyecto

El proyecto se divide en dos partes principales: `backend` y `frontend`.

```
.
├── backend/
│   ├── alembic/                  # Migraciones de la base de datos
│   ├── app/                      # Aplicación FastAPI
│   │   ├── database/             # Conexión y modelos de la base de datos
│   │   ├── models/               # Modelos ORM de SQLAlchemy
│   │   ├── routes/               # Endpoints de la API
│   │   └── schemas/              # Esquemas Pydantic para validación de datos
│   ├── auth.py                   # Lógica de autenticación
│   ├── requirements.txt          # Dependencias de Python del backend
│   └── README.md                 # Documentación específica del backend
├── frontend/
│   ├── public/                   # Archivos estáticos
│   ├── src/                      # Código fuente de la aplicación React
│   │   ├── assets/               # Imágenes y otros recursos
│   │   ├── components/           # Componentes de React reutilizables
│   │   ├── context/              # Context de React para gestión de estado
│   │   ├── App.css               # Estilos globales
│   │   ├── App.jsx               # Componente principal de la aplicación
│   │   ├── index.css             # CSS base
│   │   └── main.jsx              # Punto de entrada de la aplicación React
│   ├── package.json              # Dependencias de Node.js del frontend
│   └── README.md                 # Documentación específica del frontend
└── README.md                     # README principal del proyecto
```

## Configuración e Instalación

Sigue estos pasos para tener el proyecto funcionando en tu máquina local.

### Configuración del Entorno

Antes de ejecutar la aplicación, necesitas configurar las variables de entorno tanto para el backend como para el frontend.

**Para el backend:**

1.  Navega al directorio `backend`.
2.  Crea un nuevo archivo llamado `.env` copiando el archivo de ejemplo:
    ```bash
    cp .env.example .env
    ```
3.  Abre el archivo `.env` y actualiza las variables según sea necesario. El contenido debería ser similar a esto:
    ```
    # Configuración del Backend
    DATABASE_URL="sqlite:///./app/database/mundodeporte.db"
    SECRET_KEY="tu_clave_super_secreta_aqui"
    ```
    -   `DATABASE_URL`: La cadena de conexión para tu base de datos. El valor por defecto está configurado para SQLite.
    -   `SECRET_KEY`: Una clave secreta para la generación de tokens JWT. Se recomienda usar una cadena larga y aleatoria.

**Para el frontend:**

1.  Navega al directorio `frontend`.
2.  Crea un nuevo archivo llamado `.env` copiando el archivo de ejemplo:
    ```bash
    cp .env.example .env
    ```
3.  El archivo `.env` debe contener la URL de tu API de backend:
    ```
    # Configuración del Frontend
    VITE_API_URL=http://localhost:8000
    ```
    -   `VITE_API_URL`: La URL de la API del backend. El valor por defecto es `http://localhost:8000`.

### Configuración del Backend

1.  **Navega al directorio del backend:**
    ```bash
    cd backend
    ```

2.  **Crea un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    ```

3.  **Activa el entorno virtual:**
    -
        ```bash
        source venv/bin/activate
        ```

4.  **Instala las dependencias del backend:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Ejecuta las migraciones de la base de datos:**
    ```bash
    alembic upgrade head
    ```

6.  **Inicia el servidor del backend:**
    ```bash
    uvicorn app.main:app --reload --port 8000
    ```
    La API del backend estará disponible en `http://localhost:8000`.

### Configuración del Frontend

1.  **Navega al directorio del frontend:**
    ```bash
    cd frontend
    ```

2.  **Instala las dependencias del frontend:**
    ```bash
    npm install
    ```

3.  **Inicia el servidor de desarrollo del frontend:**
    ```bash
    npm run dev
    ```
    La aplicación del frontend estará disponible en `http://localhost:5173` (u otro puerto si el 5173 está en uso).

## Ejecutando la Aplicación

1.  Asegúrate de que tanto el servidor del backend como el del frontend estén funcionando en instancias de terminal separadas.
2.  Abre tu navegador web y navega a la URL del frontend (ej., `http://localhost:5173`).

## Endpoints de la API

El backend proporciona los siguientes endpoints principales de la API:

-   `/auth/register`: Registrar un nuevo usuario.
-   `/auth/login`: Autenticar un usuario y obtener un token JWT.
-   `/products/`: Obtener todos los productos (soporta filtrado por `min_price` y `max_price`).
-   `/products/{product_id}`: Obtener un solo producto por ID.
-   `/products/`: Crear un nuevo producto (requiere autenticación).
-   `/products/{product_id}`: Actualizar un producto existente (requiere autenticación).
-   `/products/{product_id}/stock`: Actualizar el stock de un producto (usado después de la compra).
-   `/products/{product_id}`: Eliminar un producto (requiere autenticación).

## Contribuciones

Siéntete libre de hacer un fork de este repositorio, abrir issues y enviar pull requests.

## Licencia

Este proyecto está bajo la Licencia MIT.
