from src.services.book_services import BookServices
from src.services.client_services import ClientServices
from src.services.rental_services import RentalServices
from src.ui.ui_books import UIBooks
from src.ui.ui_clients import UIClients
from src.ui.ui_rental import UIRentals


class UI:
    def __init__(self, book_serv: BookServices, client_serv: ClientServices, rental_serv: RentalServices):
        self._commands_general = {'books': self.book_work, 'clients': self.client_work, 'rentals': self.rental_work, 'statistics': self.statistic_work}

        # self._commands_statistic

        self._book_serv = book_serv
        self._client_serv = client_serv
        self._rental_serv = rental_serv

    def print_menu_general(self):
        """
        Print the menu
        """
        print("\nChoose your destination of work: ")
        print("  --> books")
        print("  --> clients")
        print("  --> rentals")
        print("  --> exit")

    def book_work(self):
        ui_books = UIBooks(self._book_serv)
        ui_books.book_work()

    def client_work(self):
        ui_client = UIClients(self._client_serv)
        ui_client.client_work()

    def rental_work(self):
        ui_rental = UIRentals(self._rental_serv)
        ui_rental.rental_work()

    def statistic_work(self):
        pass

    def start(self):

        while True:
            self.print_menu_general()
            _choice = input("\nCommand: ")

            if _choice == "exit":
                return

            if _choice not in self._commands_general:
                print("Unidentifiable command")

            else:
                self._commands_general[_choice]()

