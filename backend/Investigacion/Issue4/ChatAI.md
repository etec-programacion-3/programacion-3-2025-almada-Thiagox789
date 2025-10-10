hola buenas como harias esto ? solo dame un paso a paso de lo qeu deberia de hacer no escribas nada de codgio. 
    Descripción: Crear la API REST completa para la gestión de productos. Esto incluye endpoints para GET (listar todos y obtener uno), POST (crear), PUT (actualizar) y DELETE (eliminar). Las operaciones de creación, actualización y eliminación deben estar protegidas, requiriendo un token JWT válido.
    Objetivo de Aprendizaje: Implementación de los principios REST, uso de parámetros de ruta y consulta, dependencias de seguridad en FastAPI y serialización de datos para las respuestas.
    Prerrequisitos: Implementación de Endpoints de Autenticación.
    Criterios de Aceptación: Se pueden listar y ver productos sin autenticación. Solo los usuarios autenticados pueden crear, modificar o eliminar productos. La API responde con los códigos de estado HTTP correctos para cada operación.
    Estimación de Esfuerzo: 3 sesiones.

**Paso 1: Configuración Inicial y Dependencias**
1.  **Verificar dependencias:** Asegurarse de que `FastAPI`, `SQLAlchemy`, `Pydantic` y `python-jose[cryptography]` (para JWT) estén instalados en el entorno `backend/requirements.txt`.
2.  **Configurar la base de datos:** Confirmar que la conexión a la base de datos (`backend/app/database/db.py`) esté correctamente establecida y que el modelo `Producto` (`backend/app/models/ORM_Producto.py`) esté mapeado.

**Paso 2: Implementación de Endpoints GET (Lectura)**
1.  **Listar todos los productos:**
    *   Modificar la función `leer_productos` en `backend/app/routes/Route_Producto.py`.
    *   Debe aceptar una dependencia para la sesión de la base de datos.
    *   Consultar todos los productos de la base de datos utilizando el modelo ORM `Producto`.
    *   Devolver una lista de objetos `Producto` (del esquema Pydantic) serializados.
    *   Asegurarse de que el código de estado HTTP sea `200 OK`.
2.  **Obtener un producto por ID:**
    *   Modificar la función `leer_productos_por_id` en `backend/app/routes/Route_Producto.py`.
    *   Debe aceptar `producto_id` como parámetro de ruta y una dependencia para la sesión de la base de datos.
    *   Consultar el producto específico por `id_producto` en la base de datos.
    *   Si el producto no se encuentra, devolver una respuesta `HTTPException` con código de estado `404 Not Found`.
    *   Si se encuentra, devolver el objeto `Producto` (del esquema Pydantic) serializado.
    *   Asegurarse de que el código de estado HTTP sea `200 OK`.

**Paso 3: Implementación de Endpoints Protegidos (Creación, Actualización, Eliminación)**
1.  **Configurar la seguridad JWT:**
    *   Importar la dependencia de seguridad JWT (`get_current_user`) desde `backend/auth.py` o `backend/app/routes/Route_Auth.py` (según donde esté definida).
    *   Esta dependencia se utilizará en los endpoints POST, PUT y DELETE para asegurar que solo los usuarios autenticados puedan acceder.
2.  **Crear un producto (POST):**
    *   Modificar la función `crear_producto` en `backend/app/routes/Route_Producto.py`.
    *   Debe aceptar un objeto `ProductoCreate` (del esquema Pydantic) como cuerpo de la solicitud.
    *   Debe aceptar una dependencia para la sesión de la base de datos y la dependencia de seguridad JWT (`current_user`).
    *   Crear una nueva instancia del modelo ORM `Producto` con los datos proporcionados.
    *   Guardar el nuevo producto en la base de datos.
    *   Devolver el producto creado (objeto `Producto` serializado) con código de estado HTTP `201 Created`.
3.  **Actualizar un producto (PUT):**
    *   Modificar la función `actualizar_producto` en `backend/app/routes/Route_Producto.py`.
    *   Debe aceptar `producto_id` como parámetro de ruta, un objeto `ProductoCreate` (o similar para actualización) como cuerpo de la solicitud.
    *   Debe aceptar una dependencia para la sesión de la base de datos y la dependencia de seguridad JWT (`current_user`).
    *   Buscar el producto por `producto_id`. Si no se encuentra, devolver `HTTPException` con `404 Not Found`.
    *   Actualizar los campos del producto encontrado con los nuevos datos.
    *   Guardar los cambios en la base de datos.
    *   Devolver el producto actualizado (objeto `Producto` serializado) con código de estado HTTP `200 OK`.
4.  **Eliminar un producto (DELETE):**
    *   Modificar la función `eliminar_producto` en `backend/app/routes/Route_Producto.py`.
    *   Debe aceptar `producto_id` como parámetro de ruta.
    *   Debe aceptar una dependencia para la sesión de la base de datos y la dependencia de seguridad JWT (`current_user`).
    *   Buscar el producto por `producto_id`. Si no se encuentra, devolver `HTTPException` con `404 Not Found`.
    *   Eliminar el producto de la base de datos.
    *   Devolver un mensaje de confirmación (o el producto eliminado) con código de estado HTTP `204 No Content` (si no se devuelve contenido) o `200 OK` (si se devuelve un mensaje).

**Paso 4: Integración y Pruebas**
1.  **Integrar rutas:** Asegurarse de que `Route_Producto.py` esté incluido en el archivo `backend/app/main.py` para que las rutas sean accesibles.
2.  **Pruebas manuales/automatizadas:**
    *   Verificar que los endpoints GET funcionen sin autenticación.
    *   Obtener un token JWT válido a través de los endpoints de autenticación existentes.
    *   Probar los endpoints POST, PUT y DELETE con el token JWT para asegurar que solo los usuarios autenticados puedan realizar estas operaciones.
    *   Verificar que los códigos de estado HTTP sean correctos en todos los escenarios (éxito, no encontrado, no autorizado, etc.).
    *   Asegurarse de que la serialización de datos sea correcta en las respuestas.

Este plan cubre los requisitos de la tarea, incluyendo la protección de rutas con JWT y el uso de los principios REST.