from ..baseClass import BaseClass

class Hunter(BaseClass):
    def __init__(self):
        super().__init__("Caçador", base_health=14, base_attack=6, base_defense=4)
        self.hit_name = "Flecha Veloz"
        self.attack_skill_name = "Disparo Preciso"
        self.ultimate_skill_name = "Chuva de Flechas"
        self.turns_since_last_ultimate = 0

    def attack(self, character, target):
        damage = self.calculate_damage()
        print(f"{character.name} (Caçador) usou {self.attack_skill_name} contra {target.name}, causando {damage} de dano!")
        target.health -= damage
        self.turns_since_last_ultimate += 1
        self.check_ultimate_ready(character)

    def calculate_damage(self):
        return 20

    def ultimate(self, character, target):
        if not character.ultimate_ready:
            print(f"{character.name} tentou usar {self.ultimate_skill_name}, mas ela ainda não está pronta!")
            return
        damage = 50
        print(f"{character.name} (Caçador) lançou {self.ultimate_skill_name}, atingindo todos os inimigos com flechas devastadoras!")
        target.health -= damage
        character.ultimate_ready = False
        self.turns_since_last_ultimate = 0

    def check_ultimate_ready(self, character):
        if self.turns_since_last_ultimate >= 4:
            character.ultimate_ready = True
            print(f"A ultimate {self.ultimate_skill_name} de {character.name} está pronta!")
            self.turns_since_last_ultimate = 0
