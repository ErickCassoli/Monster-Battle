from ..baseClass import BaseClass

class Mage(BaseClass):
    def __init__(self):
        super().__init__("Mago", base_health=12, base_attack=7, base_defense=2)
        self.hit_name = "Explosão de Energia"
        self.attack_skill_name = "Bola de Fogo"
        self.ultimate_skill_name = "Tempestade Arcana"
        self.turns_since_last_ultimate = 0

    def attack(self, character, target):
        damage = self.calculate_damage()
        print(f"{character.name} (Mago) usou {self.attack_skill_name} contra {target.name}, causando {damage} de dano!")
        target.health -= damage
        self.turns_since_last_ultimate += 1
        self.check_ultimate_ready(character)

    def calculate_damage(self):
        return 25

    def ultimate(self, character, target):
        if not character.ultimate_ready:
            print(f"{character.name} tentou usar {self.ultimate_skill_name}, mas ela ainda não está pronta!")
            return
        damage = 60
        print(f"{character.name} (Mago) conjurou {self.ultimate_skill_name}, causando {damage} de dano devastador!")
        target.health -= damage
        character.ultimate_ready = False
        self.turns_since_last_ultimate = 0

    def check_ultimate_ready(self, character):
        if self.turns_since_last_ultimate >= 4:
            character.ultimate_ready = True
            print(f"A ultimate {self.ultimate_skill_name} de {character.name} está pronta!")
            self.turns_since_last_ultimate = 0
