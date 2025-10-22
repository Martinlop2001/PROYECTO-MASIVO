from PyQt5 import QtWidgets
import sys
from src.test.test_ventana import VentanaPrincipal
from src.pantallas.ventana_principal import Ventana

def main():
    print("Iniciando la aplicación...")
    print("Que programa desea ejecutar?")
    print("1. Ventana Principal")
    print("2. Test Ventana")

    opcion = input("Ingrese 1 o 2: ")

    if opcion == "1":
        app = QtWidgets.QApplication(sys.argv)
        ventana = Ventana()
        ventana.show()
        sys.exit(app.exec_())
    elif opcion == "2":
        app = QtWidgets.QApplication(sys.argv)
        ventana_test = VentanaPrincipal()
        ventana_test.show()
        sys.exit(app.exec_())
    else:
        print("Opción no válida. Saliendo de la aplicación.")

if __name__ == "__main__":
    main()