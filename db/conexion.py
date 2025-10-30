# -*- coding: utf-8 -*-

import psycopg2
from psycopg2.extras import RealDictCursor

class ConexionDB:
    """Clase para manejar la conexión a la base de datos PostgreSQL"""
    
    def __init__(self):
        self.connection_params = {
            'host': 'localhost',
            'database': 'alumnos',
            'user': 'postgres',
            'password': 'sebcheco',
            'port': '5432'
        }
    
    def get_connection(self):
        """Obtiene una nueva conexión a la base de datos"""
        return psycopg2.connect(**self.connection_params)
    
    def get_connection_with_dict_cursor(self):
        """Obtiene una conexión con cursor que retorna diccionarios"""
        conexion = psycopg2.connect(**self.connection_params)
        cursor = conexion.cursor(cursor_factory=RealDictCursor)
        return conexion, cursor
    
    def test_connection(self):
        """Prueba la conexión a la base de datos"""
        try:
            with self.get_connection() as conexion:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT 1")
                    return True
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
            return False

# Instancia global para usar en toda la aplicación
conexion_db = ConexionDB()
