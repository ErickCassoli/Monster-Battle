from ..baseRace import BaseRace

class Elf(BaseRace):
    def __init__(self):
        super().__init__("Elfo", base_health=10, base_attack=5, base_defense=2)

    def attack(self, character, target):
        damage = self.calculate_damage()
        target.health -= damage
        print(f"{character.name} (Elfo) usou Flecha Arcana contra {target.name}, causando {damage} de dano!")

    def calculate_damage(self):
        return 15