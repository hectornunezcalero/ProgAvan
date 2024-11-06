class Book:
    # Representa un libro con título, autor, ISBN y estado de préstamo.
    def __init__(self, title: str, author: str, isbn: str, is_borrowed: bool = False):
        # Inicializa un libro con título, autor, ISBN y estado de préstamo.
        self._title = title
        self._author = author
        self._isbn = isbn
        self._is_borrowed = is_borrowed

    @property
    def title(self) -> str:
        # Devuelve el título del libro.
        return self._title

    @property
    def author(self) -> str:
        # Devuelve el autor del libro.
        return self._author

    @property
    def isbn(self) -> str:
        # Devuelve el ISBN del libro.
        return self._isbn

    @property
    def is_borrowed(self) -> bool:
        # Devuelve si el libro está prestado.
        return self._is_borrowed

    @is_borrowed.setter
    def is_borrowed(self, status: bool):
        # Establece el estado de préstamo del libro.
        self._is_borrowed = status

    def __str__(self) -> str:
        # Representa el libro como una cadena con sus detalles.
        status = "Prestado" if self._is_borrowed else "Disponible"
        return f"Título: {self._title}, Autor: {self._author}, ISBN: {self._isbn}, Estado: {status}"
