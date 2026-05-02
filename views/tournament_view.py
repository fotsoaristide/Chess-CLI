"""Tournament view class for displaying tournament information."""


class TournamentView:

    @staticmethod
    def display_tournaments(tournaments):
        print("\n=== Lists of tournaments ===")
        for t in tournaments:
            print(t)

    @staticmethod
    def display_matches(matches):
        print("\n===== MATCHS =====")
        for i, match in enumerate(matches, start=1):
            print(f"Match {i} : {match.player1} vs {match.player2}")

    @staticmethod
    def ask_match_result():
        print("\nResult of match :")
        print("1 -> Player 1 wins")
        print("2 -> Player 2 wins")
        print("3 -> Draw")

        return input(" Choice : ")
