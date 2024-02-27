from datetime import date
from src.domain.book import Book
from src.domain.client import Client
from src.domain.rental import Rental
from src.repository.repository_books import MemoryRepositoryBooks
from src.repository.repository_client import MemoryRepositoryClient
from src.repository.repository_rental import MemoryRepositoryRentals


class RepositoryBooks:
    def generate_repo_books(self,  book_list: MemoryRepositoryBooks):

        book_list.add(Book(1, "Little Women", "Louisa May Alcotta"))
        book_list.add(Book(2, "Pride and Prejudice", "Jane Austen"))
        book_list.add(Book(3, "To Kill a Mockingbird ", "Harper Lee"))
        book_list.add(Book(4, "The Great Gatsby", "Scott Fitzgerald"))
        book_list.add(Book(5, "Crime and Punishment", "Fyodor Dostoevsky"))
        book_list.add(Book(6, "The Secret History", "Donna Tartt"))
        book_list.add(Book(7, "Persuasion", "Jane Austen"))
        book_list.add(Book(8, "Moby-Dick", "Herman Melville"))
        book_list.add(Book(9, "Nineteen Eighty-Four", "George Orwell"))
        book_list.add(Book(10, "Dracula", "Bram Stoker"))
        book_list.add(Book(11, "Great Expectations ", "Charles Dickens"))
        book_list.add(Book(12, "The Brothers Karamazov ", "Fyodor Dostoyevsky"))
        book_list.add(Book(13, "A Tale of Two Cities", "Charles Dickens"))
        book_list.add(Book(14, "Anna Karenina", "Leo Tolstoy"))
        book_list.add(Book(15, "Orlando", "Virginia Woolf"))
        book_list.add(Book(16, "War and Peace", "Leo Tolstoy"))
        book_list.add(Book(17, "Bleak House", "Charles Dickens"))
        book_list.add(Book(18, "Silas Marner", "George Eliot"))
        book_list.add(Book(19, "Mrs Dalloway ", "Virginia Woolf"))
        book_list.add(Book(20, "Little Women", "Louisa May Alcott"))

        return book_list



class RepositoryClients:
    def generate_repo_client(self, client_list: MemoryRepositoryClient):

        client_list.add(Client(1, "Carp Nik"))
        client_list.add(Client(2, "Silva Elian"))
        client_list.add(Client(3, "Gillian Arnold"))
        client_list.add(Client(4, "Milton Luna"))
        client_list.add(Client(5, "Singh Haley"))
        client_list.add(Client(6, "Rivas Elsa"))
        client_list.add(Client(7, "Lamb Orion"))
        client_list.add(Client(8, "Hahn Terry"))
        client_list.add(Client(9, "Schwartz Danna"))
        client_list.add(Client(10, "Summer Lara"))
        client_list.add(Client(11, "Camron Lin"))
        client_list.add(Client(12, "Mendez Nathan"))
        client_list.add(Client(13, "Hale John"))
        client_list.add(Client(14, "Perla Kim"))
        client_list.add(Client(15, "Alvarado Veronica"))
        client_list.add(Client(16, "Garcia Maximus"))
        client_list.add(Client(17, "Harper Eve"))
        client_list.add(Client(18, "Floyd Emma"))
        client_list.add(Client(19, "Hudson Jared"))
        client_list.add(Client(20, "Roselyn Small"))

        return client_list


class RepositoryRentals:
    def generate_repo_rental(self, rental_list: MemoryRepositoryRentals):

        rental_list.add(Rental(1, 2, 5, date(2022, 12, 5), date(2022, 12, 7)))
        rental_list.add(Rental(2, 3, 7, date(2022, 12, 5), date(1, 1, 1)))
        rental_list.add(Rental(3, 15, 10, date(2022, 12, 5), date(2022, 12, 8)))
        rental_list.add(Rental(4, 5, 5, date(2022, 12, 7), date(2022, 12, 9)))
        rental_list.add(Rental(5, 17, 15, date(2022, 12, 7), date(1, 1, 1)))
        rental_list.add(Rental(6, 20, 20, date(2022, 12, 7), date(1, 1, 1)))
        rental_list.add(Rental(7, 13, 8, date(2022, 12, 7), date(1, 1, 1)))
        rental_list.add(Rental(8, 10, 8, date(2022, 12, 7), date(1, 1, 1)))
        rental_list.add(Rental(9, 9, 3, date(2022, 12, 7), date(2022, 12, 8)))
        rental_list.add(Rental(10, 5, 3, date(2022, 12, 8), date(2022, 12, 9)))
        rental_list.add(Rental(11, 19, 2, date(2022, 12, 8), date(1, 1, 1)))
        rental_list.add(Rental(12, 2, 12, date(2022, 12, 8), date(2022, 12, 10)))
        rental_list.add(Rental(13, 5, 5, date(2022, 12, 9), date(1, 1, 1)))
        rental_list.add(Rental(14, 1, 5, date(2022, 12, 9), date(1, 1, 1)))
        rental_list.add(Rental(15, 7, 5, date(2022, 12, 9), date(1, 1, 1)))
        rental_list.add(Rental(16, 11, 1, date(2022, 12, 9), date(2022, 12, 13)))
        rental_list.add(Rental(17, 4, 1, date(2022, 12, 9), date(2022, 12, 13)))
        rental_list.add(Rental(18, 4, 8, date(2022, 12, 13), date(1, 1, 1)))
        rental_list.add(Rental(19, 9, 19, date(2022, 12, 14), date(1, 1, 1)))
        rental_list.add(Rental(20, 11, 13, date(2022, 12, 15), date(2022, 12, 17)))

        return rental_list
