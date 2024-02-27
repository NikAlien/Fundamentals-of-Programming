from unittest import TestCase
from board_repo import GomokuBoard
from game_play_services import GameServices


class TestGameServices(TestCase):

    def test_player_move(self):
        board = GomokuBoard()
        services = GameServices(board)
        services.player_move(1, 2)
        self.assertEqual(board.get(1, 2), 'O')

    def test_computer_tactic(self):
        board = GomokuBoard()
        services = GameServices(board)
        move = services.computer_tactic()
        self.assertEqual(len(move), 2)

        move = services.computer_tactic()
        self.assertEqual(len(move), 2)

        move = services.computer_tactic()
        self.assertEqual(len(move), 2)

        move = services.computer_tactic()
        self.assertEqual(len(move), 2)

        move = services.computer_tactic()
        self.assertEqual(len(move), 2)


    def test_computer_move(self):
        board = GomokuBoard()
        services = GameServices(board)
        move = services.computer_tactic()
        self.assertEqual(len(move), 2)

        move2 = services.computer_tactic()
        self.assertEqual(len(move2), 2)
        self.assertNotEqual(move, move2)

    def test_horizontal_move(self):
        board = GomokuBoard()
        services = GameServices(board)
        move = services.horizontal_move(2, 3, [1])
        self.assertEqual(move, [2, 4])

    def test_vertical_move(self):
        board = GomokuBoard()
        services = GameServices(board)
        move = services.vertical_move(2, 3, [1])
        self.assertEqual(move, [3, 3])

    def test_left_diagonal_move(self):
        board = GomokuBoard()
        services = GameServices(board)
        move = services.left_diagonal_move(2, 3, [1])
        self.assertEqual(move, [3, 4])

    def test_right_diagonal_move(self):
        board = GomokuBoard()
        services = GameServices(board)
        moves = services.right_diagonal_move(4, 4, [1])
        self.assertEqual(moves, [5, 3])

    def test_check_win(self):
        board = GomokuBoard()
        services = GameServices(board)
        services.player_move(1, 2)
        flag = services.check_win(1, 2, 'O')
        self.assertEqual(flag, False)

        services.player_move(1, 3)
        services.player_move(1, 4)
        services.player_move(1, 5)
        services.player_move(1, 6)
        flag = services.check_win(1, 6, 'O')
        self.assertEqual(flag, True)

    def test_horizontal_check(self):
        board = GomokuBoard()
        services = GameServices(board)
        services.player_move(1, 2)
        services.player_move(1, 3)
        services.player_move(1, 4)
        flag = services.horizontal_check(1, 3, 'O')
        self.assertEqual(flag, 3)

    def test_vertical_check(self):
        board = GomokuBoard()
        services = GameServices(board)
        services.player_move(1, 2)
        services.player_move(2, 2)
        services.player_move(3, 2)
        flag = services.vertical_check(2, 2, 'O')
        self.assertEqual(flag, 3)

    def test_left_diagonal_check(self):
        board = GomokuBoard()
        services = GameServices(board)
        services.player_move(1, 1)
        services.player_move(2, 2)
        flag = services.left_diagonal_check(2, 2, 'O')
        self.assertEqual(flag, 2)

    def test_right_diagonal_check(self):
        board = GomokuBoard()
        services = GameServices(board)
        services.player_move(5, 7)
        services.player_move(6, 6)
        services.player_move(7, 5)
        flag = services.right_diagonal_check(7, 5, 'O')
        self.assertEqual(flag, 3)

    def test_check_draw_game(self):
        board = GomokuBoard()
        services = GameServices(board)
        services.player_move(5, 7)
        services.computer_tactic()
        services.player_move(6, 6)
        services.computer_tactic()
        services.player_move(6, 5)
        flag = services.check_draw_game()
        self.assertEqual(flag, False)
