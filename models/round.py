"""Round class for chess tournament management."""

from datetime import datetime
from models.match import Match


class Round:
    """Represents a round in a chess tournament."""

    def __init__(self, name, matches=None, start_date=None, end_date=None):
        self.name = name
        self.start_date = start_date 
        self.end_date = end_date
        self.matches = matches if matches is not None else []

    def start_round(self):
        """Mark the round as started by setting start date."""
        self.start_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def end_round(self):
        """Mark the round as finished by setting end date."""
        self.end_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """Convert Round to dictionary for JSON."""
        return {
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "matches": [m.to_dict() for m in self.matches]
        }

    @staticmethod
    def from_dict(data):
        """Create Round from dictionary."""
        return Round(
            name=data["name"],
            matches=[Match.from_dict(m) for m in data.get("matches", [])],
            start_date=data.get("start_date"),
            end_date=data.get("end_date")
        )

    def __str__(self):
        return f"{self.name} ({self.start_date} - {self.end_date})"