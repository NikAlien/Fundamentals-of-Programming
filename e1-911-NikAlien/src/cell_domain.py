class Cell:
    def __init__(self):
        self.__player = ' '

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, element):
        self.__player = element

    def __str__(self):
        return self.__player
