from src.play_services import GameServices


class UI:
    def __init__(self, services: GameServices):
        self._services = services

    def start(self):
        print(self._services.transfer_board_to_ui())
        win = False

        while not win:
            try:
                pl_moves = self.player_move()
            except Exception as ve:
                print(ve)
                continue
            cmp_moves = self.computer_move()
            self.print_board_moves(pl_moves, cmp_moves)

    def print_board_moves(self, pl_moves, cmp_moves):
        print(self._services.transfer_board_to_ui())
        print(f"Human: ({str(pl_moves[0])}, {str(pl_moves[1])}, {pl_moves[2].upper()})")
        print(f"AI: ({str(cmp_moves[0])}, {str(cmp_moves[1])}, {cmp_moves[2]})")

    def player_move(self):

        print("Order moves: ")
        read = input()
        move = read.split(',')

        if len(move) != 3:
            raise Exception("Invalid input, try template: [row],[col],[element];\n    separate by comma")

        row = int(move[0].strip())
        col = int(move[1].strip())
        element = move[2].strip()

        if row > 6 or row < 1:
            raise Exception("Row not on the board;  1 < row < 6")

        if col > 6 or col < 1:
            raise Exception("Column not on the board;  1 < col < 6")

        if element.upper() != "X" and element.upper() != "O":
            raise Exception("Element on board can only be 'X' or 'O'")

        self._services.player_move(row, col, element.upper())
        return [row, col, element]

    def computer_move(self):
        return self._services.computer_move()