from datetime import date
from src.domain.rental import Rental
from src.services.services_exception import ServicesException

class BooksRentalDTO:
    def __init__(self, book, times):
        self._book = book
        self._times = times

    @property
    def times(self):
        return self._times

    @times.setter
    def times(self, new_value):
        self._times = new_value

    def __repr__(self):
        return str(self._book) + "\n   Rented --> " + str(self._times) + " times"

class ActiveClientDTO:
    def __init__(self, client, days):
        self._client = client
        self._days = days

    @property
    def days(self):
        return self._days

    @days.setter
    def days(self, new_value):
        self._days = new_value

    def __repr__(self):
        return str(self._client) + "\n   Active for " + str(self._days) + " days"

class AuthorDTO:
    def __init__(self, name, times):
        self._author = name
        self._times = times

    @property
    def times(self):
        return self._times

    @times.setter
    def times(self, new_value):
        self._times = new_value

    def __repr__(self):
        return str(self._author) + "\n   Rented: " + str(self._times) + " times"


class RentalServices:
    def __init__(self, repository_rental, repository_books, repository_clients, validator):
        self._rental_list = repository_rental
        self._books_list = repository_books
        self._client_list = repository_clients
        self._validator = validator

    def add_rental(self, book_id, client_id, rent_date: date):
        """
        Rent a book that is available and add the date
        :param rent_date:
        :param book_id:
        :param client_id:
        :return:
        """
        if self._books_list.get(book_id) is None:
            raise ServicesException("Book id is invalid")
        if self._client_list.get(client_id) is None:
            raise ServicesException("Client id is invalid")

        if len(self._rental_list.get_all_rentals()) == 0:
            rental_id = 1
        else:
            last_rental = self._rental_list.get_all_rentals().pop()
            rental_id = last_rental.rental_id + 1

        new_rental = Rental(rental_id, book_id, client_id, rent_date, date(1, 1, 1))
        self._validator.rental_validator(new_rental)

        self._rental_list.add(new_rental)

    def update_rental(self, book_id, returned_date: date):
        """
        Return the rented book, update the return date
        :param returned_date:
        :param book_id:
        :return:
        """
        self._rental_list.update_rental(book_id, returned_date)

    def give_ui_rental_list(self):
        return self._rental_list.get_all_rentals()

    def most_rented_books(self):
        """
        Statistics: books sorted descending by times it was rented
        :return:
        """
        rented_dict = {}

        for book in self._books_list.get_all_books():
            book_id = book.book_id
            rented_dict[book_id] = BooksRentalDTO(self._books_list.get(book_id), 0)

        for rental in self._rental_list.get_all_rentals():
            book_id = rental.book_id
            rented_dict[book_id].times += 1


        result = list(rented_dict.values())
        result.sort(key=lambda x: x.times, reverse= True)

        return result

    def most_active_clients(self):
        """
        Statistics: clients sorted descending by days of having books rented
        :return:
        """
        client_dict = {}

        for client in self._client_list.get_all_clients():
            client_id = client.client_id
            client_dict[client_id] = ActiveClientDTO(self._client_list.get(client_id), 0)

        for rental in self._rental_list.get_all_rentals():
            client_id = rental.client_id
            client_dict[client_id].days += len(rental)

        result = list(client_dict.values())
        result.sort(key=lambda x: x.times, reverse=True)

        return result

    def most_rented_authors(self):
        """
        Statistics: authors sorted descending by times their books were rented
        :return:
        """
        author_dict = {}

        for book in self._books_list.get_all_books():
            author = book.name
            if author not in author_dict:
                author_dict[author] = BooksRentalDTO(self._books_list.get(book.book_id).name, 0)

        for rental in self._rental_list.get_all_rentals():
            author = self._books_list.get(rental.book_id).name
            author_dict[author].times += 1


        result = list(author_dict.values())
        result.sort(key=lambda x: x.times, reverse= True)

        return result