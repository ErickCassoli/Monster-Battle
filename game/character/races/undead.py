from ..baseRace import BaseRace

class Undead(BaseRace):
    def __init__(self):
        super().__init__("Mortovivo", base_health=8, base_attack=6, base_defense=2)
        self.skill_name = "Toque Sombrio"

    def attack(self, character, target):
        damage = self.calculate_damage()
        target.health -= damage
        print(f"{character.name} (Mortovivo) usou {self.skill_name} contra {target.name}, causando {damage} de dano!")
        character.char_class.turns_since_last_ultimate += 1
        character.char_class.check_ultimate_ready(character)

    def calculate_damage(self):
        return 14