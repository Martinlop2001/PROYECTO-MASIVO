



import psycopg2



def obtener_conexion():

    conexion = psycopg2.connect(
        host=("localhost"),
        port=("5432"),
        user=("postgres"),
        password=("3239"),
        dbname=("db")
    )
    return conexion

def inicializar_base_datos():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    # Crear tabla de profesores
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS profesores (
            dni VARCHAR(16) PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,
            apellido VARCHAR(255) NOT NULL,
            correo VARCHAR(255) NOT NULL,
            telefono VARCHAR(50) NOT NULL
        )
        """
    )
    
    # Crear tabla de alumnos
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS alumnos (
            nombre VARCHAR(255) PRIMARY KEY,
            carrera VARCHAR(255) NOT NULL,
            anio VARCHAR(10) NOT NULL
        )
        """
    )
    
    # Crear tabla de materias
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS materias (
            nombre VARCHAR(255) PRIMARY KEY,
            carrera VARCHAR(255) NOT NULL,
            anio VARCHAR(10) NOT NULL
        )
        """
    )
    
    conexion.commit()
    cursor.close()
    conexion.close()


inicializar_base_datos()
