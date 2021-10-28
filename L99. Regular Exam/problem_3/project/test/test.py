import unittest

from project.pet_shop import PetShop


class PetShopTests(unittest.TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop("Test")

    def test_pet_shop_init_attributes(self):
        self.assertEqual("Test", self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_pet_shop_add_food_new_with_valid_quantity(self):
        self.assertEqual("Successfully added 1.50 grams of test_food.", self.pet_shop.add_food("test_food", 1.5))
        self.assertEqual({"test_food": 1.5}, self.pet_shop.food)

    def test_pet_shop_add_food_existing_with_valid_quantity(self):
        self.pet_shop.add_food("test_food", 1.5)
        self.assertEqual("Successfully added 1.50 grams of test_food.", self.pet_shop.add_food("test_food", 1.5))
        self.assertEqual({"test_food": 3}, self.pet_shop.food)

    def test_pet_shop_add_food_with_invalid_quantity(self):
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food("test_food", 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))
        self.assertEqual({}, self.pet_shop.food)

    def test_pet_shop_add_pet_new(self):
        self.assertEqual("Successfully added Eeyore.", self.pet_shop.add_pet("Eeyore"))
        self.assertEqual(["Eeyore"], self.pet_shop.pets)

    def test_pet_shop_add_pet_existing_raises(self):
        self.pet_shop.add_pet("Eeyore")
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Eeyore")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))
        self.assertEqual(["Eeyore"], self.pet_shop.pets)

    def test_pet_shop_feed_pet_enough_food_quantity(self):
        self.pet_shop.add_food("test_food", 1001.5)
        self.pet_shop.add_pet("Eeyore")
        self.assertEqual("Eeyore was successfully fed", self.pet_shop.feed_pet("test_food", "Eeyore"))
        self.assertEqual({"test_food": 901.5}, self.pet_shop.food)

    def test_pet_shop_feed_pet_not_enough_food_quantity(self):
        self.pet_shop.add_food("test_food", 1.5)
        self.pet_shop.add_pet("Eeyore")
        self.assertEqual("Adding food...", self.pet_shop.feed_pet("test_food", "Eeyore"))
        self.assertEqual({"test_food": 1001.5}, self.pet_shop.food)

    def test_pet_shop_feed_pet_not_existing_raises(self):
        self.pet_shop.add_food("test_food", 1.5)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("test_food", "Eeyore")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))
        self.assertEqual({"test_food": 1.5}, self.pet_shop.food)

    def test_pet_shop_feed_pet_not_existing_food(self):
        self.pet_shop.add_pet("Eeyore")
        self.assertEqual('You do not have test_food', self.pet_shop.feed_pet("test_food", "Eeyore"))
        self.assertEqual({}, self.pet_shop.food)

    def test_pet_shop_repr(self):
        self.pet_shop.add_pet("Eeyore")
        self.pet_shop.add_pet("Murphy")
        self.assertEqual(f"Shop Test:\nPets: Eeyore, Murphy", self.pet_shop.__repr__())


if __name__ == "__main__":
    unittest.main()
