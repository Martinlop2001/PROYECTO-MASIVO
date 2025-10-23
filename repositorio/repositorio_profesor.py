

import sqlite3
from db.conexion import obtener_conexion

class RepositorioProfesor:
    def listar_profesores(self):

        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM profesores ORDER BY apellido, nombre")
        profesores = cursor.fetchall()
        conexion.close()
        return profesores
    

    def buscar_profesor(self, dni):

        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM profesores WHERE dni = ?", (dni,))
        profesor = cursor.fetchone()
        conexion.close()
        return profesor
    

    def agregar_profesor(self, profesor):

        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO profesores (dni, nombre, apellido, correo, telefono)
                VALUES (?, ?, ?, ?, ?)
            """, (profesor.dni, profesor.nombre, profesor.apellido, profesor.correo, profesor.telefono))
            conexion.commit()
            conexion.close()
            return True, "Profesor agregado exitosamente"

        except sqlite3.IntegrityError as e:
            conexion.close()
            return False, "Ya existe un profesor con este DNI"
        except Exception as e:
            conexion.close()
            return False, f"Error de base de datos: {str(e)}"
    

    def actualizar_profesor(self, profesor):

        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("""
                UPDATE profesores 
                SET nombre = ?, apellido = ?, correo = ?, telefono = ?
                WHERE dni = ?
            """, (profesor.nombre, profesor.apellido, profesor.correo, profesor.telefono, profesor.dni))
            conexion.commit()
            conexion.close()
            if cursor.rowcount > 0:
                return True, "Profesor actualizado exitosamente"
            else:
                return False, "No se encontró el profesor con ese DNI"
        except Exception as e:
            conexion.close()
            return False, f"Error al actualizar profesor: {str(e)}"
    
    def eliminar_profesor(self, dni):

        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM profesores WHERE dni = ?", (dni,))
            conexion.commit()
            conexion.close()
            if cursor.rowcount > 0:
                return True, "Profesor eliminado exitosamente"
            else:
                return False, "No se encontró el profesor con ese DNI"
        except Exception as e:
            conexion.close()
            return False, f"Error al eliminar profesor: {str(e)}"