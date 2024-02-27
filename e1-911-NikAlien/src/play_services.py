import random

from src.board_repo import GameBoard

class GameServices:
    def __init__(self, board: GameBoard):
        self._board = board
        self._player_win = []
        self._counter = 0

    def transfer_board_to_ui(self):
        return str(self._board)

    def check_win(self):
        if self._counter == 9:
            pass

    def player_move(self, row, col, element):
        self._board.place_element(row - 1, col - 1, element)
        self._counter += 1
        self.check(row - 1, col - 1, element)

    def computer_move(self):
        """
        Here the computer makes the decision of whether to make a random move or if it needs to stop the player
            1. if the player is not close to a win it calls computer_move_random()
            2. else it calls computer_moves_to_stop()
        :return: a list with the coordinates where it moved and what element it used
        """
        if len(self._player_win) == 0:
            return self.computer_move_random()
        else:
            return self.computer_moves_to_stop()

    def computer_move_random(self):
        """
        1. It chooses a random set of coordinates and an element to move, in case it's an occupied cell it chooses again
        2. After the counter of elements is increased
        3. We check to see if there are 4 same elements in a line
        :return: a list with the coordinates where it moved and what element it used
        """
        while True:
            element = random.choice(['X', 'O'])
            row = random.randint(0, 5)
            col = random.randint(0, 5)
            try:
                self._board.place_element(row, col, element)
                break
            except Exception:
                continue

        self._counter += 1
        self.check(row, col, element)
        return [row + 1, col + 1, element]

    def computer_moves_to_stop(self):
        """
        1. We take the saved coordinates of an element from a 4 element line and choose right
         way of going through that line
        2. If computer couldn't place an element it calls random move
        3. Else it makes its move
        :return: a list with the coordinates where it moved and what element it used
        """
        move = self._player_win[-1]
        self._player_win.pop()
        if move[2] == 'MD':
            cmp_move = self.move_MD(move[0], move[1])
        elif move[2] == 'SD':
            cmp_move = self.move_SD(move[0], move[1])
        elif move[2] == 'H':
            cmp_move = self.move_H(move[0], move[1])
        elif move[2] == 'V':
            cmp_move = self.move_V(move[0], move[1])

        if len(cmp_move) == 0:
            return self.computer_move_random()
        else:
            if self._board.get_element(move[0], move[1]) == 'X':
                element = 'O'
            else:
                element = 'X'
            self._board.place_element(cmp_move[0], cmp_move[1], element)
            self._counter += 1
            self.check(cmp_move[0], cmp_move[1], element)
            return [cmp_move[0] + 1, cmp_move[1] + 1, element]

    def move_MD(self, row, col):
        """
        Looks for a free space in the main diagonal to stop the 4 element line
        :param row: the row of one of the elements from that line
        :param col: the col of one of the elements from that line
        :return: the coordinates where the computer moved
        """
        element = self._board.get_element(row, col)

        i = 0
        flag = 0
        while self._board.get_element(row + i, col + i) == element:
            i += 1
            if row + i > 5 or col + i > 5:
                flag = 1
                break

        if self._board.get_element(row + i, col + i) == ' ' and flag == 0:
            return [row + i, col + i]

        i = 0
        flag = 0
        while self._board.get_element(row - i, col - i) == element:
            i += 1
            if row - i < 0 or col - i < 0:
                flag = 1
                break
        if self._board.get_element(row - i, col - i) == ' ' and flag == 0:
            return [row - i, col - i]
        return []


    def move_SD(self, row, col):
        """
        Looks for a free space in the second diagonal to stop the 4 element line
        :param row: the row of one of the elements from that line
        :param col: the col of one of the elements from that line
        :return: the coordinates where the computer moved
        """
        element = self._board.get_element(row, col)

        i = 0
        flag = 0
        while self._board.get_element(row - i, col + i) == element:
            i += 1
            if row - i < 0 or col + i > 5:
                flag = 1
                break

        if self._board.get_element(row - i, col + i) == ' ' and flag == 0:
            return [row - i, col + i]

        i = 0
        flag = 0
        while self._board.get_element(row + i, col - i) == element:
            i += 1
            if row + i > 5 or col - i < 0:
                flag = 1
                break
        if self._board.get_element(row + i, col - i) == ' ' and flag == 0:
            return [row + i, col - i]
        return []

    def move_H(self, row, col):
        """
            Looks for a free space in the horizontal line to stop the 4 element line
            :param row: the row of one of the elements from that line
            :param col: the col of one of the elements from that line
            :return: the coordinates where the computer moved
        """
        element = self._board.get_element(row, col)

        i = 0
        flag = 0
        while self._board.get_element(row, col + i) == element:
            i += 1
            if col + i > 5:
                flag = 1
                break

        if self._board.get_element(row, col + i) == ' ' and flag == 0:
            return [row, col + i]

        i = 0
        flag = 0
        while self._board.get_element(row, col - i) == element:
            i += 1
            if col - i < 0:
                flag = 1
                break
        if self._board.get_element(row, col - i) == ' ' and flag == 0:
            return [row , col - i]
        return []

    def move_V(self, row, col):
        """
            Looks for a free space in the vertical line to stop the 4 element line
            :param row: the row of one of the elements from that line
            :param col: the col of one of the elements from that line
            :return: the coordinates where the computer moved
        """
        element = self._board.get_element(row, col)

        i = 0
        flag = 0
        while self._board.get_element(row + i, col) == element:
            i += 1
            if row + i > 5:
                flag = 1
                break

        if self._board.get_element(row + i, col) == ' ' and flag == 0:
            return [row + i, col]

        i = 0
        flag = 0
        while self._board.get_element(row - i, col) == element:
            i += 1
            if row - i < 0:
                flag = 1
                break
        if self._board.get_element(row - i, col) == ' ' and flag == 0:
            return [row - i, col]
        return []

    def check(self, row, col, element):
        """
        Checks if the new placed element creates a line of 4 same elements
        if yes keeps track of it by appending it to the player win list
        :param row: the row coordinate of the element
        :param col: the col coordinate of the element
        :param element: the element
        :return: nothing
        """
        if self.check_main_diagonal(row, col, element) == 4:
            self._player_win.append([row, col, 'MD'])
        if self.check_second_diagonal(row, col, element) == 4:
            self._player_win.append([row, col, 'SD'])
        if self.check_horizontal(row, col, element) == 4:
            self._player_win.append([row, col, 'H'])
        if self.check_vertical(row, col, element) == 4:
            self._player_win.append([row, col, 'V'])

    def check_main_diagonal(self, row, col, element):
        """
        Checks if the element has make a line of 4 on the main diagonal
        :param row: the row coordinate of the element
        :param col: the col coordinate of the element
        :param element: the specific element
        :return: a counter
        """
        counter = 0

        i = 0
        while self._board.get_element(row + i, col + i) == element:
            counter += 1
            i += 1
            if row + i < 0 or row + i > 5:
                break
            if col + i < 0 or col + i > 5:
                break

        i = 0
        counter -= 1
        while self._board.get_element(row - i, col - i) == element:
            counter += 1
            i += 1
            if row - i < 0 or row - i > 5:
                break
            if col - i < 0 or col - i > 5:
                break

        return counter

    def check_second_diagonal(self, row, col, element):
        """
                Checks if the element has make a line of 4 on the second diagonal
                :param row: the row coordinate of the element
                :param col: the col coordinate of the element
                :param element: the specific element
                :return: a counter
        """
        counter = 0

        i = 0
        while self._board.get_element(row - i, col + i) == element:
            counter += 1
            i += 1
            if row - i < 0 or row - i > 5:
                break
            if col + i < 0 or col + i > 5:
                break

        i = 0
        counter -= 1
        while self._board.get_element(row + i, col - i) == element:
            counter += 1
            i += 1
            if row + i < 0 or row + i > 5:
                break
            if col - i < 0 or col - i > 5:
                break

        return counter

    def check_horizontal(self, row, col, element):
        """
                Checks if the element has make a line of 4 on the horizontal line
                :param row: the row coordinate of the element
                :param col: the col coordinate of the element
                :param element: the specific element
                :return: a counter
        """
        counter = 0

        i = 0
        while self._board.get_element(row, col + i) == element:
            counter += 1
            i += 1
            if col + i < 0 or col + i > 5:
                break

        i = 0
        counter -= 1
        while self._board.get_element(row, col - i) == element:
            counter += 1
            i += 1
            if col - i < 0 or col - i > 5:
                break

        return counter

    def check_vertical(self, row, col, element):
        """
                Checks if the element has make a line of 4 on the vertical line
                :param row: the row coordinate of the element
                :param col: the col coordinate of the element
                :param element: the specific element
                :return: a counter
        """
        counter = 0

        i = 0
        while self._board.get_element(row - i, col) == element:
            counter += 1
            i += 1
            if row - i < 0 or row - i > 5:
                break

        i = 0
        counter -= 1
        while self._board.get_element(row + i, col) == element:
            counter += 1
            i += 1
            if row + i < 0 or row + i > 5:
                break

        return counter




