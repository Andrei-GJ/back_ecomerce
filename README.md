# back_ecomerce

Este proyecto es el backend para una aplicación de comercio electrónico, desarrollado en Python.

## Descripción

El propósito de este repositorio es gestionar la lógica de negocio y el acceso a datos de una plataforma de e-commerce. Incluye manejo de productos, usuarios, órdenes, autenticación, y más.

## Características principales

- Gestión de usuarios (registro, login, roles)
- CRUD de productos
- Gestión de órdenes y pagos
- Autenticación y autorización
- Integración con bases de datos relacionales/no relacionales
- API RESTful

## Tecnologías utilizadas

- Python 3.x
- FastAPI (Framework web)
- PostgreSQL (Base de datos)
- Bibliotecas principales:
  - SQLAlchemy (ORM)
  - python-dotenv (Manejo de variables de entorno)
  - uvicorn (Servidor ASGI)
  - python-multipart (Manejo de formularios)
  - psycopg2-binary (Conector PostgreSQL)

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Andrei-GJ/back_ecomerce.git
   ```
2. Accede al directorio del proyecto:
   ```bash
   cd back_ecomerce
   ```
3. Crea y activa un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Configura las variables de entorno necesarias (base de datos, claves secretas, etc.).
2. Inicializa la base de datos (si aplica).
3. Ejecuta el servidor de desarrollo:
   ```bash
   python main.py  # O el archivo principal de tu framework
   ```

## Solución de problemas comunes

### Error de clave duplicada en proveedores

Si experimentas el error `duplicate key value violates unique constraint "provider_pkey"` al crear nuevos proveedores, esto indica que la secuencia de auto-incremento de la tabla `provider` está desalineada.

**Síntomas:**
- Error al hacer POST a `/create_provider`
- Mensaje: `duplicate key value violates unique constraint "provider_pkey"`

**Solución:**
Ejecuta el siguiente script SQL en tu base de datos PostgreSQL para realinear la secuencia:

```sql
SELECT setval(pg_get_serial_sequence('provider', 'id'), MAX(id)) FROM provider;
```

**Usando el script de migración:**
```bash
psql -d your_database_name -f migrations/fix_provider_sequence.sql
```

**Explicación:**
Este comando ajusta la secuencia `provider_id_seq` para continuar desde el valor máximo actual en la tabla, evitando conflictos con IDs existentes.

**Prevención:**
- Evita insertar registros con IDs específicos en producción
- Usa siempre las operaciones de la API para crear nuevos registros
- Aplica este script después de importar datos manualmente

## Endpoints principales

- `/api/products` — Gestión de productos
- `/api/users` — Gestión de usuarios
- `/api/orders` — Gestión de órdenes

(Agrega aquí una tabla o lista de endpoints si lo deseas)

## Contribuciones

¡Las contribuciones son bienvenidas! Por favor abre un issue o pull request para sugerencias, errores o mejoras.

## Licencia

Este proyecto está bajo la Licencia MIT.

---

Desarrollado por [Andrei-GJ](https://github.com/Andrei-GJ)