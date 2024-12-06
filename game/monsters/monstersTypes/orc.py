from ..baseMonster import BaseMonster

class Orc(BaseMonster):
    def __init__(self):
        super().__init__(name="Orc", base_health=120, base_attack=15, base_defense=8)

    def special_ability(self, target):
        """Grito de Guerra: Aumenta o ataque por 5 turnos."""
        self.attack_power += 5
        print(f"{self.name} usou Grito de Guerra! Seu ataque aumentou para {self.attack_power} por 5 turnos.")
