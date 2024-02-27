class Player:
    def __init__(self, player_id: int, name: str, player_strength: int):
        self.__id = player_id
        self.__name = name
        self.__strength = player_strength

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, new_strength):
        self.__strength = new_strength

    def __str__(self):
        return f"#{self.__id}  {self.__name} - {self.__strength}"
