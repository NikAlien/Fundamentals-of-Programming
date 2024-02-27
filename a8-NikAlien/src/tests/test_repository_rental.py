from datetime import date
from unittest import TestCase
from src.domain.rental import Rental
from src.repository.repository_rental import MemoryRepositoryRentals


class TestMemoryRepositoryRentals(TestCase):
    def setUp(self):
        self.rental_list = MemoryRepositoryRentals()
    def test_add(self):
        self.fail()

    def test_search_book_id(self):
        self.fail()

    def test_update_rental(self):
        self.fail()

class TestCRUD(TestMemoryRepositoryRentals):
    def test_add(self):
        self.rental_list.add(Rental(1, 2, 5, date(2022, 12, 5), date(2022, 12, 7)))
        self.assertEqual(len(self.rental_list.get_all_rentals()), 1)

    def test_update_rental(self):
        self.rental_list.add(Rental(1, 2, 5, date(2022, 12, 5), date(1, 1, 1)))
        self.rental_list.update_rental(2, date(2022, 12, 9))
        self.assertEqual(self.rental_list.get(1).returned_date, date(2022, 12, 9))

    def test_search_book_id(self):
        self.rental_list.add(Rental(1, 2, 5, date(2022, 12, 5), date(1, 1, 1)))
        rental = self.rental_list.search_book_id(2)
        self.assertEqual(rental.rental_id, 1)