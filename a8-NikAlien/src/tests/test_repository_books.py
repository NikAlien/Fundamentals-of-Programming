from unittest import TestCase

from src.domain.book import Book
from src.repository.repository_books import MemoryRepositoryBooks

class TestMemoryRepositoryBooks(TestCase):
    def setUp(self):
        self.book_list = MemoryRepositoryBooks()
    def test_add(self):
        self.fail()

    def test_delete(self):
        self.fail()

    def test_get(self):
        self.fail()

    def test_search_author(self):
        self.fail()

    def test_search_title(self):
        self.fail()

    def test_update_book_title(self):
        self.fail()

    def test_update_book_author(self):
        self.fail()

class TestCRUD(TestMemoryRepositoryBooks):
    def test_add(self):
        self.book_list.add(Book(3, "DND", "Turcan D."))
        self.assertEqual(len(self.book_list.get_all_books()), 1)

    def test_delete(self):
        self.book_list.add(Book(1, "Cake", "Carp N."))
        self.book_list.delete(1)
        self.assertEqual(len(self.book_list.get_all_books()), 0)

    def test_get(self):
        self.book_list.add(Book(1, "Cake", "Carp N."))
        self.assertEqual(self.book_list.get(1).book_id, 1)

    def test_search_title(self):
        self.book_list.add(Book(1, "Cake", "Carp N."))
        self.book_list.add(Book(2, "Dragon", "Amy S."))
        self.book_list.add(Book(3, "Cavern", "Dan T."))
        found = self.book_list.search_title("Ca")
        self.assertEqual(len(found), 2)
        self.assertEqual(found[0].book_id, 1)
        self.assertEqual(found[1].book_id, 3)

    def test_search_author(self):
        self.book_list.add(Book(1, "Cake", "Carp N."))
        self.book_list.add(Book(2, "Dragon", "Amy S."))
        found = self.book_list.search_author("Am")
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].book_id, 2)

    def test_update_book_title(self):
        self.book_list.add(Book(1, "Cake", "Carp N."))
        book_id = 1
        new_title = "Cavern"

        self.book_list.update_book_title(book_id, new_title)
        self.assertEqual(self.book_list.get(book_id).title, "Cavern")

    def test_update_book_author(self):
        self.book_list.add(Book(1, "Cake", "Carp N."))
        book_id = 1
        new_author = "Amy S."

        self.book_list.update_book_author(book_id, new_author)
        self.assertEqual(self.book_list.get(book_id).name, "Amy S.")
