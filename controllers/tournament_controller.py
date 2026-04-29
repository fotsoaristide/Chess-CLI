"""tournament_controller class, Controller for managing tournaments."""

import json
from pathlib import Path
from models.tournament import Tournament


class TournamentController:
    def __init__(self):
        self.file_path = Path("data/tournaments.json")

    def load_tournaments(self):
        if not self.file_path.exists():
            return []

        with open(self.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Tournament.from_dict(t) for t in data]

    def save_tournaments(self, tournaments):
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in tournaments], f, indent=4)

    def create_tournament(self):
        """Create a new tournament from user input."""

        print("\n=== Create tournament ===")

        name = input("Name tournament: ")
        location = input("Location: ")
        start_date = input("Start date (YYYY-MM-DD): ")
        end_date = input("End date (YYYY-MM-DD): ")
        description = input("Description: ")

        tournament = Tournament(
            name,
            location,
            start_date,
            end_date,
            description
        )

        tournaments = self.load_tournaments()
        tournaments.append(tournament)
        self.save_tournaments(tournaments)

        print("Tournament created successfully!")