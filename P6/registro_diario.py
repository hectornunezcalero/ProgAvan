from empleado import Empleado
from cliente import Cliente

class RegistroDiario:
    def __init__(self):
        self._personas = []

    def agregar_persona(self, persona):
        if isinstance(persona, (Empleado, Cliente)):
            self._personas.append(persona)

    def visualizar_registro(self):
        for persona in self._personas:
            print(persona.Visualizar())

    def visualizar_empleados(self):
        for persona in self._personas:
            if isinstance(persona, Empleado):
                print(persona.Visualizar())

    def es_empleado(self, persona):
        return isinstance(persona, Empleado) is not None

    def __getitem__(self, indice):
        if 0 <= indice < len(self._personas):
            return self._personas[indice]
        else:
            raise IndexError("Índice fuera de rango.")

    def __add__(self, otro_registro):
        nuevo_registro = RegistroDiario()
        nuevo_registro._personas = self._personas + otro_registro._personas
        return nuevo_registro
