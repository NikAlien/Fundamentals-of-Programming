from datetime import date
from src.services.rental_services import RentalServices

class UIRentals:
    def __init__(self, rental_serv: RentalServices):
        self._commands_rentals = {'rent': self.rent_book,
                                  'return': self.return_book,
                                  'd': self.display_rental,
                                  'books': self.most_rented_books,
                                  'clients': self.most_active_clients,
                                  'authors': self.most_rented_authors}
        self._rental_serv = rental_serv

    def print_menu_rental(self):
        print("\nChoose your next command: ")
        print("  rent a book --> rent")
        print("  return a book --> return")
        print("  display rentals --> d")

        print("\nView statistics: ")
        print("  most rented books --> books")
        print("  most active clients --> clients")
        print("  most rented authors --> authors")

        print("\nBack to main menu --> x")

    def rental_work(self):
        while True:
            self.print_menu_rental()
            _choice = input("\nCommand: ")

            if  _choice == "x":
                break

            elif _choice not in self._commands_rentals:
                print("Unidentifiable command")

            else:
                try:
                    self._commands_rentals[_choice]()
                except Exception as ve:
                    print("Error: " + str(ve))

    def rent_book(self):
        book_id = int(input("Id of the rented book --> "))
        client_id = int(input("Id of the client --> "))
        rented_date = input("Rented date --> ")

        rent_date = rented_date.split("-")
        try:
            rented_date = date(int(rent_date[0]), int(rent_date[1]), int(rent_date[2]))
        except Exception:
            raise Exception("Invalid date input, try format: year-month-day")

        self._rental_serv.add_rental(book_id, client_id, rented_date)

    def return_book(self):
        book_id = int(input("Id of the returned book --> "))
        return_date = input("Return date --> ")

        return_date = return_date.split("-")
        try:
            returned_date = date(int(return_date[0]), int(return_date[1]), int(return_date[2]))
            print(str(returned_date))
        except Exception:
            raise Exception("Invalid date input, try format: year-month-day")

        self._rental_serv.update_rental(book_id, returned_date)

    def display_rental(self):
        rental_list = self._rental_serv.give_ui_rental_list()
        for rental in rental_list:
            print(rental)

    def most_rented_books(self):
        for book in self._rental_serv.most_rented_books():
            print(book)

    def most_active_clients(self):
        for client in self._rental_serv.most_active_clients():
            print(client)

    def most_rented_authors(self):
        for author in self._rental_serv.most_rented_authors():
            print(author)
