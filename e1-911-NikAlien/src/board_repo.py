from texttable import Texttable
from src.cell_domain import Cell

class GameBoard:
    def __init__(self):
        self._board = [[Cell() for i in range(6)] for j in range(6)]

    def __str__(self):
        t = Texttable()

        for row in range(6):
            t.add_row(self._board[row])

        return t.draw()

    def place_element(self, row, col, element):
        if self._board[row][col].player != ' ':
            raise Exception("Board cell is occupied, try again")
        self._board[row][col].player = element

    def get_element(self, row, col):
        return self._board[row][col].player
