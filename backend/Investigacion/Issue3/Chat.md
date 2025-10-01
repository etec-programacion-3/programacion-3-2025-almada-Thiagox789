# Pasos para construir los endpoints de registro y login con autenticación JWT

## Propmt:
Ddecime paso a paso de lo que tendria que hacer para realizar esta issue. No lo resolvas solo dame paso a paso para hacerla yo mismo. 
    Descripción: Construir los endpoints de la API para el registro (/register) y el inicio de sesión (/login). La autenticación se gestionará mediante JSON Web Tokens (JWT). Se debe asegurar que las contraseñas se almacenen de forma segura utilizando una función de hashing (ej: bcrypt).
    Objetivo de Aprendizaje: Creación de endpoints POST, validación de datos de entrada con Pydantic, hashing de contraseñas, y generación y validación de tokens JWT para la gestión de sesiones.
    Prerrequisitos: Modelado de Datos.
    Criterios de Aceptación: Un usuario puede registrarse a través de la API. Un usuario registrado puede hacer login y recibir un token de acceso. El token puede ser utilizado para acceder a un endpoint protegido de prueba.
    Estimación de Esfuerzo: 3 sesiones.

Claro, aquí tienes los pasos detallados para implementar los endpoints de registro y login con autenticación JWT en FastAPI:

## Pasos detallados:

1. **Instalar dependencias necesarias**  
   Instala fastapi, uvicorn, bcrypt, y pyjwt para JWT:

2. **Crear el esquema Pydantic para usuario y login**  
   Define modelos en `/schemas/Usuario.py` para validar los datos de entrada (registro y login).

3. **Implementar el hashing de contraseñas**  
   En /app/models/ORM_User.py o en un archivo utilitario, crea funciones para:
 - Hashear contraseñas con bcrypt.
 - Verificar contraseñas.


4. **Crear funciones para generar y verificar JWT**  
   Usa python-jose para Crea funciones para:
   - Generar tokens JWT.
   - Verificar tokens JWT.
   - Puedes hacerlo en un archivo utilitario, por ejemplo, /app/utils/jwt.py..

5. **Crear el endpoint /register**  
   En `/routes/Route_usuario.py`, crea un endpoint POST que:  
   - Reciba los datos del usuario.  
   - Valide los datos con Pydantic.  
   - Hashee la contraseña.  
   - Guarde el usuario en la base de datos.

6. **Crear el endpoint /login**  
   En `/routes/Route_usuario.py`, crea un endpoint POST que:  
   - Reciba email y contraseña.  
   - Verifique que el usuario existe y la contraseña es correcta.  
   - Genere y devuelva un JWT si la autenticación es exitosa.
7. **Crear un endpoint protegido de prueba**  
   En /app/routes/Route_usuario.py:
    - Crea un endpoint (ejemplo: /protected) que requiera el JWT en el header para acceder.
8. **Probar los endpoints**  
   Usa curl, httpie o Postman para probar:
   - Registro.
   - Login.
   - Acceso al endpoint protegido usando el token.
9. **Documentar y limpiar el código**  
   Agrega comentarios y asegúrate de que el código sea claro y seguro.

