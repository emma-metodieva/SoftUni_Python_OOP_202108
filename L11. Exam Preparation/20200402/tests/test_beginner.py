import unittest
from project.player.beginner import Beginner
from project.card.card_repository import CardRepository


class AdvancedTests(unittest.TestCase):
    def setUp(self) -> None:
        self.beginner = Beginner("Test")

    def test_beginner_init_attributes(self):
        self.assertEqual("Test", self.beginner.username)
        self.assertEqual(50, self.beginner.health)
        self.assertIsInstance(self.beginner.card_repository, CardRepository)
        self.assertEqual(0, self.beginner.card_repository.count)
        self.assertEqual([], self.beginner.card_repository.cards)

    def test_beginner_is_dead_prop(self):
        self.assertFalse(self.beginner.is_dead)
        self.beginner.health = 0
        self.assertTrue(self.beginner.is_dead)

    def test_beginner_name_empty_str_raises(self):
        with self.assertRaises(ValueError) as ex:
            beginner = Beginner("")
        self.assertEqual("Player's username cannot be an empty string.", str(ex.exception))

    def test_beginner_negative_health_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.beginner.health = -100
        self.assertEqual("Player's health bonus cannot be less than zero.", str(ex.exception))

    def test_beginner_take_damage(self):
        self.beginner.take_damage(5)
        self.assertEqual(45, self.beginner.health)

    def test_beginner_take_negative_damage_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.beginner.take_damage(-5)
        self.assertEqual("Damage points cannot be less than zero.", str(ex.exception))


if __name__ == "__main__":
    unittest.main()