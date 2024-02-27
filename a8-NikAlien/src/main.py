from src.domain.book_validator import BookValidator
from src.domain.client_validator import ClientValidator
from src.domain.rental_validator import RentalValidator
from src.repository.repository_client import MemoryRepositoryClient, TextFileRepositoryClients, \
    BinaryFileRepositoryClients
from src.repository.repository_rental import MemoryRepositoryRentals, TextFileRepositoryRentals, \
    BinaryFileRepositoryRentals
from src.services.book_services import BookServices
from src.services.client_services import ClientServices
from src.services.generate_repos import RepositoryBooks, RepositoryClients, RepositoryRentals
from src.services.rental_services import RentalServices
from src.repository.repository_books import TextFileRepositoryBooks, BinaryFileRepositoryBooks, MemoryRepositoryBooks
from src.ui.ui import UI



if __name__ == "__main__":
    book_list = MemoryRepositoryBooks()
    book_list = RepositoryBooks().generate_repo_books(book_list)
    validator_book = BookValidator()

    book_txt = TextFileRepositoryBooks()
    book_bin = BinaryFileRepositoryBooks()


    client_list = MemoryRepositoryClient()
    client_list = RepositoryClients().generate_repo_client(client_list)
    validator_client = ClientValidator()

    client_txt = TextFileRepositoryClients()
    client_bin = BinaryFileRepositoryClients()


    rental_list = MemoryRepositoryRentals()
    rental_list = RepositoryRentals().generate_repo_rental(rental_list)
    validator_rental = RentalValidator()

    rental_txt = TextFileRepositoryRentals()
    rental_bin = BinaryFileRepositoryRentals()

    services_book = BookServices(book_list, validator_book)
    services_client = ClientServices(client_list, validator_client)
    services_rental = RentalServices(rental_list, book_list, client_list, validator_rental)
    ui = UI(services_book, services_client, services_rental)

    ui.start()
