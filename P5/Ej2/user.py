class User:
    # Representa un usuario de la biblioteca con nombre, ID y libros prestados.
    def __init__(self, name: str, user_id: str):
        # Inicializa un usuario con nombre, ID y libros prestados.
        self._name = name
        self._user_id = user_id
        self._borrowed_books = []

    @property
    def name(self) -> str:
        # Devuelve el nombre del usuario.
        return self._name

    @property
    def user_id(self) -> str:
        # Devuelve el ID del usuario.
        return self._user_id

    @property
    def borrowed_books(self) -> list:
        # Devuelve la lista de libros prestados al usuario.
        return self._borrowed_books

    def borrow_book(self, book):
        # Presta un libro al usuario.
        self._borrowed_books.append(book)

    def return_book(self, book):
        # Devuelve un libro que el usuario tiene prestado.
        self._borrowed_books.remove(book)

    def __str__(self) -> str:
        # Representa al usuario como una cadena de texto con sus datos.
        return f"Nombre: {self._name}, ID: {self._user_id}, Libros Prestados: {[book.title for book in self._borrowed_books]}"
