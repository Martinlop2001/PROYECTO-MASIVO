import re

class Verificacion:

    def __init__(self, usuario, contrasena):
        self.usuario = usuario
        self.contrasena = contrasena

    def verificar_tamaño(self):
        if self.usuario and self.contrasena is None:
            return False
        elif re.fullmatch(r'.{3,10}', self.usuario) and re.fullmatch(r'.{8,12}', self.contrasena):
            return True
        return False
