import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMenu
from servicio.usuarioservicio import UsuarioServicio

class Ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana_principal.ui", self)
        self.actionSalir.triggered.connect(QtWidgets.qApp.quit)
        self.actionUsuarios.triggered.connect(self.abrir_usuarios)

    def abrir_usuarios(self):
        self.ventana_usuarios = VentanaUsuarios()
        self.ventana_usuarios.show()

class VentanaUsuarios(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("usuarios.ui", self)
        self.servicio_usuario = UsuarioServicio()
        
        self.btnCerrar.clicked.connect(self.close)
        self.btnIngresar.clicked.connect(self.ingresar_usuario)
        self.btnEliminar.clicked.connect(self.eliminar_usuario)

        self.listar_usuarios()

        self.tlbUsuarios.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tlbUsuarios.customContextMenuRequested.connect(self.menu_contextual)

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
                self.modificar_usuario(row)

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
        contraseña = self.contraseña.text()

        if not nombre or not contraseña:
            self.mensaje_aviso_error("Por favor, complete todos los campos.")
            return
        
        self.servicio_usuario.agregar_usuario(nombre, contraseña)
        self.mensaje_aviso(f"Usuario {nombre} agregado exitosamente.")
        self.listar_usuarios()

    def eliminar_usuario(self):
        fila_seleccionada = self.tlbUsuarios.currentRow()
        if fila_seleccionada < 0:
            self.mensaje_aviso_error("Por favor, seleccione un usuario para eliminar.")
            return

        nombre_usuario, contraseña = self.tlbUsuarios.item(fila_seleccionada, 0).text(), self.tlbUsuarios.item(fila_seleccionada, 1).text()
        self.servicio_usuario.eliminar_usuario(nombre_usuario, contraseña)
        self.mensaje_aviso(f"Usuario {nombre_usuario} eliminado exitosamente.")
        self.listar_usuarios()

    def modificar_usuario(self, row):
        try:
            nombre_actual = self.tlbUsuarios.item(row, 0).text()
            contraseña_actual = self.tlbUsuarios.item(row, 1).text()

            nuevo_nombre, ok1 = QtWidgets.QInputDialog.getText(self, "Modificar Usuario", "Nuevo nombre:", text=nombre_actual)
            nuevo_contraseña, ok2 = QtWidgets.QInputDialog.getText(self, "Modificar Usuario", "Nueva contraseña:", text=contraseña_actual)

            if ok1 and ok2 and nuevo_nombre and nuevo_contraseña:
                self.servicio_usuario.modificar_usuario(nombre_actual, contraseña_actual, nuevo_nombre, nuevo_contraseña)
                self.mensaje_aviso(f"Usuario {nombre_actual} modificado exitosamente.")
                self.listar_usuarios()
            else:
                self.mensaje_aviso_error("Modificación cancelada o datos inválidos.")
        except Exception as e:
            self.mensaje_aviso_error(f"Error al modificar el usuario: {e}")

    def mensaje_aviso_error(self, mensaje):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Warning)
        msg_box.setText(mensaje)
        msg_box.setWindowTitle("Aviso")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec()
    
    def mensaje_aviso(self, mensaje):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.setText(mensaje)
        msg_box.setWindowTitle("Aviso")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())