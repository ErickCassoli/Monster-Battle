from baseMonster import BaseMonster

class Goblin(BaseMonster):
    def __init__(self):
        super().__init__(name="Goblin", base_health=30, base_attack=5, base_defense=2)

    def special_ability(self, target):
        damage = 10
        target.health -= damage
        print(f"{self.name} usou Corte Selvagem, causando {damage} de dano em {target.name}!")
