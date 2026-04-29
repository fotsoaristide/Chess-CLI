from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from views.menu_view import MenuView
from views.tournament_view import TournamentView


def main():
    player_controller = PlayerController()
    tournament_controller = TournamentController()

    while True:
        MenuView.display()
        choice = MenuView.get_choice()

        if choice == "1":
            player_controller.create_player()

        elif choice == "2":
            tournament_controller.create_tournament()

        elif choice == "3":
            tournament_controller.add_player_to_tournament(player_controller)

        elif choice == "4":
            tournaments = tournament_controller.load_tournaments()
            TournamentView.display_tournaments(tournaments)
        elif choice == "5":
            break


if __name__ == "__main__":
    main()