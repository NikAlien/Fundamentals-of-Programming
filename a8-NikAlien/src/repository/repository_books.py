import pickle
from src.domain.book import Book
from src.repository.repository_exception import RepositoryException

class MemoryRepositoryBooks:
    def __init__(self):
        self._data = {}

    def add(self, new_book: Book):
        if new_book.book_id in self._data:
            raise RepositoryException("Book already in repo")
        self._data[new_book.book_id] = new_book

    def delete(self, book_id):
        if book_id not in self._data:
            raise RepositoryException("Book not in repo")
        del self._data[book_id]

    def get_all_books(self):
        return list(self._data.values())

    def get(self, book_id):
        if book_id not in self._data:
            return None
        return self._data[book_id]

    # The whole search
    def search_author(self, author: str):
        found_books = []

        for book in self.get_all_books():
            if author.lower() in book.name.lower():
                found_books.append(book)

        return found_books

    def search_title(self, title: str):
        found_books = []

        for book in self.get_all_books():
            if title.lower() in book.title.lower():
                found_books.append(book)

        return found_books

    def update_book_title(self, book_id, book_title):
        if book_id not in self._data:
            raise RepositoryException("Book id not in repo")
        self._data[book_id].title = book_title

    def update_book_author(self, book_id, book_author):
        if book_id not in self._data:
            raise RepositoryException("Book id not in repo")
        self._data[book_id].name = book_author

class TextFileRepositoryBooks(MemoryRepositoryBooks):
    def __init__(self, file_name = "books.txt"):
        super(TextFileRepositoryBooks, self).__init__()

        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        fin = open(self._file_name, "rt")
        lines = fin.readlines()
        fin.close()

        for line in lines:
            book_line = line.split(",")
            new_book = Book(int(book_line[0]), book_line[1], book_line[2].strip())
            super().add(new_book)

    def _save_file(self):
        fout = open(self._file_name, "wt")

        for book_line in self.get_all_books():
            book_line = str(book_line.book_id) + "," + book_line.title + "," + str(book_line.name) + "\n"
            fout.write(book_line)

        fout.close()

    def add(self, new_book: Book):
        super().add(new_book)
        self._save_file()

    def delete(self, book_id):
        super().delete(book_id)
        self._save_file()

    def update_book_title(self, book_id, book_title):
        super().update_book_title(book_id, book_title)
        self._save_file()

    def update_book_author(self, book_id, book_author):
        super().update_book_author(book_id, book_author)
        self._save_file()

class BinaryFileRepositoryBooks(MemoryRepositoryBooks):
    def __init__(self, file_name="books.bin"):
        super(BinaryFileRepositoryBooks, self).__init__()

        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        fin = open(self._file_name, "rb")
        books = pickle.load(fin)

        for book_line in books:
            super().add(book_line)
        fin.close()

    def _save_file(self):
        fout = open(self._file_name, "wb")
        pickle.dump(self.get_all_books(), fout)
        fout.close()

    def add(self, new_book: Book):
        super().add(new_book)
        self._save_file()

    def delete(self, book_id):
        super().delete(book_id)
        self._save_file()

    def update_book_title(self, book_id, book_title):
        super().update_book_title(book_id, book_title)
        self._save_file()

    def update_book_author(self, book_id, book_author):
        super().update_book_author(book_id, book_author)
        self._save_file()
