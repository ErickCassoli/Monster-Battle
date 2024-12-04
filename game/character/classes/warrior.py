from ..baseClass import BaseClass

class Warrior(BaseClass):
    def __init__(self):
        super().__init__("Guerreiro", base_health=20, base_attack=5, base_defense=5)

    def attack(self, character, target):
        damage = self.calculate_damage()
        target.health -= damage
        print(f"{character.name} (Guerreiro) usou Golpe Giratório contra {target.name}, causando {damage} de dano em área!")

    def calculate_damage(self):
        return 20

    def ultimate(self, character, target):
        damage = 50
        target.health -= damage
        print(f"{character.name} (Guerreiro) usou Fúria de Batalha, causando {damage} de dano massivo!")