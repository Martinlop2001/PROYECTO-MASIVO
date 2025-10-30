import psycopg2

class ConexionDB:
    def __init__(self):
        self.connection = self.connect_to_db()

    def connect_to_db(self):
        connection = psycopg2.connect(
            user="postgres",
            password="123456",
            host="localhost",
                database="ITES"
            )
        return connection
    
    def ejecutar_consulta(self, consulta, datos):
        print("Conexion exitosa")
        try:
            print("Paso db#1")
            cursor = self.connection.cursor()
            cursor.execute(consulta, datos)
            self.connection.commit()
            print("Paso db#2")
        except Exception as ex:
            print(ex)
            print("Error en la consulta")
            return None
        
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

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Conexion terminada")