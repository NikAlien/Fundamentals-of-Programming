from unittest import TestCase
from board_repo import GomokuBoard


class TestGomokuBoard(TestCase):
    def test_get(self):
        board = GomokuBoard()
        self.assertEqual(board.get(2, 3), ' ')

    def test_move_on_board(self):
        board = GomokuBoard()
        board.move_on_board(2, 3, 'X')
        self.assertEqual(board.get(2, 3), 'X')
