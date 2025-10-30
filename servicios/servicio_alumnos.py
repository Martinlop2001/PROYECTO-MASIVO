
from repositorio.repositorio_alumnos import RepositorioAlumnos

class ServicioAlumnos:
    def __init__(self):
        self.repositorio = RepositorioAlumnos()

    def listar_alumnos(self):
        return self.repositorio.listar_alumnos()
    
    def insertar_alumno(self, dni, nombre, apellido, correo, telefono):
        # Validaciones básicas
        if not dni or not nombre or not apellido:
            return False, "DNI, nombre y apellido son obligatorios"
        
        if not self._validar_dni(dni):
            return False, "El DNI debe contener solo números y tener entre 7 y 8 dígitos"
        
        if not self._validar_email(correo):
            return False, "El formato del correo electrónico no es válido"
        
        # Verificar si ya existe un alumno con ese DNI
        if self.repositorio.buscar_alumno_por_dni(dni):
            return False, "Ya existe un alumno con ese DNI"
        
        resultado = self.repositorio.insertar_alumno(dni, nombre, apellido, correo, telefono)
        if resultado:
            return True, "Alumno agregado exitosamente"
        else:
            return False, "Error al agregar el alumno"
    
    def modificar_alumno(self, dni, nombre, apellido, correo, telefono):
        # Validaciones básicas
        if not dni or not nombre or not apellido:
            return False, "DNI, nombre y apellido son obligatorios"
        
        if not self._validar_dni(dni):
            return False, "El DNI debe contener solo números y tener entre 7 y 8 dígitos"
        
        if not self._validar_email(correo):
            return False, "El formato del correo electrónico no es válido"
        
        # Verificar si existe el alumno
        if not self.repositorio.buscar_alumno_por_dni(dni):
            return False, "No se encontró un alumno con ese DNI"
        
        resultado = self.repositorio.modificar_alumno(dni, nombre, apellido, correo, telefono)
        if resultado:
            return True, "Alumno modificado exitosamente"
        else:
            return False, "Error al modificar el alumno"
    
    def eliminar_alumno(self, dni):
        if not dni:
            return False, "El DNI es obligatorio"
        
        if not self._validar_dni(dni):
            return False, "El DNI debe contener solo números y tener entre 7 y 8 dígitos"
        
        # Verificar si existe el alumno
        if not self.repositorio.buscar_alumno_por_dni(dni):
            return False, "No se encontró un alumno con ese DNI"
        
        resultado = self.repositorio.borrar_alumno(dni)
        if resultado:
            return True, "Alumno eliminado exitosamente"
        else:
            return False, "Error al eliminar el alumno"
    
    def buscar_alumno_por_dni(self, dni):
        if not dni or not self._validar_dni(dni):
            return None
        return self.repositorio.buscar_alumno_por_dni(dni)
    
    def _validar_dni(self, dni):
        """Valida que el DNI contenga solo números y tenga entre 7 y 8 dígitos"""
        if not dni:
            return False
        dni_str = str(dni).strip()
        return dni_str.isdigit() and 7 <= len(dni_str) <= 8
    
    def _validar_email(self, email):
        """Validación básica de email"""
        if not email:
            return True  # Email es opcional
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
