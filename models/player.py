"""Player class for chess tournament management."""

import re


class Player:
    """Represents a chess player."""
    def __init__(self, first_name, last_name, birthdate, chess_id, ranking=0):
        if not self.is_valid_chess_id(chess_id):
            raise ValueError("Invalid chess ID format (ex: AB12345)")

        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.chess_id = chess_id
        self.ranking = ranking
        self.score = 0

    def to_dict(self):
        """Convert the Player instance to a dictionary for JSON storage."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthdate": self.birthdate,
            "chess_id": self.chess_id,
            "ranking": self.ranking,
            "score": self.score
        }

    @staticmethod
    def is_valid_chess_id(chess_id: str) -> bool:
        """Validate the chess ID format (ex: AB12345)."""
        return bool(re.match(r"^[A-Z]{2}\d{5}$", chess_id))

    @staticmethod
    def from_dict(data):
        """Create a Player instance from a dictionary."""
        player = Player(
            data["first_name"],
            data["last_name"],
            data["birthdate"],
            data["chess_id"],
            data.get("ranking", 0)
        )

        player.score = data.get("score", 0)

        return player

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def __lt__(self, other):
        return (self.last_name,
                self.first_name) < (other.last_name,
                                    other.first_name)
