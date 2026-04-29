class MenuView:

    @staticmethod
    def display():
        print("\n=== MENU PRINCIPAL ===")
        print("1. Ajouter un joueur")
        print("2. Liste des joueurs")
        print("3. Créer un tournoi")
        print("4. Quitter")

    @staticmethod
    def get_choice():
        return input("Choix: ")
    
    @staticmethod
    def show_players(players):
        for p in players:
            print(p)