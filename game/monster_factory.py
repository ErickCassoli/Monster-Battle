import random
from .monsters.monstersTypes.goblin import Goblin

class MonsterFactory:
    @staticmethod
    def create_monster(wave):
        """Cria um monstro baseado na dificuldade da wave"""
        monsters = [Goblin()]

        # Escolhe um monstro aleatório
        monster = random.choice(monsters)

        # Escala os atributos do monstro com base na wave
        monster.health += wave * 10
        monster.attack_power += wave * 2
        monster.defense += wave

        return monster
