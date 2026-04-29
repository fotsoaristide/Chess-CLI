"""Main entry point for the application."""

from controllers.player_controller import PlayerController
from views.menu_view import MenuView


def main():
    player_controller = PlayerController()

    while True:
        MenuView.display()
        choice = MenuView.get_choice()

        if choice == "1":
            player_controller.create_player()
        elif choice == "4":
            break


if __name__ == "__main__":
    main()