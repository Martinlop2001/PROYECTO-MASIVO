import sqlite3

class UsuarioRepositorio:
    def __init__(self):
        self.db_path = "src/db/db.db"

    def conectar(self):
        return sqlite3.connect(self.db_path)

    def agregar_usuario(self, usuario):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombreusuario, contraseña) VALUES (?, ?)", (usuario.nombre, usuario.contraseña))
        conn.commit()
        conn.close()

    def obtener_usuario(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        conn.close()
        return usuarios

    def eliminar_usuario(self, id):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id_usuario = ?", (id,))
        conn.commit()
        conn.close()
    
    def buscar_id(self, nombre, contraseña):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id_usuario FROM usuarios WHERE nombreusuario = ? AND contraseña = ?", (nombre, contraseña))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None
    
    def modificar_usuario(self, id, nuevo_nombre, nueva_contraseña):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET nombreusuario = ?, contraseña = ? WHERE id_usuario = ?", (nuevo_nombre, nueva_contraseña, id))
        conn.commit()
        conn.close()