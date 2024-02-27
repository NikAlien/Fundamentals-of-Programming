from unittest import TestCase
from src.domain.client import Client


class TestClient(TestCase):
    def setUp(self):
        self.client = Client(1, "Turcan Dan")

    def test_client_id(self):
        self.fail()

    def test_name(self):
        self.fail()

class TestInit(TestClient):
    def test_client_id(self):
        self.assertEqual(self.client.client_id, 1)

    def test_name(self):
        self.assertEqual(self.client.name, "Turcan Dan")

class TestUpdate(TestClient):
    def test_client_id(self):
        self.assertTrue(True)

    def test_name(self):
        self.client.name = "Carp Nik"
        self.assertEqual(self.client.name, "Carp Nik")
