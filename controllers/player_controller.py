"""Controller for managing chess players."""

from models.player import Player
from controllers.storage import JsonStorage


class PlayerController:
    def __init__(self):
        self.storage = JsonStorage("data/players.json")

    def create_player(self):
        """Create a new player by getting input from the user."""
        first_name = input("Prénom: ")
        last_name = input("Nom: ")
        birthdate = input("Date de naissance: ")
        chess_id = input("ID échec (ex: AB12345): ")

        player = Player(first_name, last_name, birthdate, chess_id)

        players = self.storage.load()
        players.append(player.to_dict())

        self.storage.save(players)

        print("Joueur ajouté !")