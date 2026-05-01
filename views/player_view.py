""" class PlayerView Handle all player inputs and displays."""


class PlayerView:

    @staticmethod
    def ask_player_data():
        """Ask user for player info."""
        print("\n=== Create Player ===")

        first_name = input("First name: ")
        last_name = input("Last name: ")
        birthdate = input("Birth date (YYYY-MM-DD): ")
        chess_id = input("Chess ID: ")

        return first_name, last_name, birthdate, chess_id

    @staticmethod
    def display_success_creation():
        print("Player created successfully!")

    @staticmethod
    def display_players(players):
        print("\n=== Players ===")
        for i, p in enumerate(players, start=1):
            print(
                f"{i}. {p.first_name} {p.last_name} | "
                f"Rank: {p.ranking} | Score: {p.score}"
            )

    @staticmethod
    def choose_player(players):
        print("\n=== Select Player ===")

        for i, p in enumerate(players, start=1):
            print(f"{i}. {p.first_name} {p.last_name}")

        try:
            choice = int(input("Choose a player: ")) - 1
            return players[choice]
        except (ValueError, IndexError):
            print("Invalid choice.")
            return None
