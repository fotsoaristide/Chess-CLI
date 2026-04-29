"""Controller for managing chess players."""

from models.player import Player
from controllers.storage import JsonStorage


class PlayerController:
    def __init__(self):
        self.storage = JsonStorage("data/players.json")

    def load_players(self):
        """Load players from JSON and return Player objects."""
        data = self.storage.load()
        return [Player.from_dict(p) for p in data]

    def create_player(self):
        """Create a new player by getting input from the user."""
        first_name = input("First name: ")
        last_name = input("Last name: ")
        birthdate = input("Birth date (YYYY-MM-DD): ")
        chess_id = input("Chess ID (e.g., AB12345): ")

        player = Player(first_name, last_name, birthdate, chess_id)

        players = self.storage.load()
        players.append(player.to_dict())

        self.storage.save(players)

        print("Player created successfully!")