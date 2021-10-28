import unittest
from project.card.trap_card import TrapCard


class TrapCardTests(unittest.TestCase):
    def setUp(self) -> None:
        self.trap_card = TrapCard("Test")

    def test_trap_card_init_attributes(self):
        self.assertEqual("Test", self.trap_card.name)
        self.assertEqual(120, self.trap_card.damage_points)
        self.assertEqual(5, self.trap_card.health_points)

    def test_trap_card__name_empty_str_raises(self):
        with self.assertRaises(ValueError) as ex:
            card = TrapCard("")
        self.assertEqual("Card's name cannot be an empty string.", str(ex.exception))

    def test_trap_card_negative_damage_points_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.trap_card.damage_points = -100
        self.assertEqual("Card's damage points cannot be less than zero.", str(ex.exception))

    def test_trap_card_negative_health_points_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.trap_card.health_points = -100
        self.assertEqual("Card's HP cannot be less than zero.", str(ex.exception))


if __name__ == "__main__":
    unittest.main()