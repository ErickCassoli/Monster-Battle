import importlib
import os

def list_available_classes():
    """Lista todas as classes disponíveis no jogo."""
    path = os.path.join(os.path.dirname(__file__), "../character/classes")
    class_files = [f[:-3] for f in os.listdir(path) if f.endswith(".py") and f != "__init__.py"]
    return class_files

def list_available_races():
    """Lista todas as raças disponíveis no jogo."""
    path = os.path.join(os.path.dirname(__file__), "../character/races")
    race_files = [f[:-3] for f in os.listdir(path) if f.endswith(".py") and f != "__init__.py"]
    return race_files

def select_class():
    """Permite ao jogador selecionar uma classe."""
    classes = list_available_classes()
    print("Escolha uma classe:")
    for idx, cls in enumerate(classes, 1):
        print(f"{idx}. {cls.capitalize()}")
    choice = int(input("Escolha: ")) - 1
    module = importlib.import_module(f"game.character.classes.{classes[choice]}")
    return getattr(module, classes[choice].capitalize())()

def select_race():
    """Permite ao jogador selecionar uma raça."""
    races = list_available_races()
    print("Escolha uma raça:")
    for idx, race in enumerate(races, 1):
        print(f"{idx}. {race.capitalize()}")
    choice = int(input("Escolha: ")) - 1
    module = importlib.import_module(f"game.character.races.{races[choice]}")
    return getattr(module, races[choice].capitalize())()
