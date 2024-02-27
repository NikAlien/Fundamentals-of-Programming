from unittest import TestCase

from cell_domain import Cell


class TestCell(TestCase):
    def test_game_piece(self):
        cell = Cell()
        self.assertEqual(cell.game_piece, ' ')

    def test_game_piece_value(self):
        cell = Cell()
        cell.game_piece = 'X'
        self.assertEqual(cell.game_piece, 'X')
