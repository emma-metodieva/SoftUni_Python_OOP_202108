import unittest
from project.card.magic_card import MagicCard


class MagicCardTests(unittest.TestCase):
    def setUp(self) -> None:
        self.magic_card = MagicCard("Test")

    def test_magic_card_init_attributes(self):
        self.assertEqual("Test", self.magic_card.name)
        self.assertEqual(5, self.magic_card.damage_points)
        self.assertEqual(80, self.magic_card.health_points)

    def test_magic_card__name_empty_str_raises(self):
        with self.assertRaises(ValueError) as ex:
            card = MagicCard("")
        self.assertEqual("Card's name cannot be an empty string.", str(ex.exception))

    def test_magic_card_negative_damage_points_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.magic_card.damage_points = -100
        self.assertEqual("Card's damage points cannot be less than zero.", str(ex.exception))

    def test_magic_card_negative_health_points_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.magic_card.health_points = -100
        self.assertEqual("Card's HP cannot be less than zero.", str(ex.exception))


if __name__ == "__main__":
    unittest.main()