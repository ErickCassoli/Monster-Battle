from ..baseClass import BaseClass

class Paladin(BaseClass):
    def __init__(self):
        super().__init__("Paladino", base_health=18, base_attack=5, base_defense=6)
        self.hit_name = "Martelo Sagrado"
        self.attack_skill_name = "Golpe Purificador"
        self.ultimate_skill_name = "Proteção Divina"
        self.turns_since_last_ultimate = 0

    def attack(self, character, target):
        damage = self.calculate_damage()
        print(f"{character.name} (Paladino) usou {self.attack_skill_name} contra {target.name}, causando {damage} de dano!")
        target.health -= damage
        self.turns_since_last_ultimate += 1
        self.check_ultimate_ready(character)

    def calculate_damage(self):
        return 15

    def ultimate(self, character, target):
        if not character.ultimate_ready:
            print(f"{character.name} tentou usar {self.ultimate_skill_name}, mas ela ainda não está pronta!")
            return
        print(f"{character.name} (Paladino) conjurou {self.ultimate_skill_name}, restaurando 50 de vida!")
        character.health += 50
        character.ultimate_ready = False
        self.turns_since_last_ultimate = 0

    def check_ultimate_ready(self, character):
        if self.turns_since_last_ultimate >= 3:
            character.ultimate_ready = True
            print(f"A ultimate {self.ultimate_skill_name} de {character.name} está pronta!")
            self.turns_since_last_ultimate = 0
