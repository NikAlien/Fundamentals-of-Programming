from src.domain import Player

class Repository:
    def __init__(self):
        self._data = {}

    def add(self, new_player):
        self._data[new_player.id] = new_player

    def delete(self, player_id):
        del self._data[player_id]

    def search_weakest_player(self):
        id = 0
        strength = 1000

        for player in self.get_all_players():
            if player.strength < strength:
                strength = player.strength
                id = player.id

        return self.get(id)

    def get_all_players(self):
        return list(self._data.values())

    def get(self, player_id):
        return self._data[player_id]

    def __len__(self):
        return len(self.get_all_players())


class TextFileRepository(Repository):
    def __init__(self, file_name = "players_list.txt"):
        super(TextFileRepository, self).__init__()
        self._file_name = file_name

        self._load_file()

    def _load_file(self):
        fin = open(self._file_name, "rt")
        lines = fin.readlines()
        fin.close()

        for line in lines:
            line = line.split(',')
            new_player = Player(int(line[0]), line[1], int(line[2].strip()))
            super().add(new_player)

    def _save_file(self):
        fout = open(self._file_name, "wt")

        for player in self.get_all_players():
            line = str(player.id) + "," + player.name + "," + str(player.strength) + "\n"
            fout.write(line)

        fout.close()

