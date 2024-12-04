from game.utils.character_utils import create_character
from game.monster_factory import MonsterFactory
from game.save_manager import SaveManager

class GameManager:
    def __init__(self):
        self.wave = 1
        self.score = 0

    def show_health(self, player, enemy):
        print(f"\nHP de {player.name}: {player.health}")
        print(f"HP de {enemy.name}: {enemy.health}")


    def pvp_mode(self):
        print("Jogador 1, crie seu personagem:")
        player1 = create_character()

        print("Jogador 2, crie seu personagem:")
        player2 = create_character()

        players = [player1, player2]
        turn = 0

        while all(player.health > 0 for player in players):
            current_player = players[turn % 2]
            target = players[(turn + 1) % 2]
            self.show_health(current_player, target)

            print(f"\nTurno de {current_player.name}")
            print("Escolha sua ação:")
            print("1. Ataque Básico\n2. Ataque de Raça\n3. Ataque de Classe\n4. Ultimate")
            action = input("Escolha: ")

            if action == "1":
                current_player.basic_attack(target)
            elif action == "2":
                current_player.race_attack(target)
            elif action == "3":
                current_player.class_attack(target)
            elif action == "4":
                current_player.ultimate(target)
            else:
                print("Ação inválida!")

            if target.health <= 0:
                print(f"{target.name} foi derrotado!")
                break

            turn += 1

        winner = players[0] if players[0].health > 0 else players[1]
        print(f"\n{winner.name} venceu a batalha!")


    def pve_mode(self):
        print("Crie seu personagem:")
        player = create_character()

        while player.health > 0:
            print(f"\n=== Wave {self.wave} ===")
            monster = MonsterFactory.create_monster(self.wave)
            print(f"Você está enfrentando um {monster.name} com {monster.health} de HP!")

            while player.health > 0 and monster.health > 0:
                self.show_health(player, monster)
                print("\nTurno do jogador")
                print("Escolha sua ação:")
                print("1. Ataque Básico\n2. Ataque de Raça\n3. Ataque de Classe\n4. Ultimate")
                action = input("Escolha: ")

                if action == "1":
                    player.basic_attack(monster)
                elif action == "2":
                    player.race_attack(monster)
                elif action == "3":
                    player.class_attack(monster)
                elif action == "4":
                    player.ultimate(monster)
                else:
                    print("Ação inválida!")

                if monster.health > 0:
                    self.show_health(player, monster)
                    print("\nTurno do monstro")
                    monster.attack(player)

            if player.health <= 0:
                print(f"\nVocê foi derrotado na Wave {self.wave}!")
                break

            print(f"Parabéns! Você sobreviveu à Wave {self.wave}!")
            self.wave += 1
            self.score += 100
            player.health = min(player.health + 10, 100)  # Recupera 10 HP por wave

        print(f"Fim de jogo! Sua pontuação final foi: {self.score}")
        SaveManager.save_score(player.name, self.score)