from book import Book

class Library:
    # Representa una biblioteca que gestiona una colección de libros.
    def __init__(self):
        # Inicializa una biblioteca vacía.
        self._books = []

    def add_book(self, book: Book):
        # Agrega un libro a la biblioteca.
        self._books.append(book)

    def remove_book(self, isbn: str):
        # Elimina un libro de la biblioteca usando su ISBN.
        self._books = [book for book in self._books if book.isbn != isbn]

    def borrow_book(self, isbn: str) -> bool:
        # Presta un libro de la biblioteca.
        book = self.find_book(isbn)
        if book and not book.is_borrowed:
            book.is_borrowed = True
            return True
        return False

    def return_book(self, isbn: str) -> bool:
        # Devuelve un libro a la biblioteca.
        book = self.find_book(isbn)
        if book and book.is_borrowed:
            book.is_borrowed = False
            return True
        return False

    def find_book(self, search: str):
        # Busca libros en la biblioteca por título o autor.
        return [book for book in self._books if search.lower() in book.title.lower() or search.lower() in book.author.lower()]

    def __str__(self) -> str:
        # Representa la biblioteca como una cadena de texto.
        return "\n".join(str(book) for book in self._books)
