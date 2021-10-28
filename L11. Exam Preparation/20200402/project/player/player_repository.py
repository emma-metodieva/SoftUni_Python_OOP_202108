from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    # @property
    # def count(self):
    #     return len(self.players)

    def add(self, player: Player):
        add_player_username = player.username
        player_usernames = [p.username for p in self.players]

        if add_player_username in player_usernames:
            raise ValueError(f"Player {add_player_username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, username: str):
        if username == '':
            raise ValueError("Player cannot be an empty string!")

        player_to_remove = self.find(username)
        self.players.remove(player_to_remove)
        self.count -= 1

    def find(self, username: str):
        player = [p for p in self.players if p.username == username][0]
        return player
