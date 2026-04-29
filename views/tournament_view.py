"""Tournament view class for displaying tournament information."""

class TournamentView:
    
    @staticmethod
    def display_tournaments(tournaments):
        print("\n=== Liste des tournois ===")
        for t in tournaments:
            print(t)