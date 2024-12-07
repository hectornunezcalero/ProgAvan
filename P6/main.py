from datetime import time
from registro_diario import RegistroDiario
from empleado import Empleado
from cliente import Cliente
from utils import leer_cadena

def menu():
    registro = RegistroDiario()
    otro_registro = RegistroDiario()

    while True:
        print("\nMenú:")
        print("1. Introducir empleado")
        print("2. Introducir cliente")
        print("3. Buscar por nombre y edad")
        print("4. Mostrar registro diario")
        print("5. Mostrar empleados")
        print("6. Visualizar persona por índice")
        print("7. Combinar registros diarios")
        print("8. Salir")
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = leer_cadena("Nombre del empleado: ")
            edad = int(input("Edad: "))
            nacio = time.fromisoformat(input("Hora de nacimiento (HH:MM:SS): "))
            categoria = leer_cadena("Categoría: ")
            antiguedad = int(input("Antigüedad: "))
            registro.agregar_persona(Empleado(nombre, edad, nacio, categoria, antiguedad))
        
        elif opcion == "2":
            nombre = leer_cadena("Nombre del cliente: ")
            edad = int(input("Edad: "))
            nacio = time.fromisoformat(input("Hora de nacimiento (HH:MM:SS): "))
            dni = leer_cadena("DNI: ")
            registro.agregar_persona(Cliente(nombre, edad, nacio, dni))
        
        elif opcion == "3":
            nombre = leer_cadena("Nombre: ")
            edad = int(input("Edad: "))
            encontrado = False
            for persona in registro._personas:
                if persona.nombre == nombre and persona.edad == edad:
                    print("Persona encontrada:")
                    print(persona.Visualizar())
                    encontrado = True
                    break
            if not encontrado:
                print("Persona no encontrada.")
        
        elif opcion == "4":
            registro.visualizar_registro()
        
        elif opcion == "5":
            registro.visualizar_empleados()
        
        elif opcion == "6":
            indice = int(input("Índice: "))
            try:
                print(registro[indice].Visualizar())
            except IndexError:
                print("Índice fuera de rango.")
        
        elif opcion == "7":
            otro_registro.agregar_persona(Cliente("Juan", 30, time(10, 0, 0), "12345678A"))
            otro_registro.agregar_persona(Empleado("Ana", 40, time(12, 0, 0), "Técnico", 10))
            registro = registro + otro_registro
            print("Registros combinados.")
        
        elif opcion == "8":
            break
        
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu()
