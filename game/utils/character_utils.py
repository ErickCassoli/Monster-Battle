from .menu_utils import select_class, select_race
from game.character.baseCharacter import BaseCharacter

def create_character():
    """Criação de personagem com seleção dinâmica de raça e classe."""
    name = input("Digite o nome do personagem: ")
    race = select_race()
    char_class = select_class()
    return BaseCharacter(name, race, char_class)
