from book import Book
from library import Library
from user import User
from utils import leer_int, leer_float, crear_menu

# Crear libros
book1 = Book("1984", "George Orwell", "12345")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "67890")

# Crear biblioteca
library = Library()
library.add_book(book1)
library.add_book(book2)

# Crear usuario
user = User("Juan", "001")

# Interacción con la biblioteca
library.borrow_book("12345")
user.borrow_book(book1)

print(library)
print(user)
