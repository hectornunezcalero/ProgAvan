from publicacion import Libro, Revista
from utils import guardar_publicaciones, cargar_publicaciones
from excepciones import ErrorArchivo

def menu():
    publicaciones = []
    while True:
        print("\nMenú:")
        print("1. Añadir publicaciones (libros o revistas).")
        print("2. Mostrar publicaciones disponibles.")
        print("3. Guardar publicaciones en un fichero.")
        print("4. Cargar publicaciones desde un fichero.")
        print("5. Salir.")
        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                tipo = input("¿Es un libro o una revista? (l/r): ").strip().lower()
                try:
                    titulo = input("Título: ")
                    autor = input("Autor: ")
                    anio = int(input("Año: "))

                    if tipo == 'l':
                        genero = input("Género: ")
                        publicaciones.append(Libro(titulo, autor, anio, genero))
                    elif tipo == 'r':
                        num_edicion = int(input("Número de edición: "))
                        publicaciones.append(Revista(titulo, autor, anio, num_edicion))
                    else:
                        print("Tipo no válido.")
                except ValueError as e:
                    print(f"Error: {e}")

            case "2":
                if publicaciones:
                    for pub in publicaciones:
                        print(pub.descripcion())
                else:
                    print("No hay publicaciones registradas.")

            case "3":
                nombre_archivo = input("Nombre del archivo: ")
                try:
                    guardar_publicaciones(nombre_archivo, publicaciones)
                    print("Publicaciones guardadas exitosamente.")
                except ErrorArchivo as e:
                    print(f"Error: {e}")

            case "4":
                nombre_archivo = input("Nombre del archivo: ")
                try:
                    publicaciones = cargar_publicaciones(nombre_archivo)
                    print("Publicaciones cargadas exitosamente.")
                except ErrorArchivo as e:
                    print(f"Error: {e}")

            case "5":
                print("Saliendo del programa.")
                break

            case _:
                print("Opción no válida.")
