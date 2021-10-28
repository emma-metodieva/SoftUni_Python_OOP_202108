import unittest
from project.player.advanced import Advanced
from project.card.card_repository import CardRepository


class AdvancedTests(unittest.TestCase):
    def setUp(self) -> None:
        self.advanced = Advanced("Test")

    def test_advanced_init_attributes(self):
        self.assertEqual("Test", self.advanced.username)
        self.assertEqual(250, self.advanced.health)
        self.assertIsInstance(self.advanced.card_repository, CardRepository)
        self.assertEqual(0, self.advanced.card_repository.count)
        self.assertEqual([], self.advanced.card_repository.cards)

    def test_advanced_is_dead_prop(self):
        self.assertFalse(self.advanced.is_dead)
        self.advanced.health = 0
        self.assertTrue(self.advanced.is_dead)

    def test_advanced_name_empty_str_raises(self):
        with self.assertRaises(ValueError) as ex:
            advanced = Advanced("")
        self.assertEqual("Player's username cannot be an empty string.", str(ex.exception))

    def test_advanced_negative_health_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.advanced.health = -100
        self.assertEqual("Player's health bonus cannot be less than zero.", str(ex.exception))

    def test_advanced_take_damage(self):
        self.advanced.take_damage(50)
        self.assertEqual(200, self.advanced.health)

    def test_advanced_take_negative_damage_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.advanced.take_damage(-50)
        self.assertEqual("Damage points cannot be less than zero.", str(ex.exception))


if __name__ == "__main__":
    unittest.main()