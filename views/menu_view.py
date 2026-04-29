class MenuView:

    @staticmethod
    def display():
        print("\n=== MAIN MENU ===")
        print("1. Add a player")
        print("2. Create a tournament")
        print("3. List tournaments")
        print("4. Quit")
    @staticmethod
    def get_choice():
        return input("Choice: ")