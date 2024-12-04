import sys
import os
import pytest

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from game.utils.character_utils import create_character
from game.character.classes.warrior import Warrior
from game.character.races.elf import Elf


@pytest.fixture
def mock_input(monkeypatch):
    """
    Mocka as entradas do usuário para a criação de personagem.
    """
    inputs = iter(["TestPlayer", "1", "1"])  # Nome, Classe: Warrior, Raça: Elf
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

def test_create_character(mock_input):
    """
    Testa se a criação do personagem retorna um personagem válido.
    """
    character = create_character()
    
    assert character.name == "TestPlayer", "O nome do personagem está incorreto."
    assert isinstance(character.char_class, Warrior), "A classe do personagem deveria ser Warrior."
    assert isinstance(character.race, Elf), "A raça do personagem deveria ser Elf."
    assert character.health > 0, "O personagem deveria ter saúde inicial maior que 0."
    assert hasattr(character, "basic_attack"), "O personagem deveria possuir o método basic_attack."
    assert hasattr(character, "ultimate"), "O personagem deveria possuir o método ultimate."

