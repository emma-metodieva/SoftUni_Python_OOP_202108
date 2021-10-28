import unittest

from project.rooms.room import Room
from project.people.child import Child
from project.appliances.fridge import Fridge


class RoomTests(unittest.TestCase):
    def setUp(self) -> None:
        self.room = Room("Test", 100, 2)

    def test_room_init_attributes(self):
        self.assertEqual("Test", self.room.family_name)
        self.assertEqual(100, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_room_expenses_set_with_valid_properties(self):
        self.room.expenses = 10
        self.assertEqual(10, self.room.expenses)

    def test_room_expenses_set_with_invalid_properties_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -10
        self.assertEqual("Expenses cannot be negative", str(ex.exception))
        self.assertEqual(0, self.room.expenses)

    def test_room_calculate_expenses(self):
        child = Child(5, 1.2)
        fridge = Fridge()
        self.room.expenses = self.room.calculate_expenses([child], [fridge])
        self.assertEqual(222.0, self.room.expenses)

    def test_room_calculate_expenses_with_no_args(self):
        self.room.expenses = self.room.calculate_expenses()
        self.assertEqual(0, self.room.expenses)


if __name__ == "__main__":
    unittest.main()