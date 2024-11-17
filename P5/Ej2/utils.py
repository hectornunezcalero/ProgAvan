from typing import List, Dict
import uuid

def leer_int(prompt: str) -> int:
    """
    Lee un número entero del usuario con manejo de errores y anotaciones de tipo.
    :param prompt: Mensaje para mostrar al usuario.
    :return: Número entero ingresado por el usuario.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Error: Debes ingresar un número entero.")

def leer_float(prompt: str) -> float:
    """
    Lee un número flotante del usuario con manejo de errores y anotaciones de tipo.
    :param prompt: Mensaje para mostrar al usuario.
    :return: Número flotante ingresado por el usuario.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Debes ingresar un número flotante.")

def crear_menu(options: List[str]) -> int:
    """
    Crea un menú numerado y solicita al usuario seleccionar una opción.
    :param options: Lista de opciones a mostrar en el menú.
    :return: Índice de la opción seleccionada por el usuario.
    """
    if not isinstance(options, list) or not all(isinstance(option, str) for option in options):
        raise TypeError("Error: 'options' debe ser una lista de cadenas de texto.")
    
    print("\nMenú de opciones:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = leer_int("Selecciona una opción: ")
            if 1 <= choice <= len(options):
                return choice
            else:
                print(f"Error: Elige una opción entre 1 y {len(options)}.")
        except ValueError:
            print("Error: Debes ingresar un número válido.")

def generar_id_unico() -> str:
    """
    Genera un ID único utilizando uuid4() y devuelve los primeros 8 caracteres.
    :return: ID único como cadena de texto (8 caracteres).
    """
    unique_id = uuid.uuid4()  # Genera un UUID de versión 4.
    return str(unique_id)[:8]
