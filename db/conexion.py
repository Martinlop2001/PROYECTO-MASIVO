
import sqlite3


def obtener_conexion():

    conexion = sqlite3.connect("db/profesores.db")
    return conexion

def inicializar_base_datos():

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    # Crear tabla de profesores si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS profesores (
            dni TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            correo TEXT NOT NULL,
            telefono TEXT NOT NULL
        )
    """)
    
    conexion.commit()
    conexion.close()


inicializar_base_datos()
