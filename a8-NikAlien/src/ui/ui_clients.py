from src.services.client_services import ClientServices

class UIClients:
    def __init__(self, client_serv: ClientServices):
        self._commands_clients = {'+': self.add_client,
                                  '-': self.delete_client,
                                  'up': self.update_client,
                                  'd': self.display_client_list,
                                  's': self.search_client}
        self._client_serv = client_serv

    def print_menu_clients(self):
        print("\nChoose your next command: ")
        print("  add --> +")
        print("  delete --> -")
        print("  update --> up")
        print("  display list --> d")
        print("  search --> s")
        print("  back to main menu --> x")

    def client_work(self):
        while True:
            self.print_menu_clients()
            _choice = input("\nCommand: ")

            if _choice == "x":
                break

            elif _choice not in self._commands_clients:
                print("Unidentifiable command")

            else:
                try:
                    self._commands_clients[_choice]()
                except Exception as ve:
                    print("Error: " + str(ve))

    def add_client(self):
        client_id = int(input("Client id --> "))
        name = input("Client name --> ")

        self._client_serv.add_client(client_id, name)

    def delete_client(self):
        client_id = int(input("Give the id of the client you want to delete: "))
        self._client_serv.delete_client(client_id)

    def update_client(self):
        client_id = int(input("Give the id of the client you want to update: "))
        name = input("New name --> ")

        self._client_serv.update_name(client_id, name)

    def display_client_list(self):
        client_list = self._client_serv.sort_client_list()
        for client in client_list:
            print(client)

    def search_client(self):
        while True:
            answer = input("Are you searching by id or name? ")

            if answer.lower() == "id":
                client_id = int(input("Search by id --> "))

                print("\n")
                print(self._client_serv.search_by_id(client_id))
                break

            elif answer.lower() == "name":
                name = input("Search by name --> ")
                found_list = self._client_serv.search_by_name(name)

                print("\n")
                for client in found_list:
                    print(client)
                break

            else:
                print("Unidentifiable command")