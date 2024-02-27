from src.domain.book import Book
from src.services.services_exception import ServicesException

class BookServices:
    def __init__(self, repository, validator):
        self._book_list = repository
        self._validator = validator

    def add_book(self, book_id, title, author):
        """
        create a new object of class Book and add it to the repository
        :param book_id:
        :param title:
        :param author:
        :return:
        """
        new_book = Book(book_id, title, author)
        self._validator.book_validate(new_book)

        self._book_list.add(new_book)

    def delete_book(self, book_id):
        """
        Delete a book from repo by its id
        :param book_id:
        :return:
        """
        self._book_list.delete(book_id)

    def update_title(self, book_id, title):
        """
        Update the title of a specific book in the repo given by its id
        :param book_id:
        :param title:
        :return:
        """
        self._book_list.update_book_title(book_id, title)

    def update_author(self, book_id, author):
        """
        Update the author of a specific book in the repo given by its id
        :param book_id:
        :param author:
        :return:
        """
        self._book_list.update_book_author(book_id, author)

    def sort_book_list(self):
        """
        bring back a list of book recordings sorted in ascending order by their ids
        :return:
        """
        books_list = sorted(self._book_list.get_all_books(), key=lambda x: x.book_id)
        return books_list

    def search_by_title(self, title):
        """
        Search all books by the title attribute that contain the sub-string given by the user
        :param title:
        :return:
        """
        found_books = self._book_list.search_title(title)
        if len(found_books) == 0:
             raise ServicesException("No results found")
        return found_books

    def search_by_author(self, author):
        """
        Search all books by the author attribute that contain the sub-string given by the user
        :param author:
        :return:
        """
        found_books = self._book_list.search_author(author)
        if len(found_books) == 0:
             raise ServicesException("No results found")
        return found_books

    def search_by_id(self, book_id):
        """
        Return back the book with the id given by the user
        :param book_id:
        :return:
        """
        return self._book_list.get(book_id)
