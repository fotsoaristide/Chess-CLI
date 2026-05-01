"""Main application file for the chess tournament management system."""

from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from views.player_view import PlayerView


def display_menu():
    print("\n====== CHESS TOURNAMENT ======")
    print("1. Create tournament")
    print("2. Add player to tournament")
    print("3. Launch tournament")
    print("4. Show tournaments")
    print("5. Show players")
    print("6. Quit")


def choose_tournament(tournaments):
    if not tournaments:
        print("No tournaments available.")
        return None

    print("\n=== Tournaments ===")
    for i, t in enumerate(tournaments):
        print(f"{i + 1}. {t.name}")

    choice = int(input("Choose a tournament: ")) - 1
    return tournaments[choice]


def show_tournaments(tournaments):
    print("\n=== Tournaments ===")
    for t in tournaments:
        print(f"{t.name} ({len(t.players)} players)")


def display_final_ranking(players):
    print("\n===== FINAL RANKING =====")
    sorted_players = sorted(players, key=lambda p: p.score, reverse=True)

    for i, p in enumerate(sorted_players, start=1):
        print(f"{i}. {p.first_name} {p.last_name} - {p.score} pts")


def launch_tournament(tournament_controller):
    tournaments = tournament_controller.load_tournaments()
    tournament = choose_tournament(tournaments)

    if not tournament:
        return

    if tournament.current_round > 0:
        print("This tournament has already started or finished.")
        return

    players = tournament.players

    if len(players) < 2:
        print("Not enough players.")
        return

    # Reset scores
    for player in players:
        player.score = 0

    if tournament_controller.player_controller:
        tournament_controller.save_players_from_tournament(
            tournament_controller.player_controller,
            tournament
        )

    print(f"\nStarting tournament: {tournament.name}")

    number_of_rounds = tournament.nb_rounds

    for round_number in range(1, number_of_rounds + 1):
        print(f"\n=== ROUND {round_number} ===")
        tournament_controller.play_round(tournament, players, round_number)

    print("\nTournament finished!")
    display_final_ranking(players)


def main():
    player_controller = PlayerController()
    tournament_controller = TournamentController(player_controller)

    while True:
        display_menu()
        choice = input(" Your choice: ")

        if choice == "1":
            tournament_controller.create_tournament()

        elif choice == "2":
            tournament_controller.add_player_to_tournament(player_controller)

        elif choice == "3":
            launch_tournament(tournament_controller)

        elif choice == "4":
            tournaments = tournament_controller.load_tournaments()
            show_tournaments(tournaments)

        elif choice == "5":
            players = player_controller.load_players()
            PlayerView.display_players(players)

        elif choice == "6":
            print("Goodbye !")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
