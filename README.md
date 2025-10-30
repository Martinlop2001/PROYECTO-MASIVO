# Sistema de Gestión de Alumnos

Sistema desarrollado en Python con PyQt5 para la gestión de alumnos, utilizando PostgreSQL como base de datos.

## Características

- ✅ Interfaz gráfica moderna con PyQt5
- ✅ Conexión a base de datos PostgreSQL
- ✅ Operaciones CRUD completas (Crear, Leer, Actualizar, Eliminar)
- ✅ Validaciones de datos
- ✅ Interfaz intuitiva y fácil de usar

## Requisitos del Sistema

### Software Necesario
- Python 3.7 o superior
- PostgreSQL 12 o superior
- pip (gestor de paquetes de Python)

### Dependencias Python
- PyQt5
- psycopg2-binary

## Instalación

### 1. Clonar o descargar el proyecto
```bash
git clone <url-del-repositorio>
cd proyecto_progamacion
```

### 2. Instalar dependencias de Python
```bash
pip install -r requirements.txt
```

### 3. Configurar PostgreSQL

#### Crear la base de datos:
```sql
CREATE DATABASE alumnos;
```

#### Crear el usuario y asignar permisos:
```sql
CREATE USER postgres WITH PASSWORD 'sebcheco';
GRANT ALL PRIVILEGES ON DATABASE alumnos TO postgres;
```

#### Ejecutar el script de creación de tablas:
```bash
psql -U postgres -d alumnos -f db/schema_postgresql.sql
```

### 4. Configurar la conexión a la base de datos

Los parámetros de conexión están configurados en `repositorio/repositorio_alumnos.py`:

```python
self.connection_params = {
    'host': 'localhost',
    'database': 'alumnos',
    'user': 'postgres',
    'password': 'sebcheco',
    'port': '5432'
}
```

Si necesitas cambiar estos parámetros, modifica el archivo mencionado.

## Uso

### Ejecutar la aplicación
```bash
python main.py
```

### Funcionalidades

1. **Ventana Principal**: Muestra el menú principal con opción "Alumnos"
2. **Gestión de Alumnos**: Al hacer clic en "Alumnos" se abre la ventana de gestión
3. **Lista de Alumnos**: Se muestran todos los alumnos en una tabla
4. **Agregar Alumno**: Completa el formulario y haz clic en "Agregar"
5. **Modificar Alumno**: Selecciona un alumno de la tabla, modifica los datos y haz clic en "Modificar"
6. **Eliminar Alumno**: Selecciona un alumno y haz clic en "Eliminar"
7. **Actualizar Lista**: Haz clic en "Actualizar Lista" para refrescar los datos

### Validaciones

- **DNI**: Debe contener solo números y tener entre 7 y 8 dígitos
- **Nombre y Apellido**: Campos obligatorios
- **Correo**: Formato de email válido (opcional)
- **Teléfono**: Campo opcional

## Estructura del Proyecto

```
proyecto_progamacion/
├── main.py                          # Archivo principal
├── requirements.txt                 # Dependencias
├── README.md                       # Este archivo
├── alumnos.py                      # Modelo de datos
├── db/
│   ├── schema_postgresql.sql       # Script de creación de tablas
│   └── conexion.py                 # Configuración de conexión (legacy)
├── interfaz/
│   ├── ventana_principal.py        # Ventana principal
│   ├── ventana_gestion_alumnos.py  # Ventana de gestión de alumnos
│   ├── ventana_alumnos_ui.py       # UI generada por Qt Designer
│   └── ventana_alumnos.ui          # Archivo de diseño Qt
├── repositorio/
│   └── repositorio_alumnos.py      # Capa de acceso a datos
└── servicios/
    └── servicio_alumnos.py         # Lógica de negocio
```

## Solución de Problemas

### Error de conexión a PostgreSQL
- Verifica que PostgreSQL esté ejecutándose
- Confirma que los parámetros de conexión sean correctos
- Asegúrate de que la base de datos 'alumnos' existe

### Error de importación de módulos
- Ejecuta `pip install -r requirements.txt`
- Verifica que estés en el directorio correcto del proyecto

### Error de permisos de base de datos
- Verifica que el usuario 'postgres' tenga permisos en la base de datos
- Ejecuta el script SQL para crear las tablas

## Contribuciones

Para contribuir al proyecto:
1. Fork el repositorio
2. Crea una rama para tu feature
3. Realiza los cambios
4. Envía un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.
