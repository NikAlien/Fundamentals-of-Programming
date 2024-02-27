class Book:
    def __init__(self, book_id, title, name):
        self.__book_id = book_id
        self.__title = title
        self.__name = name

    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __str__(self):
        return f"#{self.__book_id} „{self.__title}” by {self.__name}"