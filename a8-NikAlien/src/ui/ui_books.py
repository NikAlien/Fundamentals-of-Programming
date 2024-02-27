from src.services.book_services import BookServices

class UIBooks:
    def __init__(self, book_serv: BookServices):

        self._commands_books = {'+': self.add_book,
                                '-': self.delete_book,
                                'up': self.update_book,
                                'd': self.display_book_list,
                                's': self.search_books}
        self._book_serv = book_serv

    def print_menu_books(self):
        print("\nChoose your next command: ")
        print("  add --> +")
        print("  delete --> -")
        print("  update --> up")
        print("  display list --> d")
        print("  search --> s")
        print("  back to main menu --> x")

    def book_work(self):
        while True:
            self.print_menu_books()
            _choice = input("\nCommand: ")

            if _choice == "x":
                break

            elif _choice not in self._commands_books:
                print("Unidentifiable command")

            else:
                try:
                    self._commands_books[_choice]()
                except Exception as ve:
                    print("Error: " + str(ve))

    def add_book(self):
        book_id = int(input("Book id --> "))
        title = input("Book title --> ")
        author = input("Author --> ")

        self._book_serv.add_book(book_id, title, author)

    def delete_book(self):
        book_id = int(input("Give the id of the book you want to delete: "))
        self._book_serv.delete_book(book_id)

    def update_book(self):
        book_id = int(input("Give the id of the book you want to update: "))

        while True:
            answer = input("You want to update the title or the author? ")

            if answer.lower() == "title":
                title = input("New title --> ")
                self._book_serv.update_title(book_id, title)
                break

            elif answer.lower() == "author":
                author = input("New author --> ")
                self._book_serv.update_author(book_id, author)
                break

            else:
                print("Unidentifiable command")

    def display_book_list(self):
        book_list = self._book_serv.sort_book_list()
        for book in book_list:
            print(book)

    def search_books(self):
        while True:
            answer = input("Are you searching by id, title or author? ")

            if answer.lower() == "id":
                book_id = input("Search by id --> ")
                print("\n")
                print(self._book_serv.search_by_id(book_id))
                break

            elif answer.lower() == "title":
                title = input("Search by title --> ")
                found_list = self._book_serv.search_by_title(title)

                print("\n")
                for book in found_list:
                    print(book)
                break

            elif answer.lower() == "author":
                author = input("Search by author --> ")
                found_list = self._book_serv.search_by_author(author)

                print("\n")
                for book in found_list:
                    print(book)
                break

            else:
                print("Unidentifiable command")