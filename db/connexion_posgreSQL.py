import psycopg2

class ConexionDB:
    def __init__(self):
        self.connection = self.connect_to_db()
        self.inicializar_base_datos()

    def connect_to_db(self):
        connection = psycopg2.connect(
            user="postgres",
            password="123456",
            host="localhost",
                database="ITES"
            )
        return connection
    
    def ejecutar_consulta(self, consulta, datos):
        try:
            cursor = self.connection.cursor()
            cursor.execute(consulta, datos)
            self.connection.commit()
            return True
        except Exception as ex:
            print(ex)
            print("Error en la consulta")
            return False
        
    def obtencion(self, consulta, dato):
        try:
            cursor = self.connection.cursor()
            cursor.execute(consulta, dato)
            muestra = cursor.fetchall()
            self.connection.commit()
            return muestra
        except Exception as ex:
            print(ex)
            return None
        
    def inicializar_base_datos(self):

        cursor = self.connection.cursor()

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

        # Crear tabla de usuarios
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS usuarios (
                id_usuario uuid PRIMARY KEY,
                nombre_usuario VARCHAR(100) NOT NULL,
                contrasena VARCHAR(100) NOT NULL
            )
            """
        )

        self.connection.commit()
        cursor.close()
        self.connection.close()

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Conexion terminada")