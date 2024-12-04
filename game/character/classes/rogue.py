from ..baseClass import BaseClass

class Rogue(BaseClass):
    def __init__(self):
        super().__init__("Ladino", base_health=14, base_attack=8, base_defense=3)
        self.hit_name = "Facada Rápida"
        self.attack_skill_name = "Ataque das Sombras"
        self.ultimate_skill_name = "Dança das Adagas"
        self.turns_since_last_ultimate = 0

    def attack(self, character, target):
        damage = self.calculate_damage()
        print(f"{character.name} (Ladino) usou {self.attack_skill_name} contra {target.name}, causando {damage} de dano!")
        target.health -= damage
        self.turns_since_last_ultimate += 1
        self.check_ultimate_ready(character)

    def calculate_damage(self):
        return 18

    def ultimate(self, character, target):
        if not character.ultimate_ready:
            print(f"{character.name} tentou usar {self.ultimate_skill_name}, mas ela ainda não está pronta!")
            return
        damage = 40
        print(f"{character.name} (Ladino) realizou {self.ultimate_skill_name}, atingindo todos os inimigos ao redor!")
        target.health -= damage
        character.ultimate_ready = False
        self.turns_since_last_ultimate = 0

    def check_ultimate_ready(self, character):
        if self.turns_since_last_ultimate >= 3:
            character.ultimate_ready = True
            print(f"A ultimate {self.ultimate_skill_name} de {character.name} está pronta!")
            self.turns_since_last_ultimate = 0
