"""tournament_controller class, Controller for managing tournaments."""

import json
from pathlib import Path
from models.tournament import Tournament
from models.match import Match
from models.round import Round
from views.tournament_view import TournamentView


class TournamentController:
    def __init__(self, player_controller=None):
        self.file_path = Path("data/tournaments.json")
        self.player_controller = player_controller

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

        print("\n=== Create a tournament ===")

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

    def add_player_to_tournament(self, player_controller):
        """Add a player to a selected tournament."""
        tournaments = self.load_tournaments()

        if not tournaments:
            print("No tournaments available.")
            return

        # Show tournaments
        print("\n=== SSelection of tournament ===")
        for i, t in enumerate(tournaments):
            print(f"{i + 1}. {t.name}")

        choice = int(input("Choose a tournament: ")) - 1
        tournament = tournaments[choice]

        # Load players
        players = player_controller.load_players()

        if not players:
            print("No players available.")
            return

        # Show players
        print("\n=== List of Players ===")
        for i, p in enumerate(players):
            print(f"{i + 1}. {p.first_name} {p.last_name}")

        player_choice = int(input("Choose a player: ")) - 1
        player = players[player_choice]
        
        # Add player to tournament
        tournament.add_player(player)

        # Save updated tournament
        self.save_tournaments(tournaments)

        print("Player added to tournament!")

    def save_players(self, player_controller, players):
        player_controller.save_players(players)    

    def generate_first_round(self, players):
        """Generate the first round of a tournament based on player rankings."""
        players_sorted = sorted(players, key=lambda p: p.ranking, reverse=True)

        matches = []

        for i in range(0, len(players_sorted), 2):
            if i + 1 < len(players_sorted):
                match = Match(players_sorted[i], players_sorted[i + 1])
                matches.append(match)
                
        return matches
     
    def generate_next_round(self, players):
        """Generate subsequent rounds based on current player scores."""
        players_sorted = sorted(players, key=lambda p: p.score, reverse=True)

        matches = []

        for i in range(0, len(players_sorted), 2):
            if i + 1 < len(players_sorted):
                match = Match(players_sorted[i], players_sorted[i + 1])
                matches.append(match)

        return matches

    def update_match_scores(self, match, result):
        """Update the scores of a match based on the result."""
        if result == "1":
            match.update_scores(1, 0)
            match.player1.score += 1
        elif result == "2":
            match.update_scores(0, 1)
            match.player2.score += 1
        else:
            match.update_scores(0.5, 0.5)
            match.player1.score += 0.5
            match.player2.score += 0.5

    def play_round(self, tournament, players, round_number):
        """Play a round of the tournament, updating match scores and saving results."""
        if round_number == 1:
            matches = self.generate_first_round(players)
        else:
            matches = self.generate_next_round(players)

        round_obj = Round(name=f"Round {round_number}", matches=matches)

        TournamentView.display_matches(matches)

        for match in matches:
            result = TournamentView.ask_match_result()
            self.update_match_scores(match, result)

        # after updating scores, we need to save the updated player data
        self.save_players_from_tournament(self.player_controller, tournament)

        round_obj.end_round()
        tournament.rounds.append(round_obj)  

        # Save updated tournament with new round and match results
        tournaments = self.load_tournaments()

        for i, t in enumerate(tournaments):
            if t.name == tournament.name:
                tournaments[i] = tournament
                break

        self.save_tournaments(tournaments)  

    def save_players_from_tournament(self, player_controller, tournament):
        """Save all players from the tournament to ensure their scores are updated."""
        all_players = tournament.players
        player_controller.save_players(all_players)  
    