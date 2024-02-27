from unittest import TestCase
from src.board_repo import GameBoard
from src.play_services import GameServices


class TestGameServices(TestCase):
    def setUp(self):
        self.board = GameBoard()
        self.services = GameServices(self.board)
    def test_computer_move(self):
        moves = self.services.computer_move()
        self.assertEqual(len(moves), 3)

    def test_computer_move_random(self):
        moves = self.services.computer_move_random()
        self.assertEqual(len(moves), 3)

    def test_computer_moves_to_stop(self):
        board = GameBoard()
        self.services = GameServices(board)
        self.services.player_move(2, 2, 'x')
        self.services.player_move(2, 3, 'x')
        self.services.player_move(2, 4, 'x')
        self.services.player_move(2, 5, 'x')
        moves = self.services.computer_moves_to_stop()
        self.assertEqual(len(moves), 3)

    def test_move_md(self):
        board = GameBoard()
        self.services = GameServices(board)
        self.services.player_move(2, 2, 'x')
        self.services.player_move(3, 3, 'x')
        self.services.player_move(4, 4, 'x')
        self.services.player_move(5, 5, 'x')
        moves = self.services.move_MD(2,2)
        self.assertEqual(len(moves), 2)

    def test_move_sd(self):
        board = GameBoard()
        self.services = GameServices(board)
        self.services.player_move(2, 2, 'x')
        self.services.player_move(3, 3, 'x')
        self.services.player_move(4, 4, 'x')
        self.services.player_move(5, 5, 'x')
        print(board)
        moves = self.services.move_SD(2,2)
        self.assertEqual(len(moves), 2)

    def test_move_h(self):
        board = GameBoard()
        self.services = GameServices(board)
        self.services.player_move(2, 2, 'x')
        self.services.player_move(2, 3, 'x')
        self.services.player_move(2, 4, 'x')
        self.services.player_move(2, 5, 'x')
        print(board)
        moves = self.services.move_H(1, 4)
        self.assertEqual(len(moves), 2)

    def test_move_v(self):
        board = GameBoard()
        self.services = GameServices(board)
        self.services.player_move(2, 2, 'x')
        self.services.player_move(3, 2, 'x')
        self.services.player_move(4, 2, 'x')
        self.services.player_move(5, 2, 'x')
        print(board)
        moves = self.services.move_H(4, 1)
        self.assertEqual(len(moves), 2)


    def test_check_main_diagonal(self):
        board = GameBoard()
        self.services = GameServices(board)
        self.services.player_move(2, 2, 'x')
        self.services.player_move(3, 3, 'x')
        self.services.player_move(4, 4, 'x')
        self.services.player_move(5, 5, 'x')
        self.assertEqual(self.services.check_main_diagonal(4,4, 'x'), 4)

    def test_check_second_diagonal(self):
        board = GameBoard()
        self.services = GameServices(board)
        self.services.player_move(2, 2, 'x')
        self.services.player_move(3, 3, 'x')
        self.services.player_move(4, 4, 'x')
        self.services.player_move(5, 5, 'x')
        self.assertEqual(self.services.check_second_diagonal(4, 4, 'x'), 1)

    def test_check_horizontal(self):
        board = GameBoard()
        self.services = GameServices(board)
        self.services.player_move(2, 2, 'x')
        self.services.player_move(2, 3, 'x')
        self.services.player_move(2, 4, 'x')
        self.assertEqual(self.services.check_horizontal(1, 3, 'x'), 3)

    def test_check_vertical(self):
        board = GameBoard()
        self.services = GameServices(board)
        self.services.player_move(2, 2, 'x')
        self.services.player_move(2, 3, 'x')
        self.services.player_move(2, 4, 'x')
        self.assertEqual(self.services.check_vertical(1, 3, 'x'), 1)
