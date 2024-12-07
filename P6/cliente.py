from ficha import Ficha

class Cliente(Ficha):
    
    def __init__(self, nombre="", edad=0, nacio=None, dni=""):
        super().__init__(nombre, edad, nacio)
        self._dni = dni

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, valor):
        self._dni = valor

    def Visualizar(self):
        base = super().Visualizar()
        return f"{base}, DNI: {self.dni}"

    def __eq__(self, otro):
        return isinstance(otro, Cliente) and self.nombre == otro.nombre and self.edad == otro.edad
