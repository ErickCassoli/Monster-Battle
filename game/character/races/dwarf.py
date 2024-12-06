from ..baseRace import BaseRace

class Dwarf(BaseRace):
    def __init__(self):
        super().__init__("Anão", base_health=12, base_attack=6, base_defense=5)
        self.skill_name = "Golpe Pesado"

    def attack(self, character, target):
        damage = self.calculate_damage()
        target.health -= damage
        print(f"{character.name} (Anão) usou {self.skill_name} contra {target.name}, causando {damage} de dano!")
        character.char_class.turns_since_last_ultimate += 1
        character.char_class.check_ultimate_ready(character)

    def calculate_damage(self):
        return 18