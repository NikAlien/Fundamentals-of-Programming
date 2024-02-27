from src.domain.validatorException import ValidatorException
from src.domain.book import Book

class BookValidator:
    def __init__(self):
        self._errors = ""

    def book_validate(self, book):
        if not isinstance(book, Book):
            raise TypeError("Can only validate Book objects")

        self._errors = []
        if book.book_id is None:
            self._errors.append("Book must have an id")
        if book.title is None:
            self._errors.append("Book must have a title")
        if book.name is None:
            self._errors.append("Book must have an author")

        if len(self._errors) > 0:
            raise ValidatorException(self._errors)
        return True
