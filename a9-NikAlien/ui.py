from game_play_services import GameServices


class UI:
    def __init__(self, services: GameServices):
        self._services = services

    def print_start_menu(self):
        print("\nWELCOME TO GOMOKU GAME\n")
        print("      --MENU--        ")
        print("   start game - s")
        print("      exit - x\n")

    def print_game_mode(self):
        print("\nSelect when do you want ot move: ")
        print("   first - 1")
        print("   second - 2\n")

    def start(self):
        while True:
            self.print_start_menu()
            choice = input("--> ")

            if choice.lower() == "x":
                break
            elif choice.lower() == "s":
                self.play_game()
                break
            else:
                print("! Unidentifiable command !")

    def play_game(self):
        while True:
            self.print_game_mode()
            mode = input("--> ")
            winner = None
            games = {"2": self.mode_computer_first, "1": self.mode_player_first}

            if mode not in games:
                print("! Unidentifiable command !")
            else:
                print("\n  --GAME START--  \n")
                print(self._services.get_data_to_ui())
                while True:
                    if self._services.check_draw_game():
                        winner = "NOBODY"
                        break
                    try:
                        winner = games[mode]()
                        if winner is not None:
                            break
                    except Exception as ve:
                         print(ve)

            print(f"\n  -- {winner} WINS --")
            print( "   --- End Game ---\n")
            print("\n----------------------\n")
            break

    def player_move_read(self):
        while True:
            row = int(input("Row: "))
            col = input("Column: ")

            if col.upper() < 'A' or col.upper() > 'J':
                print("! Column must be between A and J !")
            elif row < 1 or row > 10:
                print("! Row must be between 1 and 10 !")
            else:
                return [row - 1, ord(col.upper()) - ord('A')]

    def player_move(self):
        while True:
            try:
                move = self.player_move_read()
                self._services.player_move(move[0], move[1])
                break
            except Exception as ve:
                print(ve)

        print(self._services.get_data_to_ui())
        win = self._services.check_win(move[0], move[1], 'O')
        return win


    def computer_move(self):
        move = self._services.computer_tactic()
        print("\nComputer moves: ")
        print(f"  row - {move[0] + 1}")
        print(f"  column - {chr(move[1] + ord('A'))}\n")
        print(self._services.get_data_to_ui())
        win = self._services.check_win(move[0], move[1], 'X')
        return win



    def mode_player_first(self):
        """
        - lets player move first
        - checks if they won
        - lets computer move next
        - checks if computer won
        :return: "PLAYER" - player win, "COMPUTER" - computer win, NONE - nobody win
        """
        win = self.player_move()
        if win is not False:
            return "PLAYER"

        win = self.computer_move()
        if win is not False:
            return "COMPUTER"

        return None



    def mode_computer_first(self):
        """
        - lets computer move first
        - checks if it won
        - lets player move next
        - checks if they won
        :return: "PLAYER" - player win, "COMPUTER" - computer win, NONE - nobody win
        """
        win = self.computer_move()
        if win is not False:
            return "COMPUTER"

        win = self.player_move()
        if win is not False:
            return "PLAYER"

        return None
