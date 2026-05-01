class MenuView:

    @staticmethod
    def display():
        print("\n=== MAIN MENU ===")
        print("1. Add a player")
        print("2. Create a tournament")
        print("3. Add a player to a tournament")
        print("4. List of tournamants")
        print("5. Exit")

    @staticmethod
    def get_choice():
        return input("Choice: ")
