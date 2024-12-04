from ..baseClass import BaseClass

class Warrior(BaseClass):
    def __init__(self):
        super().__init__("Guerreiro", base_health=20, base_attack=5, base_defense=5)
        self.attack_skill_name = "Golpe Giratório"
        self.ultimate_skill_name = "Fúria de Batalha"
        self.turns_since_last_ultimate = 0  # Contador para carregar a ultimate

    def attack(self, character, target):
        damage = self.calculate_damage()
        print(f"{character.name} (Guerreiro) usou {self.attack_skill_name} contra {target.name}, causando {damage} de dano!")
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
        print(f"{character.name} (Guerreiro) usou {self.ultimate_skill_name}, causando {damage} de dano massivo!")
        target.health -= damage
        character.ultimate_ready = False  # Reseta o carregamento

    def check_ultimate_ready(self, character):
        """Carrega a ultimate após 3 turnos."""
        if self.turns_since_last_ultimate >= 5:
            character.ultimate_ready = True
            print(f"A ultimate {self.ultimate_skill_name} de {character.name} está pronta!")
            self.turns_since_last_ultimate = 0