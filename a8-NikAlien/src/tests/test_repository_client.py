from unittest import TestCase

from src.domain.client import Client
from src.repository.repository_client import MemoryRepositoryClient


class TestMemoryRepositoryClient(TestCase):
    def setUp(self):
        self.client_list = MemoryRepositoryClient()
    def test_add(self):
        self.fail()

    def test_delete(self):
        self.fail()

    def test_get(self):
        self.fail()

    def test_search_name(self):
        self.fail()

    def test_update_client(self):
        self.fail()

class TestCRUD(TestMemoryRepositoryClient):
    def test_add(self):
        self.client_list.add(Client(1, "Carp Nik"))
        self.assertEqual(len(self.client_list.get_all_clients()), 1)

    def test_get(self):
        self.client_list.add(Client(1, "Carp Nik"))
        self.assertEqual(self.client_list.get(1).client_id, 1)

    def test_delete(self):
        self.client_list.add(Client(1, "Carp Nik"))
        self.client_list.delete(1)
        self.assertEqual(len(self.client_list.get_all_clients()), 0)

    def test_search_name(self):
        self.client_list.add(Client(1, "Carp Nik"))
        self.client_list.add(Client(2, "Turcan Dan"))
        found = self.client_list.search_name("Da")
        self.assertEqual(found[0].client_id, 2)

    def test_update_client(self):
        self.client_list.add(Client(1, "Carp Nik"))
        self.client_list.update_client_name(1, "Turcan Dan")
        self.assertEqual(self.client_list.get(1).name, "Turcan Dan")
