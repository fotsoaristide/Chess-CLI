"""Manages player data and interactions between the model and view."""

from models.player import Player
from controllers.storage import JsonStorage
from views.player_view import PlayerView


class PlayerController:
    def __init__(self):
        self.storage = JsonStorage("data/players.json")

    def load_players(self):
        data = self.storage.load()
        return [Player.from_dict(p) for p in data]

    def save_players(self, players):
        data = [p.to_dict() for p in players]
        self.storage.save(data)

    def create_player(self):
        """Create player using PlayerView."""
        first_name, last_name, birthdate, chess_id = (
            PlayerView.ask_player_data())

        player = Player(first_name, last_name, birthdate, chess_id)

        players = self.load_players()
        players.append(player)

        self.save_players(players)

        PlayerView.display_success_creation()
