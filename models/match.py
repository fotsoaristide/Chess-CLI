"""Match class representing a match between two players in a tournament."""

from models.player import Player


class Match:
    def __init__(self, player1, player2, score1=0, score2=0):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def to_dict(self):
        """Convert Match to dictionary for JSON."""
        return {
            "player1": self.player1.to_dict(),
            "score1": self.score1,
            "player2": self.player2.to_dict(),
            "score2": self.score2
        }

    def update_scores(self, score1, score2):
        """Update the scores of the match."""
        self.score1 = score1
        self.score2 = score2

    def get_winner(self):
        """Determine the winner of the match."""
        if self.score1 > self.score2:
            return self.player1
        elif self.score2 > self.score1:
            return self.player2
        return None  # Draw
    
    def is_draw(self):
        return self.score1 == self.score2

    @staticmethod
    def from_dict(data):
        """Create Match from dictionary."""
        return Match(
            Player.from_dict(data["player1"]),
            Player.from_dict(data["player2"]),
            data.get("score1", 0),
            data.get("score2", 0)
        )

    def __str__(self):
        return f"{self.player1} ({self.score1}) vs {self.player2} ({self.score2})"