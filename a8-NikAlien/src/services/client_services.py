from src.domain.client import Client
from src.services.services_exception import ServicesException

class ClientServices:
    def __init__(self, repository, validator):
        self._client_list = repository
        self._validator = validator

    def add_client(self, client_id, name):
        """
        Add a new object of class Client to the repo
        :param client_id:
        :param name:
        :return:
        """
        new_client = Client(client_id, name)
        self._validator.client_validator(new_client)

        self._client_list.add(new_client)

    def delete_client(self, client_id):
        """
        Delete a client with the given id
        :param client_id:
        :return:
        """
        self._client_list.delete(client_id)

    def update_name(self, client_id, name):
        """
        Update the clients name
        :param client_id:
        :param name:
        :return:
        """
        self._client_list.update_client_name(client_id, name)

    def sort_client_list(self):
        """
        Return list with clients sorted ascending according to their ids
        :return:
        """
        clients_list = sorted(self._client_list.get_all_clients(), key=lambda x: x.client_id)
        return clients_list

    def search_by_name(self, name):
        """
        Search client with a give substring
        :param name:
        :return:
        """
        found_clients = self._client_list.search_name(name)
        if len(found_clients) == 0:
             raise ServicesException("No results found")
        return found_clients

    def search_by_id(self, client_id):
        """
        Search client by its id
        :param client_id:
        :return:
        """
        return self._client_list.get(client_id)