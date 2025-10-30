
from db.conexion import conexion_db

class RepositorioAlumnos:
    def __init__(self):
        self.conexion_db = conexion_db

    def listar_alumnos(self):
        try:
            conexion, cursor = self.conexion_db.get_connection_with_dict_cursor()
            try:
                cursor.execute("SELECT * FROM alumno ORDER BY apellido, nombre")
                alumnos = cursor.fetchall()
                return [dict(alumno) for alumno in alumnos]
            finally:
                cursor.close()
                conexion.close()
        except Exception as e:
            print(f"Error al listar alumnos: {e}")
            return []

    def insertar_alumno(self, dni, nombre, apellido, correo, telefono):
        try:
            conexion = self.conexion_db.get_connection()
            try:
                with conexion.cursor() as cursor:
                    cursor.execute("""
                        INSERT INTO alumno (dni, nombre, apellido, correo, telefono)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (dni, nombre, apellido, correo, telefono))
                    conexion.commit()
                    print(f"Alumno {nombre} {apellido} insertado correctamente.")
                    return True
            finally:
                conexion.close()
        except Exception as e:
            print(f"Error al insertar alumno: {e}")
            return False

    def borrar_alumno(self, dni):
        try:
            conexion = self.conexion_db.get_connection()
            try:
                with conexion.cursor() as cursor:
                    cursor.execute("DELETE FROM alumno WHERE dni = %s", (dni,))
                    conexion.commit()
                    if cursor.rowcount > 0:
                        print(f"Alumno con DNI {dni} ha sido eliminado.")
                        return True
                    else:
                        print(f"No se encontró alumno con DNI {dni}")
                        return False
            finally:
                conexion.close()
        except Exception as e:
            print(f"Error al eliminar alumno: {e}")
            return False

    def modificar_alumno(self, dni, nombre, apellido, correo, telefono):
        try:
            conexion = self.conexion_db.get_connection()
            try:
                with conexion.cursor() as cursor:
                    cursor.execute("""
                        UPDATE alumno
                        SET nombre = %s, apellido = %s, correo = %s, telefono = %s
                        WHERE dni = %s
                    """, (nombre, apellido, correo, telefono, dni))
                    conexion.commit()
                    if cursor.rowcount > 0:
                        print(f"Alumno con DNI {dni} ha sido actualizado.")
                        return True
                    else:
                        print(f"No se encontró alumno con DNI {dni}")
                        return False
            finally:
                conexion.close()
        except Exception as e:
            print(f"Error al modificar alumno: {e}")
            return False

    def buscar_alumno_por_dni(self, dni):
        try:
            conexion, cursor = self.conexion_db.get_connection_with_dict_cursor()
            try:
                cursor.execute("SELECT * FROM alumno WHERE dni = %s", (dni,))
                alumno = cursor.fetchone()
                return dict(alumno) if alumno else None
            finally:
                cursor.close()
                conexion.close()
        except Exception as e:
            print(f"Error al buscar alumno: {e}")
            return None
