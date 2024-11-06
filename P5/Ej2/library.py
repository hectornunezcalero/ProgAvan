from book import Book

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        self._books.append(book)

    def remove_book(self, isbn: str):
        self._books = [book for book in self._books if book.isbn != isbn]

    def borrow_book(self, isbn: str):
        book = self.find_book(isbn)
        if book and not book.is_borrowed:
            book.is_borrowed = True
            return True
        return False

    def return_book(self, isbn: str):
        book = self.find_book(isbn)
        if book and book.is_borrowed:
            book.is_borrowed = False
            return True
        return False

    def find_book(self, search: str):
        return [book for book in self._books if search.lower() in book.title.lower() or search.lower() in book.author.lower()]

    def __str__(self) -> str:
        return "\n".join(str(book) for book in self._books)
