
import sqlite3

string_conexion = ".\\db\\registro.db"

class RepositorioMateria:
    def listar_materias(self) -> list[any]:
        conexion = sqlite3.connect(string_conexion)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM materias")
        materias = cursor.fetchall()
        conexion.close()
        return materias

    def agregar_materia(self, nombre: str, carrera: str, anio: int):
        conexion = sqlite3.connect(string_conexion)
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO materias (nombre, carrera, anio) VALUES (?, ?, ?)",
            (nombre, carrera, anio)
        )
        conexion.commit()
        conexion.close()

    def eliminar_materia(self, nombre):
        conexion = sqlite3.connect(string_conexion)
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM materias WHERE nombre = ?", (nombre,))
        conexion.commit()
        conexion.close()

    def modificar_materia(self, nombre_original, nuevo_nombre, nueva_carrera, nuevo_anio):
        conexion = sqlite3.connect(string_conexion)
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE materias
            SET nombre = ?, carrera = ?, anio = ?
            WHERE nombre = ?
        """, (nuevo_nombre, nueva_carrera, nuevo_anio, nombre_original))
        conexion.commit()
        conexion.close()

