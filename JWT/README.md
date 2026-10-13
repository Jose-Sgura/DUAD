# Fruit Store API

API REST hecha con **Flask** para una tienda de frutas, con autenticación **JWT (RS256)**, roles (`admin` / `user`), productos, compras con facturas, agenda de contactos e historial de inicios de sesión.

- Base de datos: PostgreSQL, accedida con **SQLAlchemy Core** (sin SQL crudo).
- Contraseñas guardadas con **argon2**.
- Access token de 15 minutos y refresh token de 7 días.

## Requisitos

- Python 3.10 o superior
- PostgreSQL en ejecución

## Puesta en marcha

1. **Instalar dependencias** (opcionalmente dentro de un entorno virtual):

   ```
   python -m venv venv
   venv\Scripts\activate        # en Linux/Mac: source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configurar la base de datos.** Crea un archivo `.env` en esta carpeta con la cadena de conexión:

   ```
   DATABASE_URL=postgresql+psycopg2://usuario:contrasena@localhost:5432/postgres
   ```

   Si no existe `DATABASE_URL`, se usa el valor por defecto que aparece en `db.py`. Evita caracteres especiales (como la ñ) en la contraseña de la base de datos.

3. **Generar las llaves JWT.** Las llaves **no** están en el repositorio (por seguridad, la llave privada no se sube a Git), así que hay que crearlas:

   ```
   python generate_keys.py
   ```

   Esto crea `keys/private.pem` y `keys/public.pem`.

4. **Iniciar el servidor:**

   ```
   python app.py
   ```

   Al arrancar se crean automáticamente las tablas que falten (`users`, `products`, `invoices`, `invoice_items`, `contacts`, `login_history`).

## Autenticación

- `POST /register` y `POST /login` devuelven `token` (access, 15 min) y `refresh_token` (7 días).
- Los endpoints protegidos reciben el access token en el header: `Authorization: Bearer <token>`.
- Cuando el access token expira, se pide uno nuevo con `POST /refresh-token` enviando `{"refresh_token": "..."}`.
- Un refresh token **no** sirve para acceder a los endpoints; solo para renovar.
- El primer admin se puede crear sin token. Después, solo un admin autenticado puede crear otro admin.

Códigos de error: `401` si no hay token o es inválido/expirado, `403` si el usuario no tiene permiso para esa acción.

## Endpoints

| Método | Ruta | Acceso | Descripción |
|---|---|---|---|
| GET | `/liveness` | público | Comprobar que el servidor responde |
| POST | `/register` | público* | Crear usuario (`username`, `password`, `role` opcional) |
| POST | `/login` | público | Iniciar sesión |
| POST | `/refresh-token` | refresh token | Obtener un access token nuevo |
| GET | `/me` | autenticado | Datos del usuario actual |
| GET | `/login-history` | admin | Historial de inicios de sesión (`?user_id=` o `?username=` opcionales) |
| POST, GET | `/products` | admin | Crear / listar productos |
| GET, PUT, DELETE | `/products/<id>` | admin | Ver / editar / borrar un producto |
| POST | `/purchase` | admin, user | Comprar productos (genera factura) |
| GET | `/invoices` | admin, user | Facturas del usuario actual |
| POST, GET | `/contacts` | admin, user | Crear contacto / listar contactos |
| GET, PUT, DELETE | `/contacts/<id>` | admin, user | Ver / editar / borrar un contacto |

\* Crear un usuario con `"role": "admin"` exige token de admin si ya existe uno.

### Reglas de la agenda de contactos

- **user**: solo ve y gestiona sus propios contactos (si pide el de otro, recibe 404).
- **admin**: ve los contactos de todos y puede eliminar cualquiera; solo crea y edita los suyos.

### Historial de inicios de sesión

Cada intento en `/login` se guarda con usuario, fecha/hora, IP y si fue exitoso o fallido, incluso cuando el usuario no existe.

## Ejemplo rápido

```
POST /register
{"username": "admin", "password": "mi_clave", "role": "admin"}

POST /login
{"username": "admin", "password": "mi_clave"}

GET /me
Authorization: Bearer <token>

POST /refresh-token
{"refresh_token": "<refresh_token>"}
```

## Estructura

| Archivo | Contenido |
|---|---|
| `app.py` | Rutas de la API |
| `auth.py` | Validación del token y decorador `login_required` |
| `db.py` | Tablas y `DBManager` (acceso a la base de datos) |
| `JWT_Manager.py` | `JWTManager` para crear y verificar tokens |
| `generate_keys.py` | Genera el par de llaves RSA |
