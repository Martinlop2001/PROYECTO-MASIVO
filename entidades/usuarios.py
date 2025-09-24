class Usarios:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña

    def saludar(self):
        return f"{self.nombre}, {self.contraseña}"