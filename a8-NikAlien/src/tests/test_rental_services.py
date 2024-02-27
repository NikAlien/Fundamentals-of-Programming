import select
from datetime import date
from unittest import TestCase

from src.domain.rental_validator import RentalValidator
from src.repository.repository_books import MemoryRepositoryBooks
from src.repository.repository_client import MemoryRepositoryClient
from src.repository.repository_rental import MemoryRepositoryRentals
from src.services.generate_repos import RepositoryBooks, RepositoryClients
from src.services.rental_services import RentalServices


class TestRentalServices(TestCase):
    def setUp(self):
        self.rental_list = MemoryRepositoryRentals()
        self.book_list = RepositoryBooks().generate_repo_books(MemoryRepositoryBooks())
        self.client_list = RepositoryClients().generate_repo_client(MemoryRepositoryClient())
        self.serv = RentalServices(self.rental_list, self.book_list, self.client_list, RentalValidator())
    def test_add_rental(self):
        self.fail()

    def test_update_rental(self):
        self.fail()

class TestRentalService(TestRentalServices):
    def test_add_rental(self):
        self.serv.add_rental(2, 5, "2022-12-16")
        self.assertEqual(len(self.rental_list.get_all_rentals()), 1)

    def test_update_rental(self):
        self.serv.add_rental(2, 5, "2022-12-16")
        self.serv.update_rental(2, "2022-12-17")
        self.assertEqual(self.rental_list.get(1).returned_date, date(2022, 12, 17))