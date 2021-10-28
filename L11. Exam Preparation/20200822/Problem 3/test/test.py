import unittest

from project.room import Room
from project.room import Child
from project.room import Fridge


class RoomTests(unittest.TestCase):
    def setUp(self) -> None:
        self.room = Room("Test", 100, 2)

    def test_room_init_attributes(self):
        self.assertEqual("Test", self.room.family_name)
        self.assertEqual(100, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room._expenses)

    def test_room_expenses_set_with_valid_properties(self):
        self.room.expenses = 10
        self.assertEqual(10, self.room.expenses)

    def test_room_expenses_set_with_invalid_properties(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -10
        self.assertEqual("Expenses cannot be negative", str(ex.exception))
        self.assertEqual(0, self.room._expenses)

    def test_room_calculate_expenses(self):
        child = Child(5, 1.2)
        self.room.calculate_expenses([child])
        self.assertEqual(186.0, self.room.expenses)


if __name__ == "__main__":
    unittest.main()