from ..baseMonster import BaseMonster

class Lich(BaseMonster):
    def __init__(self):
        super().__init__(name="Lich", base_health=100, base_attack=10, base_defense=12)

    def special_ability(self, target):
        """Ressurgir: Restaura parte da sua própria vida ao absorver energia do alvo."""
        life_steal = 20
        target.health -= life_steal
        self.health += life_steal
        print(f"{self.name} usou Ressurgir em {target.name}! Absorveu {life_steal} de vida.")
