import pickle
from src.domain.client import Client
from src.repository.repository_exception import RepositoryException


class MemoryRepositoryClient:
    def __init__(self):
        self.client_list = {}

    def add(self, new_client: Client):
        if new_client.client_id in self.client_list:
            raise RepositoryException("Client already in repo")
        self.client_list[new_client.client_id] = new_client

    def delete(self, client_id):
        if client_id not in self.client_list:
            raise RepositoryException("Client not in repo")
        del self.client_list[client_id]

    def get_all_clients(self):
        return list(self.client_list.values())

    def get(self, client_id):
        if client_id not in self.client_list:
            return None
        return self.client_list[client_id]

    # The whole search
    def search_name(self, name: str):
        found_clients = []

        for client in self.get_all_clients():
            if name.lower() in client.name.lower():
                found_clients.append(client)

        return found_clients

    def update_client_name(self, client_id, client_name):
        if client_id not in self.client_list:
            raise RepositoryException("Client id not in repo")
        self.client_list[client_id].name = client_name


class TextFileRepositoryClients(MemoryRepositoryClient):
    def __init__(self, file_name="client.txt"):
        super(TextFileRepositoryClients, self).__init__()

        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        fin = open(self._file_name, "rt")
        lines = fin.readlines()
        fin.close()

        for line in lines:
            client_line = line.split(",")
            new_client = Client(int(client_line[0]), client_line[1].strip())
            super().add(new_client)

    def _save_file(self):
        fout = open(self._file_name, "wt")

        for client_line in self.get_all_clients():
            client_line = str(client_line.client_id) + "," + client_line.name +  "\n"
            fout.write(client_line)

        fout.close()

    def add(self, new_client: Client):
        super().add(new_client)
        self._save_file()

    def delete(self, client_id):
        super().delete(client_id)
        self._save_file()

    def update_client_name(self, client_id, client_name):
        super().update_client_name(client_id, client_name)
        self._save_file()


class BinaryFileRepositoryClients(MemoryRepositoryClient):
    def __init__(self, file_name="client.bin"):
        super(BinaryFileRepositoryClients, self).__init__()

        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        fin = open(self._file_name, "rb")
        clients = pickle.load(fin)

        for client_line in clients:
            super().add(client_line)
        fin.close()

    def _save_file(self):
        fout = open(self._file_name, "wb")
        pickle.dump(self.get_all_clients(), fout)
        fout.close()

    def add(self, new_client: Client):
        super().add(new_client)
        self._save_file()

    def delete(self, client_id):
        super().delete(client_id)
        self._save_file()

    def update_client_name(self, client_id, client_name):
        super().update_client_name(client_id, client_name)
        self._save_file()
