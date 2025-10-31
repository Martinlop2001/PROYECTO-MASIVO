from PyQt5 import QtWidgets, uic
from ventanas.ventana_usuarios import VentanaUsuarios

class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("xml/ventana_principal.ui", self)
        self.actionSalir.triggered.connect(QtWidgets.qApp.quit)
        self.actionUsuarios.triggered.connect(self.abrir_usuarios)
        self.actionAcercade.triggered.connect(self.mostrar_acercade)
        self.actionUsuarios_2.triggered.connect(self.sobre_usuarios)

    def abrir_usuarios(self):
        self.ventana_usuarios = VentanaUsuarios()
        self.ventana_usuarios.show()

    def mostrar_acercade(self):
        QtWidgets.QMessageBox.information(self, "Acerca de", "Aplicación de Gestión de Usuarios\nDesarrollada por Luis")
    
    def sobre_usuarios(self):
        QtWidgets.QMessageBox.information(self, "Sobre Usuarios", "En este sistema puedes gestionar los usuarios.\nPuedes agregar, eliminar o modificar usuarios existentes.")