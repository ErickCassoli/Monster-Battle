import random
from .monsters.monstersTypes.goblin import Goblin
from .monsters.monstersTypes.dragon import Dragon
from .monsters.monstersTypes.lich import Lich
from .monsters.monstersTypes.orc import Orc

class MonsterFactory:
    @staticmethod
    def create_monster(wave):
        """Cria um monstro baseado na dificuldade da wave"""
        monsters = [Goblin(), Dragon(), Lich(), Orc()]

        # Escolhe um monstro aleatório
        monster = random.choice(monsters)

        # Escala os atributos do monstro com base na wave
        monster.health += wave * 10
        monster.attack_power += wave * 2
        monster.defense += wave

        return monster
