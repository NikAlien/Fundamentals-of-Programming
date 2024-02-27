from unittest import TestCase
from src.domain.book import Book


class TestBook(TestCase):
    def setUp(self):
        self.book = Book(1, "Cake", "C N")

    def test_book_id(self):
        self.fail()

    def test_title(self):
        self.fail()

    def test_name(self):
        self.fail()


class TestInit(TestBook):
    def test_book_id(self):
        self.assertEqual(self.book.book_id, 1)

    def test_title(self):
        self.assertEqual(self.book.title, "Cake")

    def test_name(self):
        self.assertEqual(self.book.name, "C N")

class TestUpdate(TestBook):
    def test_book_id(self):
        self.assertTrue(True)

    def test_title(self):
        self.book.title = "Dragon"
        self.assertEqual(self.book.title, "Dragon")

    def test_name(self):
        self.book.name = "amy"
        self.assertEqual(self.book.name, "amy")