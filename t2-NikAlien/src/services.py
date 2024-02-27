import random

class Services:
    def __init__(self, player_repo):
        self._player_repo = player_repo

    def add_player(self, new_player):
        """
        Adding the winning player back to the list while also adding to their strength
        :param new_player:
        :return:
        """
        new_player.strength += 1
        self._player_repo.add(new_player)

    def sort_player_list(self):
        """
        returning the list in descending order
        :return:
        """
        return sorted(self._player_repo.get_all_players(), key= lambda x: x.strength, reverse = True)

    def number_of_players_to_eliminate(self):
        """
        How many players to qualify, we look for the biggest number tht;s a square of two that's smaller than the length
        of the current list
        :return:
        """
        current_pair = 2
        while current_pair * 2 <= len(self._player_repo):
            current_pair *= 2
        return len(self._player_repo) - current_pair

    def number_of_players_left(self):
        return len(self._player_repo)

    def weakest_player(self):
        return self._player_repo.search_weakest_player()

    def qualifying_round_pair(self):
        """
        looks for the weakest player and deletes it
        after we look again for the other weakest player and return both

        :return: the pair
        """
        player1 = self.weakest_player()
        self._player_repo.delete(player1.id)

        player2 = self.weakest_player()
        self._player_repo.delete(player2.id)

        return [player1, player2]

    def tournament_pairs(self):
        """

        using random choice we look for two random players and return them both
        as a pair while deleting from the original list

        :return:
        """
        player1 = random.choice(self._player_repo.get_all_players())
        self._player_repo.delete(player1.id)

        player2 = random.choice(self._player_repo.get_all_players())
        self._player_repo.delete(player2.id)

        return [player1, player2]







