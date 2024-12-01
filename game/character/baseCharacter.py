from game.character import BaseRace
from game.character import BaseClass

class BaseCharacter:
    def __init__(self, name, race, char_class):
        if not isinstance(race, BaseRace):
            raise ValueError("race must be an instance of BaseRace.")
        if not isinstance(char_class, BaseClass):
            raise ValueError("char_class must be an instance of BaseClass.")
        
        self.name = name
        self.race = race
        self.char_class = char_class
        self.health = 100 + race.base_health + char_class.base_health
        self.attack_power = 10 + race.base_attack + char_class.base_attack
        self.defense = 5 + race.base_defense + char_class.base_defense
        self.ultimate_ready = False

    def basic_attack(self, target):
        damage = max(0, self.attack_power - target.defense)
        target.health -= damage
        print(f"{self.name} realizou um ataque básico contra {target.name}, causando {damage} de dano!")

    def race_attack(self, target):
        self.race.attack(self, target)

    def class_attack(self, target):
        self.char_class.attack(self, target)

    def ultimate(self, target):
        if not self.ultimate_ready:
            print(f"{self.name} tentou usar a Ultimate, mas ela ainda não está pronta!")
            return
        self.char_class.ultimate(self, target)
        self.ultimate_ready = False