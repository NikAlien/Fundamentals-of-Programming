from unittest import TestCase
from src.domain.book_validator import BookValidator
from src.repository.repository_books import MemoryRepositoryBooks
from src.services.book_services import BookServices


class TestBookServices(TestCase):
    def setUp(self):
        self.book_list = MemoryRepositoryBooks()
        self.serv = BookServices(self.book_list, BookValidator())
    def test_add_book(self):
        self.fail()

    def test_delete_book(self):
        self.fail()

    def test_update_title(self):
        self.fail()

    def test_update_author(self):
        self.fail()

    def test_search_by_title(self):
        self.fail()

    def test_search_by_author(self):
        self.fail()

    def test_search_by_id(self):
        self.fail()

class TestBookService(TestBookServices):
    def test_add_book(self):
        self.serv.add_book(1, "Little Women", "Louisa May Alcotta")
        self.assertEqual(len(self.book_list.get_all_books()), 1)

    def test_delete_book(self):
        self.serv.add_book(1, "Little Women", "Louisa May Alcotta")
        self.serv.add_book(2, "Little Women", "Louisa May Alcotta")
        self.assertEqual(len(self.book_list.get_all_books()), 2)
        self.serv.delete_book(1)
        self.assertEqual(len(self.book_list.get_all_books()), 1)

    def test_update_title(self):
        self.serv.add_book(1, "Little Women", "Louisa May Alcotta")
        self.serv.add_book(2, "Little Women", "Louisa May Alcotta")
        self.serv.update_title(2, "SPO")
        self.assertEqual(self.book_list.get(2).title, "SPO")

    def test_update_author(self):
        self.serv.add_book(1, "Little Women", "Louisa May Alcotta")
        self.serv.add_book(2, "Little Women", "Louisa May Alcotta")
        self.serv.update_author(1, "Carp Nik")
        self.assertEqual(self.book_list.get(1).name, "Carp Nik")

    def test_search_by_id(self):
        self.serv.add_book(1, "Little Women", "Louisa May Alcotta")
        self.serv.add_book(2, "SPO", "Carp Nik")
        book = self.serv.search_by_id(2)
        self.assertEqual(book.name, "Carp Nik")

    def test_search_by_author(self):
        self.serv.add_book(1, "Little Women", "Louisa May Alcotta")
        self.serv.add_book(2, "SPO", "Carp Nik")
        book = self.serv.search_by_author("i")
        self.assertEqual(len(book), 2)

    def test_search_by_title(self):
        self.serv.add_book(1, "Little Women", "Louisa May Alcotta")
        self.serv.add_book(2, "SPO", "Carp Nik")
        book = self.serv.search_by_title("o")
        self.assertEqual(len(book), 2)