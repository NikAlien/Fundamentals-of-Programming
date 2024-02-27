from datetime import date
from src.domain.validatorException import ValidatorException
from src.domain.rental import Rental


class RentalValidator:
    def __init__(self):
        self._errors = ""

    def rental_validator(self, rental):
        if not isinstance(rental, Rental):
            raise TypeError("Can only validate Rental objects")
        self._errors = []
        if rental.rental_id is None:
            self._errors.append("Rental must have an id")
        if rental.book_id is None:
            self._errors.append("There must be a book that was rented")
        if rental.client_id is None:
            self._errors.append("There must be a client that rented")
        if rental.rented_date > date.today():
            self._errors.append("Rented date is invalid, this is a future date")

        if len(self._errors) > 0:
            raise ValidatorException(self._errors)
        return True
