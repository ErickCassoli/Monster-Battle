import unittest
from game.character.baseCharacter import BaseCharacter
from game.character.races.elf import Elf
from game.character.classes.warrior import Warrior


class TestBaseCharacter(unittest.TestCase):
    def test_character_creation(self):
        race = Elf()
        char_class = Warrior()
        character = BaseCharacter(name="Legolas", race=race, char_class=char_class)
        
        self.assertEqual(character.name, "Legolas")
        self.assertEqual(character.health, 135)  # 100 + 10 (Elf) + 20 (Warrior)
        self.assertEqual(character.attack_power, 20)  # 10 + 5 (Elf) + 5 (Warrior)
        self.assertEqual(character.defense, 12)  # 5 + 2 (Elf) + 5 (Warrior)

    def test_race_attack(self):
        race = Elf()
        char_class = Warrior()
        character = BaseCharacter(name="Legolas", race=race, char_class=char_class)

        target = BaseCharacter(name="Orc", race=Elf(), char_class=Warrior())
        character.race_attack(target)

        self.assertEqual(target.health, 120)  # 135 - 15 (Elf attack)

if __name__ == "__main__":
    unittest.main()
