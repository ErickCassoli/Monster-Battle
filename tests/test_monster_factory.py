import pytest
from game.monsters.monstersTypes.goblin import Goblin
from game.monsters.monstersTypes.dragon import Dragon
from game.monsters.monstersTypes.lich import Lich
from game.monsters.monstersTypes.orc import Orc
from game.monster_factory import MonsterFactory

@pytest.fixture
def monster_classes():
    """Fixture que retorna as classes de monstros disponíveis."""
    return [Goblin, Dragon, Lich, Orc]

def test_create_monster_returns_valid_monster(monster_classes):
    """
    Testa se a fábrica retorna um monstro válido.
    """
    monster = MonsterFactory.create_monster(wave=1)
    assert any(isinstance(monster, cls) for cls in monster_classes), "A fábrica deve retornar uma instância válida de monstro."

def test_create_monster_attribute_scaling():
    """
    Testa se os atributos do monstro são escalados corretamente com base na wave.
    """
    wave = 3
    monster = MonsterFactory.create_monster(wave)

    assert monster.health >= 30, "A saúde do monstro deveria ser maior ou igual a 30."
    assert monster.attack_power >= 6, "O ataque do monstro deveria ser maior ou igual a 6."
    assert monster.defense >= 3, "A defesa do monstro deveria ser maior ou igual a 3."

def test_create_monster_random(monster_classes):
    """
    Testa se a fábrica está retornando monstros diferentes ao longo de múltiplas execuções.
    """
    monsters = {type(MonsterFactory.create_monster(wave=1)) for _ in range(10)}
    assert len(monsters) > 1, "A fábrica deveria retornar mais de um tipo de monstro após múltiplas execuções."

def test_create_monster_scaling_values():
    """
    Testa se o cálculo de atributos está correto para uma wave alta.
    """
    wave = 10
    monster = MonsterFactory.create_monster(wave)

    assert monster.health == monster.__class__().health + wave * 10, "A saúde não foi escalada corretamente."
    assert monster.attack_power == monster.__class__().attack_power + wave * 2, "O ataque não foi escalado corretamente."
    assert monster.defense == monster.__class__().defense + wave, "A defesa não foi escalada corretamente."
