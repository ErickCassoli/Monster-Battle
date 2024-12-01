class BaseMonster:
    def __init__(self, name, base_health, base_attack, base_defense):
        self.name = name
        self.health = base_health
        self.attack_power = base_attack
        self.defense = base_defense

    def attack(self, target):
        damage = max(0, self.attack_power - target.defense)
        target.health -= damage
        print(f"{self.name} atacou {target.name}, causando {damage} de dano!")

    def special_ability(self, target):
        """Habilidade especial do monstro (implementada nas subclasses)"""
        raise NotImplementedError("Habilidade especial não implementada para este monstro.")
