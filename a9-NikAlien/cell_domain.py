class Cell:
    """
    'X' - computer
    'O' - human
    ' ' - nobody
    """
    def __init__(self):
        self._game_piece = ' '

    @property
    def game_piece(self):
        return self._game_piece

    @game_piece.setter
    def game_piece(self, value):
        self._game_piece = value

    def __str__(self):
        return self._game_piece

