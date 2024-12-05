from ..baseClass import BaseClass

class Necromancer(BaseClass):
    def __init__(self):
        super().__init__("Necromante", base_health=10, base_attack=6, base_defense=3)
        self.hit_name = "Golpe Sombrio"
        self.attack_skill_name = "Dreno de Vida"
        self.ultimate_skill_name = "Exército de Mortos"
        self.turns_since_last_ultimate = 0

    def attack(self, character, target):
        damage = self.calculate_damage()
        print(f"{character.name} (Necromante) usou {self.attack_skill_name} contra {target.name}, causando {damage} de dano e restaurando 5 de vida!")
        target.health -= damage
        character.health += 5
        self.turns_since_last_ultimate += 1
        self.check_ultimate_ready(character)

    def calculate_damage(self):
        return 18

    def ultimate(self, character, target):
        if not character.ultimate_ready:
            print(f"{character.name} tentou usar {self.ultimate_skill_name}, mas ela ainda não está pronta!")
            return
        print(f"{character.name} (Necromante) conjurou {self.ultimate_skill_name}, invocando aliados sombrios para lutar ao seu lado!")
        character.ultimate_ready = False
        self.turns_since_last_ultimate = 0

    def check_ultimate_ready(self, character):
        if self.turns_since_last_ultimate >= 5:
            character.ultimate_ready = True
            print(f"A ultimate {self.ultimate_skill_name} de {character.name} está pronta!")
            self.turns_since_last_ultimate = 0
