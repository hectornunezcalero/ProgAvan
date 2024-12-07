def leer_cadena(mensaje):
    cadena = input(mensaje).strip()
    while not cadena:
        print("La entrada no puede estar vacía. Inténtelo de nuevo.")
        cadena = input(mensaje).strip()
    return cadena
