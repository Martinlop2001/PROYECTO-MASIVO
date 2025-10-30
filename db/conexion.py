
import os
import psycopg2
from psycopg2 import sql


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
    
    conexion.commit()
    cursor.close()
    conexion.close()


inicializar_base_datos()
