from src.services import Services

class UI:
    def __init__(self, service: Services):
        self._commands = {"d": self.display_list, "p": self.play}
        self._service = service

    def print_menu(self):
        print("\nChoose your command: ")
        print("   d - display list of players")
        print("   p - play the tournament")
        print("   x - exit")

    def start(self):
        while True:
            self.print_menu()
            _choice = input("--> ")

            if _choice == "x":
                break

            elif _choice not in self._commands:
                print("Unidentifiable command")

            else:
                try:
                    self._commands[_choice]()
                except Exception as ve:
                    print(ve)

    def display_list(self):
        print("\nPlayer list: ")
        for player in self._service.sort_player_list():
            print(player)

    def play(self):
        while True:
            number_qualifications = self._service.number_of_players_to_eliminate()

            if number_qualifications != 0:
                for i in range(number_qualifications):
                    print("Qualifying round:")
                    self.play_round(self._service.qualifying_round_pair())
            else:
                print("No qualifying rounds, start tournament: ")

            players_left = self._service.number_of_players_left()
            if players_left == 1:
                break

            print(f"\nLast {players_left} players")
            self.play_round(self._service.tournament_pairs())

        print("The tournament has ended!!!")


    def play_round(self, pair):
        for player in pair:
            print(player)

        print("\n Choose the id of the winner: ")

        while True:
            winner_id = int(input("--> "))
            if winner_id == pair[0].id:
                self._service.add_player(pair[0])
                break
            elif winner_id == pair[1].id:
                self._service.add_player(pair[1])
                break
            else:
                print("Wrong input value")