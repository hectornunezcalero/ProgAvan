from library import Library
from book import Book
from user import User

def main():
    # Función principal para interactuar con el sistema de la biblioteca.
    
    # Crear instancias de la biblioteca, usuario y libros
    library = Library()
    user = User("Juan Pérez", "U001")
    
    book1 = Book("El Quijote", "Miguel de Cervantes", "978-3-16-148410-0")
    book2 = Book("1984", "George Orwell", "978-0-452-28423-4")
    
    # Agregar libros a la biblioteca
    library.add_book(book1)
    library.add_book(book2)

    # Mostrar todos los libros en la biblioteca
    print("Biblioteca actual:")
    print(library)

    # Prestar un libro y mostrar libros prestados
    library.borrow_book("978-3-16-148410-0")
    user.borrow_book(book1)
    print("\nLibros prestados por el usuario:")
    print(user)

    # Devolver un libro y actualizar la información
    library.return_book("978-3-16-148410-0")
    user.return_book(book1)
    print("\nLibros prestados por el usuario después de la devolución:")
    print(user)

if __name__ == "__main__":
    main()
