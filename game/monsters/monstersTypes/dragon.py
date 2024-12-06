from ..baseMonster import BaseMonster

class Dragon(BaseMonster):
    def __init__(self):
        super().__init__(name="Dragão", base_health=300, base_attack=25, base_defense=20)

    def special_ability(self, target):
        """Sopro de Fogo: Causa dano massivo ignorando a defesa."""
        damage = 40  # Dano fixo ignorando defesa
        target.health -= damage
        print(f"{self.name} usou Sopro de Fogo em {target.name}, causando {damage} de dano ignorando defesa!")
