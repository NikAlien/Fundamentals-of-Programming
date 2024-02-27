import pickle
from datetime import date
from src.domain.rental import Rental
from src.repository.repository_exception import RepositoryException


class MemoryRepositoryRentals:
    def __init__(self):
        self._data = {}

    def add(self, new_rental: Rental):
        if new_rental.rental_id in self._data:
            raise RepositoryException("Rental id already in repo")
        if self.search_book_id(new_rental.book_id) is not None:
            raise RepositoryException("Book is currently rented")

        self._data[new_rental.rental_id] = new_rental

    def get_all_rentals(self):
        return list(self._data.values())

    def get(self, rental_id):
        if rental_id not in self._data:
            return None
        return self._data[rental_id]

    # The whole search
    def search_book_id(self, book_id):
        for rental in self.get_all_rentals():
            if book_id == rental.book_id and rental.returned_date == date(1, 1, 1):
                return rental
        return None

    def update_rental(self, book_id, return_date):
        rental = self.search_book_id(book_id)

        if rental is None:
            raise RepositoryException("Book is not rented")
        if rental.rented_date > return_date:
            raise RepositoryException("Return date must be later than rented date")

        self._data[rental.rental_id].returned_date = return_date


class TextFileRepositoryRentals(MemoryRepositoryRentals):
    def __init__(self, file_name="rentals.txt"):
        super(TextFileRepositoryRentals, self).__init__()

        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        fin = open(self._file_name, "rt")
        lines = fin.readlines()
        fin.close()

        for line in lines:
            rentals_line = line.split(",")

            rent_date = rentals_line[3].split("-")
            rented_date = date(int(rent_date[0]), int(rent_date[1]), int(rent_date[2]))

            return_date = rentals_line[4].strip().split("-")
            returned_date = date(int(return_date[0]), int(return_date[1]), int(return_date[2]))

            new_rental = Rental(rentals_line[0], rentals_line[1], rentals_line[2], rented_date, returned_date)
            super().add(new_rental)

    def _save_file(self):
        fout = open(self._file_name, "wt")

        for rental_line in self.get_all_rentals():
            rental_line = str(rental_line.rental_id) + "," + str(rental_line.book_id) + "," +\
                          str(rental_line.client_id) + "," + str(rental_line.rented_date) + "," + \
                          str(rental_line.returned_date) + "\n"
            fout.write(rental_line)

        fout.close()

    def add(self, new_rental: Rental):
        super().add(new_rental)
        self._save_file()

    def update_rental(self, book_id, return_date):
        super().update_rental(book_id, return_date)
        self._save_file()


class BinaryFileRepositoryRentals(MemoryRepositoryRentals):
    def __init__(self, file_name="rentals.bin"):
        super(BinaryFileRepositoryRentals, self).__init__()

        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        fin = open(self._file_name, "rb")
        rentals = pickle.load(fin)

        for rental_line in rentals:
            super().add(rental_line)
        fin.close()

    def _save_file(self):
        fout = open(self._file_name, "wb")
        pickle.dump(self.get_all_rentals(), fout)
        fout.close()

    def add(self, new_rental: Rental):
        super().add(new_rental)
        self._save_file()

    def update_rental(self, book_id, return_date):
        super().update_rental(book_id, return_date)
        self._save_file()