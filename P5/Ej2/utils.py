def leer_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Debes ingresar un número entero.")

def leer_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Debes ingresar un número flotante.")

def crear_menu(options: list) -> int:
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
