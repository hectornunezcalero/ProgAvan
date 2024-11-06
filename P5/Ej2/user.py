class User:
    def __init__(self, name: str, user_id: str):
        self._name = name
        self._user_id = user_id
        self._borrowed_books = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def user_id(self) -> str:
        return self._user_id

    @property
    def borrowed_books(self) -> list:
        return self._borrowed_books

    def borrow_book(self, book):
        self._borrowed_books.append(book)

    def return_book(self, book):
        self._borrowed_books.remove(book)

    def __str__(self) -> str:
        return f"Nombre: {self._name}, ID: {self._user_id}, Libros Prestados: {[book.title for book in self._borrowed_books]}"
