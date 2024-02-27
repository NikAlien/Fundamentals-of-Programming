from unittest import TestCase

from src.domain.client_validator import ClientValidator
from src.repository.repository_client import MemoryRepositoryClient
from src.services.client_services import ClientServices


class TestClientServices(TestCase):
    def setUp(self):
        self.client_list = MemoryRepositoryClient()
        self.serv = ClientServices(self.client_list, ClientValidator())
    def test_add_client(self):
        self.fail()

    def test_delete_client(self):
        self.fail()

    def test_update_name(self):
        self.fail()

    def test_search_by_name(self):
        self.fail()

    def test_search_by_id(self):
        self.fail()

class TestClientService(TestClientServices):
    def test_add_client(self):
        self.serv.add_client(1, "Carp Nik")
        self.assertEqual(len(self.client_list.get_all_clients()), 1)

    def test_delete_client(self):
        self.serv.add_client(1, "Carp Nik")
        self.serv.add_client(2, "Sor Amy")
        self.serv.delete_client(2)
        self.assertEqual(len(self.client_list.get_all_clients()), 1)

    def test_search_by_id(self):
        self.serv.add_client(1, "Carp Nik")
        self.serv.add_client(2, "Sor Amy")
        client = self.serv.search_by_id(1)
        self.assertEqual(client.name, "Carp Nik")

    def test_search_by_name(self):
        self.serv.add_client(1, "Carp Nik")
        self.serv.add_client(2, "Sor Amy")
        client = self.serv.search_by_name("a")
        self.assertEqual(len(client), 2)

    def test_update_name(self):
        self.serv.add_client(2, "Sor Amy")
        self.serv.update_name(2, "Dan")
        self.assertEqual(self.client_list.get(2).name, "Dan")


