from library import Library
from book import Book
from user import User
from utils import leer_int, crear_menu, leer_float, generar_id_unico

def main():
    # Crear instancia de la biblioteca
    library = Library()
    users = {}
    
    # Función auxiliar para mostrar todos los libros
    def mostrar_libros():
        if library.books:
            print("\nListado de libros en la biblioteca:")
            print(library)
        else:
            print("\nNo hay libros en la biblioteca.")

    # Función auxiliar para registrar un nuevo usuario
    def registrar_usuario():
        print("\nRegistro de usuario:")
        nombre = input("Introduce el nombre del usuario: ")
        user_id = generar_id_unico()
        users[user_id] = User(nombre, user_id)
        print(f"Usuario registrado con éxito. ID de usuario: {user_id}")

    # Función auxiliar para añadir un libro
    def añadir_libro():
        print("\nAñadir libro:")
        titulo = input("Introduce el título del libro: ")
        autor = input("Introduce el autor del libro: ")
        isbn = input("Introduce el ISBN del libro: ")
        libro = Book(titulo, autor, isbn)
        library.add_book(libro)
        print(f"Libro '{titulo}' añadido a la biblioteca.")

    # Función auxiliar para eliminar un libro
    def eliminar_libro():
        mostrar_libros()
        isbn = input("\nIntroduce el ISBN del libro a eliminar: ")
        if library.remove_book(isbn):
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print(f"No se encontró ningún libro con ISBN {isbn}.")

    # Función auxiliar para realizar un préstamo
    def realizar_prestamo():
        mostrar_libros()
        isbn = input("\nIntroduce el ISBN del libro a prestar: ")
        user_id = input("Introduce el ID del usuario: ")
        if user_id in users:
            usuario = users[user_id]
            libro = library.borrow_book(isbn)
            if libro:
                usuario.borrow_book(libro)
                print(f"Libro '{libro.title}' prestado al usuario '{usuario.name}'.")
            else:
                print(f"El libro con ISBN {isbn} no está disponible.")
        else:
            print("Usuario no registrado.")

    # Función auxiliar para realizar una devolución
    def realizar_devolucion():
        user_id = input("\nIntroduce el ID del usuario: ")
        if user_id in users:
            usuario = users[user_id]
            if usuario.borrowed_books:
                print("\nLibros prestados por el usuario:")
                for i, book in enumerate(usuario.borrowed_books, 1):
                    print(f"{i}. {book.title} (ISBN: {book.isbn})")
                indice = leer_int("Introduce el número del libro a devolver: ") - 1
                if 0 <= indice < len(usuario.borrowed_books):
                    libro = usuario.borrowed_books[indice]
                    usuario.return_book(libro)
                    library.return_book(libro.isbn)
                    print(f"Libro '{libro.title}' devuelto con éxito.")
                else:
                    print("Selección inválida.")
            else:
                print("El usuario no tiene libros prestados.")
        else:
            print("Usuario no registrado.")

    # Opciones del menú
    opciones = [
        "Añadir libro",
        "Eliminar libro",
        "Registrar usuario",
        "Realizar préstamo",
        "Realizar devolución",
        "Mostrar todos los libros",
        "Salir"
    ]

    while True:
        print("\n=== Biblioteca ===")
        eleccion = crear_menu(opciones)
        
        # Usamos match-case para las opciones
        match eleccion:
            case 1:  # Añadir libro
                añadir_libro()
            case 2:  # Eliminar libro
                eliminar_libro()
            case 3:  # Registrar usuario
                registrar_usuario()
            case 4:  # Realizar préstamo
                realizar_prestamo()
            case 5:  # Realizar devolución
                realizar_devolucion()
            case 6:  # Mostrar todos los libros
                mostrar_libros()
            case 7:  # Salir
                print("Saliendo del sistema de la biblioteca.")
                break
            case _:
                print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
