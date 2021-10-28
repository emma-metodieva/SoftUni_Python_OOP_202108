import unittest
from project.battle_field import BattleField
from project.player.beginner import Beginner
from project.player.advanced import Advanced
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard


class BattleFieldTests(unittest.TestCase):
    def setUp(self) -> None:
        self.beginner = Beginner("B")
        self.advanced = Advanced("A")
        self.magic_card = MagicCard("M")
        self.trap_card = TrapCard("T")
        self.beginner.card_repository.add(self.trap_card)
        self.advanced.card_repository.add(self.magic_card)

    def test_battle_field_dead_player_raises(self):
        self.advanced.health = 0
        self.assertTrue(self.advanced.is_dead)
        with self.assertRaises(ValueError) as ex:
            BattleField.fight(self.beginner, self.advanced)
        self.assertEqual("Player is dead!", str(ex.exception))

    def test_battle_field_increase_beginners_health(self):
        BattleField.fight(self.beginner, self.advanced)
        self.assertEqual(90, self.beginner.health)

    def test_battle_field_increase_beginners_card_damage_points(self):
        BattleField.fight(self.beginner, self.advanced)
        self.assertEqual(150, self.beginner.card_repository.find("T").damage_points)

    def test_battle_field_health_after_fight(self):
        BattleField.fight(self.beginner, self.advanced)
        self.assertEqual(90, self.beginner.health)
        self.assertEqual(180, self.advanced.health)


if __name__ == "__main__":
    unittest.main()