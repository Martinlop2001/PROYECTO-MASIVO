



import sqlite3


class RepositorioProfesor:
    def listar_profesores(self) -> list[any]:
        conexion = sqlite3.connect(".\\db\\profesores.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM profesores")
        profesores = cursor.fetchall()
        return profesores
    