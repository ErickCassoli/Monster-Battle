from ..baseRace import BaseRace

class Orc(BaseRace):
    def __init__(self):
        super().__init__("Orc", base_health=15, base_attack=7, base_defense=3)
        self.skill_name = "Investida Brutal"

    def attack(self, character, target):
        damage = self.calculate_damage()
        target.health -= damage
        print(f"{character.name} (Orc) usou {self.skill_name} contra {target.name}, causando {damage} de dano!")
        character.char_class.turns_since_last_ultimate += 1
        character.char_class.check_ultimate_ready(character)

    def calculate_damage(self):
        return 20