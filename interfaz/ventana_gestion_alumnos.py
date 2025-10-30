# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from serviciosalum.servicio_alumnos import ServicioAlumnos

class VentanaGestionAlumnos(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.servicio_alumnos = ServicioAlumnos()
        self.alumno_seleccionado = None
        self.setup_ui()
        self.cargar_alumnos()
        
    def setup_ui(self):
        self.setWindowTitle("Gestión de Alumnos")
        self.setGeometry(100, 100, 900, 600)
        
        # Widget central
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        layout_principal = QtWidgets.QVBoxLayout()
        central_widget.setLayout(layout_principal)
        
        # Título
        titulo = QtWidgets.QLabel("Gestión de Alumnos")
        titulo.setAlignment(QtCore.Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        layout_principal.addWidget(titulo)
        
        # Tabla de alumnos (ARRIBA)
        self.tabla_alumnos = QtWidgets.QTableWidget()
        self.tabla_alumnos.setColumnCount(5)
        self.tabla_alumnos.setHorizontalHeaderLabels(["DNI", "Nombre", "Apellido", "Correo", "Teléfono"])
        
        # Configurar la tabla
        header = self.tabla_alumnos.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        
        # Conectar selección de fila
        self.tabla_alumnos.itemSelectionChanged.connect(self.seleccionar_alumno)
        
        # Habilitar menú contextual (click derecho)
        self.tabla_alumnos.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tabla_alumnos.customContextMenuRequested.connect(self.mostrar_menu_contextual)
        
        layout_principal.addWidget(self.tabla_alumnos)
        
        # Frame para formulario (ABAJO)
        frame_formulario = QtWidgets.QFrame()
        frame_formulario.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        frame_formulario.setMaximumHeight(200)
        layout_formulario = QtWidgets.QGridLayout()
        frame_formulario.setLayout(layout_formulario)
        
        # Campos del formulario
        self.label_dni = QtWidgets.QLabel("DNI:")
        self.input_dni = QtWidgets.QLineEdit()
        self.input_dni.setPlaceholderText("Ingrese el DNI (solo números)")
        
        self.label_nombre = QtWidgets.QLabel("Nombre:")
        self.input_nombre = QtWidgets.QLineEdit()
        self.input_nombre.setPlaceholderText("Ingrese el nombre")
        
        self.label_apellido = QtWidgets.QLabel("Apellido:")
        self.input_apellido = QtWidgets.QLineEdit()
        self.input_apellido.setPlaceholderText("Ingrese el apellido")
        
        self.label_correo = QtWidgets.QLabel("Correo:")
        self.input_correo = QtWidgets.QLineEdit()
        self.input_correo.setPlaceholderText("ejemplo@correo.com")
        
        self.label_telefono = QtWidgets.QLabel("Teléfono:")
        self.input_telefono = QtWidgets.QLineEdit()
        self.input_telefono.setPlaceholderText("Ingrese el teléfono")
        
        # Posicionar campos en el grid
        layout_formulario.addWidget(self.label_dni, 0, 0)
        layout_formulario.addWidget(self.input_dni, 0, 1)
        layout_formulario.addWidget(self.label_nombre, 0, 2)
        layout_formulario.addWidget(self.input_nombre, 0, 3)
        
        layout_formulario.addWidget(self.label_apellido, 1, 0)
        layout_formulario.addWidget(self.input_apellido, 1, 1)
        layout_formulario.addWidget(self.label_correo, 1, 2)
        layout_formulario.addWidget(self.input_correo, 1, 3)
        
        layout_formulario.addWidget(self.label_telefono, 2, 0)
        layout_formulario.addWidget(self.input_telefono, 2, 1)
        
        # Botones de acción (EN EL MEDIO)
        frame_botones = QtWidgets.QFrame()
        layout_botones = QtWidgets.QHBoxLayout()
        frame_botones.setLayout(layout_botones)
        
        self.btn_agregar = QtWidgets.QPushButton("Agregar")
        self.btn_agregar.clicked.connect(self.agregar_alumno)
        self.btn_agregar.setStyleSheet("QPushButton { padding: 8px; }")
        
        self.btn_modificar = QtWidgets.QPushButton("Modificar")
        self.btn_modificar.clicked.connect(self.modificar_alumno)
        self.btn_modificar.setStyleSheet("QPushButton { padding: 8px; }")
        
        self.btn_eliminar = QtWidgets.QPushButton("Eliminar")
        self.btn_eliminar.clicked.connect(self.eliminar_alumno)
        self.btn_eliminar.setStyleSheet("QPushButton { padding: 8px; }")
        
        self.btn_limpiar = QtWidgets.QPushButton("Limpiar")
        self.btn_limpiar.clicked.connect(self.limpiar_formulario)
        self.btn_limpiar.setStyleSheet("QPushButton { padding: 8px; }")
        
        self.btn_actualizar = QtWidgets.QPushButton("Actualizar Lista")
        self.btn_actualizar.clicked.connect(self.cargar_alumnos)
        self.btn_actualizar.setStyleSheet("QPushButton { padding: 8px; }")
        
        layout_botones.addWidget(self.btn_agregar)
        layout_botones.addWidget(self.btn_modificar)
        layout_botones.addWidget(self.btn_eliminar)
        layout_botones.addWidget(self.btn_limpiar)
        layout_botones.addWidget(self.btn_actualizar)
        layout_botones.addStretch()
        
        layout_principal.addWidget(frame_botones)
        
        # Agregar el formulario al final (ABAJO)
        layout_principal.addWidget(frame_formulario)
        
        # Configurar validadores
        self.input_dni.textChanged.connect(self.validar_dni)
        
    def validar_dni(self):
        """Valida que el DNI solo contenga números"""
        dni = self.input_dni.text()
        if not dni.isdigit():
            self.input_dni.setText(dni[:-1] if len(dni) > 0 else "")
            
    def cargar_alumnos(self):
        """Carga todos los alumnos en la tabla"""
        try:
            alumnos = self.servicio_alumnos.listar_alumnos()
            self.tabla_alumnos.setRowCount(len(alumnos))
            
            for i, alumno in enumerate(alumnos):
                self.tabla_alumnos.setItem(i, 0, QTableWidgetItem(str(alumno.get('dni', ''))))
                self.tabla_alumnos.setItem(i, 1, QTableWidgetItem(alumno.get('nombre', '')))
                self.tabla_alumnos.setItem(i, 2, QTableWidgetItem(alumno.get('apellido', '')))
                self.tabla_alumnos.setItem(i, 3, QTableWidgetItem(alumno.get('correo', '')))
                self.tabla_alumnos.setItem(i, 4, QTableWidgetItem(alumno.get('telefono', '')))
                
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar alumnos: {str(e)}")
            
    def seleccionar_alumno(self):
        """Se ejecuta cuando se selecciona un alumno en la tabla"""
        fila_actual = self.tabla_alumnos.currentRow()
        if fila_actual >= 0:
            dni = self.tabla_alumnos.item(fila_actual, 0).text()
            self.alumno_seleccionado = self.servicio_alumnos.buscar_alumno_por_dni(dni)
            
            if self.alumno_seleccionado:
                self.input_dni.setText(str(self.alumno_seleccionado.get('dni', '')))
                self.input_nombre.setText(self.alumno_seleccionado.get('nombre', ''))
                self.input_apellido.setText(self.alumno_seleccionado.get('apellido', ''))
                self.input_correo.setText(self.alumno_seleccionado.get('correo', ''))
                self.input_telefono.setText(self.alumno_seleccionado.get('telefono', ''))
                
    def limpiar_formulario(self):
        """Limpia todos los campos del formulario"""
        self.input_dni.clear()
        self.input_nombre.clear()
        self.input_apellido.clear()
        self.input_correo.clear()
        self.input_telefono.clear()
        self.alumno_seleccionado = None
        self.tabla_alumnos.clearSelection()
        
    def mostrar_menu_contextual(self, posicion):
        """Muestra el menú contextual al hacer click derecho en la tabla"""
        # Verificar si hay una fila seleccionada
        fila_actual = self.tabla_alumnos.currentRow()
        if fila_actual < 0:
            return
            
        # Crear el menú contextual
        menu_contextual = QtWidgets.QMenu(self)
        
        # Acción para eliminar
        accion_eliminar = menu_contextual.addAction("Eliminar Alumno")
        accion_eliminar.triggered.connect(self.eliminar_alumno_contextual)
        
        # Mostrar el menú en la posición del cursor
        menu_contextual.exec_(self.tabla_alumnos.mapToGlobal(posicion))
        
    def eliminar_alumno_contextual(self):
        """Elimina el alumno seleccionado desde el menú contextual"""
        fila_actual = self.tabla_alumnos.currentRow()
        if fila_actual < 0:
            QMessageBox.warning(self, "Advertencia", "Seleccione un alumno para eliminar")
            return
            
        # Obtener los datos del alumno de la tabla
        dni = self.tabla_alumnos.item(fila_actual, 0).text()
        nombre = self.tabla_alumnos.item(fila_actual, 1).text()
        apellido = self.tabla_alumnos.item(fila_actual, 2).text()
        
        # Mostrar confirmación
        respuesta = QMessageBox.question(
            self, 
            "Confirmar eliminación", 
            f"¿Está seguro que desea eliminar al alumno {nombre} {apellido} (DNI: {dni})?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if respuesta == QMessageBox.Yes:
            resultado, mensaje = self.servicio_alumnos.eliminar_alumno(dni)
            
            if resultado:
                QMessageBox.information(self, "Éxito", mensaje)
                self.limpiar_formulario()
                self.cargar_alumnos()
            else:
                QMessageBox.warning(self, "Error", mensaje)
        
    def agregar_alumno(self):
        """Agrega un nuevo alumno"""
        dni = self.input_dni.text().strip()
        nombre = self.input_nombre.text().strip()
        apellido = self.input_apellido.text().strip()
        correo = self.input_correo.text().strip()
        telefono = self.input_telefono.text().strip()
        
        if not dni or not nombre or not apellido:
            QMessageBox.warning(self, "Advertencia", "DNI, nombre y apellido son obligatorios")
            return
            
        resultado, mensaje = self.servicio_alumnos.insertar_alumno(dni, nombre, apellido, correo, telefono)
        
        if resultado:
            QMessageBox.information(self, "Éxito", mensaje)
            self.limpiar_formulario()
            self.cargar_alumnos()
        else:
            QMessageBox.warning(self, "Error", mensaje)
            
    def modificar_alumno(self):
        """Modifica un alumno existente"""
        if not self.alumno_seleccionado:
            QMessageBox.warning(self, "Advertencia", "Seleccione un alumno para modificar")
            return
            
        dni = self.input_dni.text().strip()
        nombre = self.input_nombre.text().strip()
        apellido = self.input_apellido.text().strip()
        correo = self.input_correo.text().strip()
        telefono = self.input_telefono.text().strip()
        
        if not dni or not nombre or not apellido:
            QMessageBox.warning(self, "Advertencia", "DNI, nombre y apellido son obligatorios")
            return
            
        resultado, mensaje = self.servicio_alumnos.modificar_alumno(dni, nombre, apellido, correo, telefono)
        
        if resultado:
            QMessageBox.information(self, "Éxito", mensaje)
            self.limpiar_formulario()
            self.cargar_alumnos()
        else:
            QMessageBox.warning(self, "Error", mensaje)
            
    def eliminar_alumno(self):
        """Elimina un alumno"""
        if not self.alumno_seleccionado:
            QMessageBox.warning(self, "Advertencia", "Seleccione un alumno para eliminar")
            return
            
        dni = self.input_dni.text().strip()
        nombre = self.input_nombre.text().strip()
        apellido = self.input_apellido.text().strip()
        
        respuesta = QMessageBox.question(
            self, 
            "Confirmar eliminación", 
            f"¿Está seguro que desea eliminar al alumno {nombre} {apellido} (DNI: {dni})?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if respuesta == QMessageBox.Yes:
            resultado, mensaje = self.servicio_alumnos.eliminar_alumno(dni)
            
            if resultado:
                QMessageBox.information(self, "Éxito", mensaje)
                self.limpiar_formulario()
                self.cargar_alumnos()
            else:
                QMessageBox.warning(self, "Error", mensaje)
