

#Sistema de Gestión de Alumnos
#Aplicación principal para gestionar alumnos con interfaz gráfica en PyQt5


import sys
import os
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt

# Agregar el directorio actual al path para importaciones
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from ventanas.ventana_principal import VentanaPrincipal
except ImportError as e:
    print(f"Error al importar módulos: {e}")
    print("Asegúrate de tener instaladas todas las dependencias:")
    print("pip install PyQt5 psycopg2-binary")
    sys.exit(1)

def main():
    """Función principal de la aplicación"""
    
    # Crear la aplicación
    app = QApplication(sys.argv)
    app.setApplicationName("Sistema de Gestión de Alumnos")
    app.setApplicationVersion("1.0")
    
    # Configurar el estilo de la aplicación
    app.setStyle('Fusion')
    
    # Configurar la paleta de colores
    palette = app.palette()
    palette.setColor(palette.Window, Qt.white)
    palette.setColor(palette.WindowText, Qt.black)
    app.setPalette(palette)
    
    try:
        # Crear y mostrar la ventana principal
        ventana_principal = VentanaPrincipal()
        ventana_principal.show()
        
        # Ejecutar la aplicación
        sys.exit(app.exec_())
        
    except Exception as e:
        # Mostrar error si algo falla
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle("Error de la Aplicación")
        msg_box.setText("Ha ocurrido un error al iniciar la aplicación:")
        msg_box.setDetailedText(str(e))
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()
        
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
