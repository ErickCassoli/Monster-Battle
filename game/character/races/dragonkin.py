from ..baseRace import BaseRace

class Dragonkin(BaseRace):
    def __init__(self):
        super().__init__("Draconato", base_health=14, base_attack=8, base_defense=4)
        self.skill_name = "Sopro Flamejante"

    def attack(self, character, target):
        damage = self.calculate_damage()
        target.health -= damage
        print(f"{character.name} (Draconato) usou {self.skill_name} contra {target.name}, causando {damage} de dano!")
        character.char_class.turns_since_last_ultimate += 1
        character.char_class.check_ultimate_ready(character)

    def calculate_damage(self):
        return 22