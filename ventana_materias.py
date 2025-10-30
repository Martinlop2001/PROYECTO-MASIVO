import sys
from PyQt5 import QtWidgets, uic
from entidades.materias import Materia
import sqlite3
from db.conexion import conexion, cursor
from servicios.servicio_materia import ServicioMateria


class Ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana_materias.ui", self)   
        self.actionSalir.triggered.connect(QtWidgets.qApp.quit)
        self.actionMaterias.triggered.connect(self.abrir_Materias)

    
    def abrir_Materias(self):
        self.ventana_materias = VentanaMaterias()
        self.ventana_materias.show()

        #sexo


class VentanaMaterias(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("materias.ui", self)   
        
        self.btnCerrar.clicked.connect(self.close)
        self.btnAgregar.clicked.connect(self.agregar_materia)
        self.btnEliminar.clicked.connect(self.eliminar_materia)
        self.btnModificar.clicked.connect(self.modificar_materia)
        self.tlbMaterias.itemSelectionChanged.connect(self.cargar_datos_seleccionados)


        self.listar_materia()
        
    def listar_materia(self):

        servicio_materia = ServicioMateria()
        materias = servicio_materia.listar_materias()


        if not materias:
            print("No hay materias registradas.")
        else:
            print("\nLista de materias:")
            self.tlbMaterias.setRowCount(len(materias))
            
            row = 0
            for materia in materias:
                self.tlbMaterias.setItem(row, 0, QtWidgets.QTableWidgetItem(str(materia[0])))
                self.tlbMaterias.setItem(row, 1, QtWidgets.QTableWidgetItem(str(materia[1])))
                self.tlbMaterias.setItem(row, 2, QtWidgets.QTableWidgetItem(str(materia[2])))
                row += 1

    def agregar_materia(self):
        nombre = self.txtNombre.text()
        carrera = self.txtCarrera.text()
        anio = self.txtAnio.text()

        if not nombre or not carrera or not anio:
            QtWidgets.QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        try:
            anio = int(anio)
            servicio = ServicioMateria()
            servicio.agregar_materia(nombre, carrera, anio)
            QtWidgets.QMessageBox.information(self, "Éxito", "Materia agregada correctamente.")
            self.listar_materia()  # refresca la tabla
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo agregar la materia: {e}")

    def eliminar_materia(self):

        
        fila = self.tlbMaterias.currentRow()
        if fila == -1:
            QtWidgets.QMessageBox.warning(self, "Error", "Seleccioná una materia para eliminar.")
            return

        nombre = self.tlbMaterias.item(fila, 0).text()


        confirmar = QtWidgets.QMessageBox.question(
            self,
            "Confirmar",
            "¿Seguro que querés eliminar esta materia?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )

        if confirmar == QtWidgets.QMessageBox.Yes:
            try:
                servicio = ServicioMateria()
                servicio.eliminar_materia(nombre)
                QtWidgets.QMessageBox.information(self, "Éxito", "Materia eliminada.")
                self.listar_materia()
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo eliminar la materia: {e}")

    def modificar_materia(self):
        fila = self.tlbMaterias.currentRow()
        if fila == -1:
            QtWidgets.QMessageBox.warning(self, "Error", "Seleccioná una materia para modificar.")
            return

        # Tomamos el nombre actual (clave para buscar)
        nombre_original = self.tlbMaterias.item(fila, 0).text()

        # Nuevos valores desde los campos de texto
        nuevo_nombre = self.txtNombre.text()
        nueva_carrera = self.txtCarrera.text()
        nuevo_anio = self.txtAnio.text()

        if not nuevo_nombre or not nueva_carrera or not nuevo_anio:
            QtWidgets.QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        try:
            nuevo_anio = int(nuevo_anio)
            servicio = ServicioMateria()
            servicio.modificar_materia(nombre_original, nuevo_nombre, nueva_carrera, nuevo_anio)
            QtWidgets.QMessageBox.information(self, "Éxito", "Materia modificada correctamente.")
            self.listar_materia()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"No se pudo modificar la materia: {e}")

    def cargar_datos_seleccionados(self):
        fila = self.tlbMaterias.currentRow()
        if fila != -1:
            self.txtNombre.setText(self.tlbMaterias.item(fila, 0).text())
            self.txtCarrera.setText(self.tlbMaterias.item(fila, 1).text())
            self.txtAnio.setText(self.tlbMaterias.item(fila, 2).text())






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
