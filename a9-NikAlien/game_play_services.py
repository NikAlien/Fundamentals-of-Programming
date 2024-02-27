import random

from board_repo import GomokuBoard


class GameServices:
    """
    - check for tie
    - check if computer wins
    - check if player wins
    - player moves
    - check if the cell is free or not to move in else exception
    - computer moves
    """
    def __init__(self, board: GomokuBoard):
        self._board = board
        self._player_move = []
        self._computer_win = []
        self._last_computer_move = []
        self._used_cells = 0

    def player_move(self, row, col):
        """
        - We get player move and put their piece on the board
        - In case of a potential win (player has 3 pieces in a row) we remember in placement for future
        computer moves
        :param row:
        :param col:
        :return: 
        """
        if self._board.get(row, col) != ' ':
            raise Exception("! Occupied cell !")
        self._board.move_on_board(row, col, 'O')
        self._used_cells += 1

        if self.horizontal_check(row, col, 'O') >= 3:
            self._player_move.append([row, col])
        if self.vertical_check(row, col, 'O') >= 3:
            self._player_move.append([row, col])
        if self.left_diagonal_check(row, col, 'O') >= 3:
            self._player_move.append([row, col])
        if self.right_diagonal_check(row, col, 'O') >= 3:
            self._player_move.append([row, col])

    def computer_tactic(self):
        """
        Tactics:
        1. First move is random
        2. In case of a potential win (computer has 4 piece near each other) we remember the position and move for the win
        3. In case the player has yet to win computer moves to win with its existing pieces
        4. In case player is close to win (has 3 pieces near each other) computer moves to stop
        :return:
        """

        if len(self._last_computer_move) == 0 and len(self._player_move) == 0:
            while True:
                row = random.randint(0, 9)
                col = random.randint(0, 9)
                if self._board.get(row, col) == ' ':
                    self._board.move_on_board(row, col, 'X')
                    break
            self._last_computer_move.append([row, col])
            self._used_cells += 1
            return [row, col]

        elif len(self._computer_win) != 0:
            print(self._computer_win)
            move = self.computer_move(self._computer_win, [1, -1], 'X')
            self._board.move_on_board(move[0], move[1], 'X')
            self._last_computer_move.append(move)
            self._computer_win.pop()
            self._used_cells += 1
            return move

        elif len(self._player_move) == 0:
            move = self.computer_move(self._last_computer_move, [1, -1], 'X')
            self._board.move_on_board(move[0], move[1], 'X')
            self._last_computer_move.append(move)
            self._used_cells += 1
            return move

        elif len(self._player_move) != 0:
            move = self.computer_move(self._player_move, [1, -1, 2, -2, 3, -3], 'O')
            self._board.move_on_board(move[0], move[1], 'X')
            self._player_move.pop()
            self._used_cells += 1
            return move


    def computer_move(self, last_move, limits, player):
        """
        - We have the list of coordinates around which the computer will move
        - Its looking for the longest line and puts its piece where there is a free space
        :param last_move: Lists of coordinates around which the computer will put the next piece
        :param limits: how far to look for a free space on the board
        :param player: identity needed to check for the longest line of pieces
        :return: the coordinates where the computer moved
        """
        flag = False
        index = len(last_move) - 1

        while not flag:
            row = last_move[index][0]
            col = last_move[index][1]

            h = self.horizontal_check(row, col, player)
            v = self.vertical_check(row, col, player)
            l = self.left_diagonal_check(row, col, player)
            r = self.right_diagonal_check(row, col, player)

            moves_list = [[self.horizontal_move, h], [self.vertical_move, v], [self.left_diagonal_move, l], [self.right_diagonal_move, r]]
            moves_list = sorted(moves_list, key= lambda x: x[1], reverse= True)

            move = []
            for i in range(4):
                move = moves_list[i][0](row, col, limits)
                if move[0] != row or move[1] != col:
                    flag = True
                    if moves_list[i][1] == 3 and player == 'X':
                        self._computer_win.append(move)
                    break

            if flag is False:
                index -= 1
            else:
                return move

    def horizontal_move(self, row, col, limits):
        """
        Computer makes a move on the horizontal line
        :param row:
        :param col:
        :param limits:
        :return:
        """
        for i in limits:
            if 0 <= col + i < 10 and self._board.get(row, col + i) == ' ':
                col += i
                break
        return [row, col]

    def vertical_move(self, row, col, limits):
        """
        Computer makes a move on the vertical line
        :param row:
        :param col:
        :param limits:
        :return:
        """
        for i in limits:
            if 0 <= row + i < 10 and self._board.get(row + i, col) == ' ':
                row += i
                break
        return [row, col]

    def left_diagonal_move(self, row, col, limits):
        """
        Computer makes a move on the main diagonal (left -> right)
        :param row:
        :param col:
        :param limits:
        :return:
        """
        for i in limits:
            if 0 <= row + i < 10 and 0 <= col + i < 10 and self._board.get(row + i, col + i) == ' ':
                row += i
                col += i
                break
        return [row, col]

    def right_diagonal_move(self, row, col, limits):
        """
        Computer makes a move on the other diagonal (right -> left)
        :param row:
        :param col:
        :param limits:
        :return:
        """
        for i in limits:
            if 0 <= row + i < 10 and 0 <= col - i < 10 and self._board.get(row + i, col - i) == ' ':
                row += i
                col -= i
                break
        return [row, col]

    def check_win(self, row, col, player):
        """
        Checks if there are 5 pieces in a line
        :param row:
        :param col:
        :param player:
        :return: True if there are, else False
        """

        if self.horizontal_check(row, col, player) == 5:
            return True

        if self.vertical_check(row, col, player) == 5:
            return True

        if self.left_diagonal_check(row, col, player) == 5:
            return True

        if self.right_diagonal_check(row, col, player) == 5:
            return True

        return False

    def horizontal_check(self, row, col, player):
        """
        Checks how many pieces there are on the horizontal line
        :param row:
        :param col:
        :param player:
        :return:
        """
        pieces = 0
        i = 0
        while 0 <= col + i < 10 and self._board.get(row, col + i) == player:
            pieces += 1
            i += 1

        i = -1
        while 0 <= col + i < 10 and self._board.get(row, col + i) == player:
            pieces += 1
            i -= 1

        return pieces

    def vertical_check(self, row, col, player):
        """
        Checks how many pieces there are on the vertical line
        :param row:
        :param col:
        :param player:
        :return:
        """
        pieces = 0
        i = 0
        while 0 <= row + i < 10 and self._board.get(row + i, col) == player:
            pieces += 1
            i += 1

        i = -1
        while 0 <= row + i < 10 and self._board.get(row + i, col) == player:
            pieces += 1
            i -= 1

        return pieces

    def left_diagonal_check(self, row, col, player):
        """
        Checks how many pieces there are on the main diagonal (left - right)
        :param row:
        :param col:
        :param player:
        :return:
        """
        pieces = 0
        i = 0
        while 0 <= row + i < 10 and 0 <= col + i < 10 and self._board.get(row + i, col + i) == player:
            pieces += 1
            i += 1

        i = -1
        while 0 <= row + i < 10 and 0 <= col + i < 10 and self._board.get(row + i, col + i) == player:
            pieces += 1
            i -= 1

        return pieces

    def right_diagonal_check(self, row, col, player):
        """
        Checks how many pieces there are on the secondary line (right -> left)
        :param row:
        :param col:
        :param player:
        :return:
        """
        pieces = 0
        i = 0
        while 0 <= row + i < 10 and 0 <= col - i < 10 and self._board.get(row + i, col - i) == player:
            pieces += 1
            i += 1

        i = -1
        while 0 <= row + i < 10 and 0 <= col - i < 10 and self._board.get(row + i, col - i) == player:
            pieces += 1
            i -= 1

        return pieces

    def check_draw_game(self):
        """
        Check if the game is a draw
        :return:
        """
        if self._used_cells == 100:
            return True
        else:
            return False

    def get_data_to_ui(self):
        return self._board