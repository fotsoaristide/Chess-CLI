"""A class representing a chess tournament."""

from models.player import Player
from models.round import Round


class Tournament:
    """Represents a chess tournament."""

    def __init__(self, name, location, start_date, end_date,
                 description="", nb_rounds=4):

        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description

        self.nb_rounds = nb_rounds
        self.current_round = 0

        self.players = []
        self.rounds = []

    def add_player(self, player):
        """Add a player to the tournament."""
        if player not in self.players:
            self.players.append(player)

    def add_round(self, round_obj):
        """Add a round to the tournament."""
        self.rounds.append(round_obj)
        self.current_round += 1

    def is_finished(self):
        """Check if tournament is finished."""
        return self.current_round >= self.nb_rounds

    def get_standings(self):
        """Return players sorted by score."""
        return sorted(self.players, key=lambda p: p.score, reverse=True)

    def to_dict(self):
        """Convert tournament to dictionary for JSON."""
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "nb_rounds": self.nb_rounds,
            "current_round": self.current_round,
            "players": [p.to_dict() for p in self.players],
            "rounds": [r.to_dict() for r in self.rounds]
        }

    @staticmethod
    def from_dict(data):
        """Create Tournament from dictionary."""

        tournament = Tournament(
            data["name"],
            data["location"],
            data["start_date"],
            data["end_date"],
            data.get("description", ""),
            data.get("nb_rounds", 4)
        )

        tournament.current_round = data.get("current_round", 0)

        # Rebuild players
        tournament.players = [
            Player.from_dict(p) for p in data.get("players", [])
        ]

        # Rebuild rounds
        tournament.rounds = [
            Round.from_dict(r) for r in data.get("rounds", [])
        ]

        return tournament

    def __str__(self):
        return f"Tournament: {self.name} at {self.location}"
