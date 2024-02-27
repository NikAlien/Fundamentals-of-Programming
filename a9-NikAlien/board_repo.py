from texttable import Texttable
from cell_domain import Cell


class GomokuBoard:
    def __init__(self):
        self._data = [[Cell() for i in range(10)] for j in range(10)]

    def get(self, row, col):
        return self._data[row][col].game_piece

    def move_on_board(self, row, col, player):
        self._data[row][col].game_piece = player

    def __str__(self):
        t = Texttable()

        header = ['#']
        for i in range(10):
            header.append(chr(ord('A') + i))

        t.header(header)
        for row in range(10):
            t.add_row([row + 1] + self._data[row])


        return t.draw()


