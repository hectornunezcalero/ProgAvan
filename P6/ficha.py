from datetime import time

class Ficha:
    def __init__(self, nombre="", edad=0, nacio=time(12, 00, 00)):
        self._nombre = nombre
        self._edad = edad
        self._nacio = nacio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        self._edad = valor

    @property
    def nacio(self):
        return self._nacio

    @nacio.setter
    def nacio(self, valor):
        self._nacio = valor

    def Visualizar(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Nacido: {self.nacio.strftime('%H:%M:%S')}"
