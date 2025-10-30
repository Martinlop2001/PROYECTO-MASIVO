from src.db.connexion_posgreSQL import ConexionDB
class UsuarioRepositorio:
    def __init__(self):
        self.db = ConexionDB()

    def agregar_usuario(self, usuario):
        consulta = "INSERT INTO usuarios (nombre_usuario, contrasena) VALUES (%s, %s);"
        datos = (usuario.nombre, usuario.contraseña)
        self.db.ejecutar_consulta(consulta, datos)

    def obtener_usuario(self):
        consulta = "SELECT * FROM usuarios;"
        usuarios = self.db.obtencion(consulta, ())
        return usuarios

    def eliminar_usuario(self, id):
        consulta = "DELETE FROM usuarios WHERE id_usuario = %s;"
        dato = (id,)
        self.db.ejecutar_consulta(consulta, dato)
    
    def buscar_id(self, nombre, contraseña):
        consulta = "SELECT id_usuario FROM usuarios WHERE nombre_usuario = %s AND contrasena = %s;"
        datos = (nombre, contraseña)
        result = self.db.obtencion(consulta, datos)
        return result[0] if result else None
    
    def modificar_usuario(self, id, nuevo_nombre, nueva_contraseña):
        consulta = "UPDATE usuarios SET nombre_usuario = %s, contrasena = %s WHERE id_usuario = %s;"
        datos = (nuevo_nombre, nueva_contraseña, id)
        self.db.ejecutar_consulta(consulta, datos)