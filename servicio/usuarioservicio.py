from repositorio.usuariorepositorio import UsuarioRepositorio

class UsuarioServicio:
    def __init__(self):
        self.repositorio = UsuarioRepositorio()

    def obtener_todos_los_usuarios(self):
        return self.repositorio.obtener_usuario()
    
    def agregar_usuario(self, nombre, contraseña):
        max_id = self.repositorio.obtener_max_id()
        new_id = max_id + 1
        self.repositorio.agregar_usuario(new_id, nombre, contraseña)

    def eliminar_usuario(self, nombre, contraseña):
        id = self.repositorio.buscar_id(nombre, contraseña)
        self.repositorio.eliminar_usuario(id)

    def modificar_usuario(self, nombre_actual, contraseña_actual, nuevo_nombre, nueva_contraseña):
        id = self.repositorio.buscar_id(nombre_actual, contraseña_actual)
        self.repositorio.modificar_usuario(id, nuevo_nombre, nueva_contraseña)