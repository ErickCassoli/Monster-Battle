from ..baseRace import BaseRace

class Elf(BaseRace):
    def __init__(self):
        super().__init__("Elfo", base_health=10, base_attack=5, base_defense=2)
        self.skill_name = "Flecha Arcana"

    def attack(self, character, target):
        damage = self.calculate_damage()
        target.health -= damage
        print(f"{character.name} (Elfo) usou {self.skill_name} contra {target.name}, causando {damage} de dano!")

    def calculate_damage(self):
        return 15