"""Class representing a round in a tournament."""

from datetime import datetime
from models.match import Match


class Round:
    def __init__(self, name, matches=None, start_date=None, end_date=None):
        self.name = name
        self.matches = matches if matches else []  # list of Match objects
        self.start_date = start_date or datetime.now().isoformat()
        self.end_date = end_date

    def end_round(self):
        """End the round by setting the end date."""
        self.end_date = datetime.now().isoformat()

    def to_dict(self):
        """Convert the round to a dictionary."""
        return {
            "name": self.name,
            "matches": [match.to_dict() for match in self.matches],
            "start_date": self.start_date,
            "end_date": self.end_date,
        }

    @staticmethod
    def from_dict(data):
        """Reconstruct a round from a dictionary."""
        matches = [Match.from_dict(m) for m in data.get("matches", [])]

        return Round(
            name=data.get("name"),
            matches=matches,
            start_date=data.get("start_date"),
            end_date=data.get("end_date"),
        )
    def __str__(self):        
        return f"{self.name} ({len(self.matches)} matches)"