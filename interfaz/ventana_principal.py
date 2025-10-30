# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from .ventana_alumnos_ui import Ui_MainWindow

class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Configurar la ventana
        self.setWindowTitle("Sistema de Gestión de Alumnos - ITES")
        self.setWindowIcon(QtGui.QIcon())  # Puedes agregar un icono aquí
        
        # Conectar las acciones del menú
        self.ui.actionAlumnos.triggered.connect(self.abrir_gestion_alumnos)
        
        # Configurar el menú
        self.ui.menu.setTitle("Gestión")
        self.ui.actionAlumnos.setText("Gestionar Alumnos")
        
    def abrir_gestion_alumnos(self):
        """Abre la ventana de gestión de alumnos"""
        from .ventana_gestion_alumnos import VentanaGestionAlumnos
        self.ventana_alumnos = VentanaGestionAlumnos()
        self.ventana_alumnos.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
