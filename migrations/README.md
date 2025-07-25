# Migraciones de Base de Datos

Este directorio contiene scripts de migración SQL para resolver problemas conocidos en la base de datos.

## Scripts Disponibles

### fix_provider_sequence.sql

**Propósito:** Corrige el desalineamiento de la secuencia de auto-incremento en la tabla `provider`.

**Problema que resuelve:** Error `duplicate key value violates unique constraint "provider_pkey"` al crear nuevos proveedores.

**Cuándo usar:** 
- Después de insertar datos manualmente en la tabla `provider`
- Al migrar datos desde otra base de datos
- Cuando se produce el error de clave duplicada al crear proveedores

**Cómo ejecutar:**
```bash
# Opción 1: Usando psql
psql -d your_database_name -f migrations/fix_provider_sequence.sql

# Opción 2: Desde un cliente PostgreSQL
\i migrations/fix_provider_sequence.sql

# Opción 3: Ejecutar directamente el comando SQL
SELECT setval(pg_get_serial_sequence('provider', 'id'), MAX(id)) FROM provider;
```

**Validación:** Después de ejecutar el script, verifica que el próximo ID será correcto:
```sql
SELECT nextval('provider_id_seq');
```

## Notas Importantes

- Siempre haz una copia de seguridad de tu base de datos antes de ejecutar migraciones
- Estos scripts están diseñados para PostgreSQL
- Ejecuta las migraciones en orden si hay múltiples archivos
- Documenta cualquier migración personalizada que agregues

## Aplicabilidad

Estos scripts deben aplicarse tanto en las ramas `main` como `develop` para mantener consistencia entre entornos.