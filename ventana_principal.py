


import sys
from PyQt5 import QtWidgets, uic
from profesores import Profesor
import sqlite3
from db.conexion import conexion, cursor
from servicio_profesor import ServicioProfesor




class Ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana_principal.ui", self)
        self.actionSalir.triggered.connect(QtWidgets.qApp.quit)
        self.actionProfesores.triggered.connect(self.abrir_profesores)
    
    def abrir_profesores(self):
        self.ventana_profesores = VentanaProfesores()
        self.ventana_profesores.show()

class VentanaProfesores(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("profesores.ui", self)
        
        self.btnCerrar.clicked.connect(self.close)

        self.listar_profesor()
        
    def listar_profesor(self):
        servicio_profesor = ServicioProfesor()
        profesores = servicio_profesor.listar_profesores()
        if not profesores:
            print("No hay profesores registrados.")
        else:
            print("\nLista de profesores:")
            self.tlbProfesores.setRowCount(len(profesores))
            
            row = 0
            for  profesor in profesores:
                #print(f"DNI: {prof[0]} | Nombre: {prof[1]} | Apellido: {prof[2]} | CorreoElectronico: {prof[3]} | Telefono: {prof[4]}")
                self.tlbProfesores.setItem(row, 0, QtWidgets.QTableWidgetItem(profesor[0]))
                self.tlbProfesores.setItem(row, 1, QtWidgets.QTableWidgetItem(profesor[1]))
                self.tlbProfesores.setItem(row, 2, QtWidgets.QTableWidgetItem(profesor[2]))
                self.tlbProfesores.setItem(row, 3, QtWidgets.QTableWidgetItem(profesor[3]))
                #self.tlbProfesores.setItem(row, 4, QtWidgets.QTableWidgetItem(profesor[4]))

                row = row + 1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())