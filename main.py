from game.game_manager import GameManager
from game.save_manager import SaveManager

def main():
    game_manager = GameManager()

    print("Bem-vindo ao Batalha de Monstros!")
    while True:
        print("\nMenu Principal:")
        print("1. PvP (Jogador vs Jogador)\n2. PvE (Jogador vs Computador)\n3. Carregar Pontuações\n4. Sair")
        choice = input("Escolha: ")

        if choice == "1":
            game_manager.pvp_mode()
        elif choice == "2":
            game_manager.pve_mode()
        elif choice == "3":
            scores = SaveManager.load_scores()
            print("Pontuações Salvas:")
            for player, score in scores.items():
                print(f"{player}: {score}")
        elif choice == "4":
            print("Saindo do jogo. Até logo!")
            break
        else:
            print("Escolha inválida!")

if __name__ == "__main__":
    main()
