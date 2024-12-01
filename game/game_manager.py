import random
from .monster_factory import MonsterFactory
from .save_manager import SaveManager

class GameManager:
    def __init__(self, player):
        self.player = player
        self.wave = 1
        self.score = 0

    def start_game(self):
        print(f"Bem-vindo, {self.player.name}! Prepare-se para enfrentar as waves de inimigos!")
        
        while self.player.health > 0:
            print(f"\n=== Wave {self.wave} ===")
            
            # Recuperação de HP no início da wave
            self.recover_health()

            # Criar inimigo para a wave atual
            enemy = MonsterFactory.create_monster(self.wave)
            print(f"Você está enfrentando um {enemy.name} com {enemy.health} de HP!")

            # Combate
            self.combat(enemy)

            if self.player.health > 0:
                print(f"Parabéns! Você sobreviveu à wave {self.wave}!")
                self.wave += 1
                self.score += 100  # Aumenta a pontuação por wave concluída

        print(f"Fim de jogo! Sua pontuação final foi: {self.score}")
        SaveManager.save_score(self.player.name, self.score)

    def recover_health(self):
        recovery = min(10, 100 - self.player.health)  # Recupera 10 HP ou o necessário até o máximo
        self.player.health += recovery
        print(f"{self.player.name} recuperou {recovery} de HP! HP atual: {self.player.health}")

    def combat(self, enemy):
        while self.player.health > 0 and enemy.health > 0:
            print("\nSuas opções:")
            print("1. Ataque Básico")
            print("2. Ataque de Raça")
            print("3. Ataque de Classe")
            print("4. Ultimate")

            choice = input("Escolha sua ação: ")

            if choice == "1":
                self.player.basic_attack(enemy)
            elif choice == "2":
                self.player.race_attack(enemy)
            elif choice == "3":
                self.player.class_attack(enemy)
            elif choice == "4":
                self.player.ultimate(enemy)
            else:
                print("Opção inválida!")

            if enemy.health > 0:
                enemy.attack(self.player)
                print(f"O {enemy.name} atacou! HP do jogador: {self.player.health}")
