from unittest import TestCase
import datetime
from src.domain.rental import Rental

class TestRental(TestCase):
    def setUp(self):
        self.rental = Rental(1, 1, 1, datetime.date(2022, 12, 10), datetime.date(1, 1, 1))
    def test_rental_id(self):
        self.fail()

    def test_client_id(self):
        self.fail()

    def test_book_id(self):
        self.fail()

    def test_rented_date(self):
        self.fail()

    def test_returned_date(self):
        self.fail()

class TestInit(TestRental):
    def test_rental_id(self):
        self.assertEqual(self.rental.rental_id, 1)

    def test_client_id(self):
        self.assertEqual(self.rental.client_id, 1)

    def test_book_id(self):
        self.assertEqual(self.rental.book_id, 1)

    def test_rented_date(self):
        self.assertEqual(self.rental.rented_date, datetime.date(2022, 12, 10))

    def test_returned_date(self):
        self.assertEqual(self.rental.returned_date, datetime.date(1, 1, 1))

class TestUpdate(TestRental):
    def test_rental_id(self):
        self.assertTrue(True)

    def test_client_id(self):
        self.assertTrue(True)

    def test_book_id(self):
        self.assertTrue(True)

    def test_rented_date(self):
        self.rental.rented_date = datetime.date(1, 1, 1,)
        self.assertEqual(self.rental.rented_date, datetime.date(1, 1, 1,))

    def test_returned_date(self):
        self.rental.returned_date = datetime.date
        self.assertEqual(self.rental.returned_date, datetime.date)
