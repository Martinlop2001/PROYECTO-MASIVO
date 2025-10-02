from PyQt5 import QtWidgets
import sys
from test_ventana import VentanaPrincipal

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())