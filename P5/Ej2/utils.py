from typing import List, Dict
import uuid

def leer_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Error: Debes ingresar un número entero.")

def leer_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Debes ingresar un número flotante.")

def crear_menu(options: List[str]) -> int:
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
    unique_id = uuid.uuid4()  # Genera un UUID de versión 4.
    return str(unique_id)[:8]
