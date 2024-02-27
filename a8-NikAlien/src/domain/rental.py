from datetime import date


class Rental:
    def __init__(self, rental_id, book_id, client_id, rented_date: date, returned_date: date):
        self.__rental_id = rental_id
        self.__client_id = client_id
        self.__book_id = book_id
        self.__rented_date = rented_date
        self.__returned_date = returned_date

    @property
    def rental_id(self):
        return self.__rental_id

    @property
    def client_id(self):
        return self.__client_id

    @property
    def book_id(self):
        return self.__book_id

    @property
    def rented_date(self):
        return self.__rented_date

    @rented_date.setter
    def rented_date(self, new_date):
        self.__rented_date = new_date

    @property
    def returned_date(self):
        return self.__returned_date

    @returned_date.setter
    def returned_date(self, new_date: date):
        self.__returned_date = new_date

    def __len__(self):
        if self.__returned_date != date(1, 1, 1):
            return (self.__returned_date - self.__rented_date).days + 1

        today = date.today()
        return (today - self.__rented_date).days + 1

    def __str__(self):
        rental_str = f"Rental #{self.__rental_id} information:\n   " \
                   f"Book #{self.__book_id}\n   Client #{self.__client_id}\n" + "   Rented date: " \
                + str(self.__rented_date)

        if self.__returned_date == date(1, 1, 1):
            rental_str  += "\n   Returned date: -"

        else:
            rental_str += "\n   Returned date: " + str(self.__returned_date)

        return rental_str