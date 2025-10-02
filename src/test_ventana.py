import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMenu
from service.usuarioservicio import UsuarioServicio

class VentanaPrincipal(QtWidgets.QMainWindow, QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("src/test_ventana_principal.ui", self)
        self.actionSalir.triggered.connect(QtWidgets.qApp.quit)
        self.actionUsuarios.triggered.connect(self.abrir_usuarios)
        self.actionAcercade.triggered.connect(self.mostrar_acercade)
        self.actionUsuarios_2.triggered.connect(self.sobre_usuarios)

        self.servicio_usuario = UsuarioServicio()
        
        self.btnIngresar.clicked.connect(self.ingresar_usuario)
        self.btnModificar.clicked.connect(self.modificar_usuario)

        self.listar_usuarios()

        self.tlbUsuarios.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tlbUsuarios.customContextMenuRequested.connect(self.menu_contextual)

    def abrir_usuarios(self):
        VentanaPrincipal().show()

    def mostrar_acercade(self):
        QtWidgets.QMessageBox.information(self, "Acerca de", "Aplicación de Gestión de Usuarios\nDesarrollada por Luis")
    
    def sobre_usuarios(self):
        QtWidgets.QMessageBox.information(self, "Sobre Usuarios", "En este sistema puedes gestionar los usuarios.\nPuedes agregar, eliminar o modificar usuarios existentes.")

    # Menu desplegable al hacer click derecho en una de las filas de la tabla
    def menu_contextual(self, pos):
        try:
            row = self.tlbUsuarios.rowAt(pos.y())
            if row >= 0:
                nombre, contraseña = self.tlbUsuarios.item(row, 0).text(), self.tlbUsuarios.item(row, 1).text()
                menu = QMenu()
                eliminar = menu.addAction("Eliminar fila")
                modificar = menu.addAction("Modificar fila")                
                accion = menu.exec(self.tlbUsuarios.mapToGlobal(pos))
            
            if accion == modificar:
                self.nombre_actual = self.tlbUsuarios.item(row, 0).text()
                self.contraseña_actual = self.tlbUsuarios.item(row, 1).text()

                self.nombre.setText(self.nombre_actual)
                self.contrasena.setText(self.contraseña_actual)

            if accion == eliminar:
                self.tlbUsuarios.removeRow(row)
                self.servicio_usuario.eliminar_usuario(nombre, contraseña)
                self.mensaje_aviso(f"Usuario {nombre} eliminado exitosamente.")
                self.listar_usuarios()
        except Exception as e:
            self.mensaje_aviso_error(f"Error al procesar la acción del menú contextual: {e}")

    def listar_usuarios(self):
        usuarios = self.servicio_usuario.obtener_todos_los_usuarios()
        
        if not usuarios:
            self.mensaje_aviso_error("No hay usuarios registrados.")
        else:
            print("\nLista de usuarios")
            self.tlbUsuarios.setRowCount(len(usuarios))
            self.tlbUsuarios.setColumnCount(2)
            for row, usuario in enumerate(usuarios):
                self.tlbUsuarios.setItem(row, 0, QtWidgets.QTableWidgetItem(str(usuario[1])))
                self.tlbUsuarios.setItem(row, 1, QtWidgets.QTableWidgetItem(str(usuario[2])))

    def ingresar_usuario(self):
        nombre = self.nombre.text()
        contraseña = self.contrasena.text()

        if not nombre or not contraseña:
            self.mensaje_aviso_error("Por favor, complete todos los campos.")
            return
        
        self.servicio_usuario.agregar_usuario(nombre, contraseña)
        self.mensaje_aviso(f"Usuario {nombre} agregado exitosamente.")
        self.listar_usuarios()

    def modificar_usuario(self):
        try:
            nuevo_nombre = self.nombre.text()
            nuevo_contraseña = self.contrasena.text()

            if self.nombre_actual and self.contraseña_actual and nuevo_nombre and nuevo_contraseña:
                self.servicio_usuario.modificar_usuario(self.nombre_actual, self.contraseña_actual, nuevo_nombre, nuevo_contraseña)
                self.mensaje_aviso(f"Usuario {self.nombre_actual} modificado exitosamente.")
                self.listar_usuarios()
            else:
                self.mensaje_aviso_error("Modificación cancelada o datos inválidos.")
        except Exception as e:
            self.mensaje_aviso_error(f"Error al modificar el usuario: {e}")

    # Ventana de aviso con mensajes de error
    def mensaje_aviso_error(self, mensaje):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Warning)
        msg_box.setText(mensaje)
        msg_box.setWindowTitle("Aviso")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec()

    # Ventana de aviso con mensajes de información
    def mensaje_aviso(self, mensaje):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.setText(mensaje)
        msg_box.setWindowTitle("Aviso")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())