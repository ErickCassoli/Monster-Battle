from game.game_manager import GameManager
from game.character.baseCharacter import BaseCharacter
from game.character.races.elf import Elf
from game.character.classes.warrior import Warrior

def main():
    print("Bem-vindo ao Batalha de Waves!")
    print("Crie seu personagem.")

    # Criar personagem do jogador
    player_name = input("Nome do personagem: ")
    player = BaseCharacter(player_name, Elf(), Warrior())

    # Iniciar o jogo
    game_manager = GameManager(player)
    game_manager.start_game()

if __name__ == "__main__":
    main()
