class BaseRace:
    def __init__(self, name, base_health, base_attack, base_defense):
        self.name = name
        self.base_health = base_health
        self.base_attack = base_attack
        self.base_defense = base_defense

    def attack(self, character, target):
        raise NotImplementedError("Ataque de raça não implementado.")
