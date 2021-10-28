import unittest

from project.factory.paint_factory import PaintFactory


class PaintFactoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.paint_factory = PaintFactory("Test", 2)

    def test_paint_factory_init_attributes(self):
        self.assertEqual("Test", self.paint_factory.name)
        self.assertEqual(2, self.paint_factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)
        self.assertEqual({}, self.paint_factory.ingredients)

    def test_paint_factory_add_valid_new_ingredient_when_capacity_available(self):
        self.paint_factory.add_ingredient("white", 1)
        self.assertEqual({"white": 1}, self.paint_factory.ingredients)

    def test_paint_factory_add_valid_existing_ingredient_when_capacity_available(self):
        self.paint_factory.add_ingredient("white", 1)
        self.paint_factory.add_ingredient("white", 1)
        self.assertEqual({"white": 2}, self.paint_factory.ingredients)

    def test_paint_factory_add_valid_new_ingredient_when_no_capacity_available_raises(self):
        self.paint_factory.add_ingredient("white", 2)
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.add_ingredient("yellow", 1)
        self.assertEqual("Not enough space in factory", str(ex.exception))
        self.assertEqual({"white": 2}, self.paint_factory.ingredients)

    def test_paint_factory_add_valid_existing_ingredient_when_no_capacity_available_raises(self):
        self.paint_factory.add_ingredient("white", 2)
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.add_ingredient("white", 1)
        self.assertEqual("Not enough space in factory", str(ex.exception))
        self.assertEqual({"white": 2}, self.paint_factory.ingredients)

    def test_paint_factory_add_invalid_ingredient_raises(self):
        with self.assertRaises(TypeError) as ex:
            self.paint_factory.add_ingredient("black", 1)
        self.assertEqual("Ingredient of type black not allowed in PaintFactory", str(ex.exception))
        self.assertEqual({}, self.paint_factory.ingredients)

    def test_paint_factory_remove_existing_ingredient_with_enough_quantity(self):
        self.paint_factory.add_ingredient("white", 1)
        self.paint_factory.remove_ingredient("white", 1)
        self.assertEqual({"white": 0}, self.paint_factory.ingredients)

    def test_paint_factory_remove_existing_ingredient_with_not_enough_quantity_raises(self):
        self.paint_factory.add_ingredient("white", 1)
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.remove_ingredient("white", 2)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))
        self.assertEqual({"white": 1}, self.paint_factory.ingredients)

    def test_paint_factory_remove_not_existing_ingredient_raises(self):
        with self.assertRaises(KeyError) as ex:
            self.paint_factory.remove_ingredient("white", 1)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))
        self.assertEqual({}, self.paint_factory.ingredients)

    def test_paint_factory_products_method(self):
        self.assertEqual({}, self.paint_factory.products)

    def test_paint_factory_repr_method(self):
        self.assertEqual("Factory name: Test with capacity 2.\n", self.paint_factory.__repr__())


if __name__ == "__main__":
    unittest.main()
