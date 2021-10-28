# L10-01. Unit Testing - Lab
# 02. Test Cat

class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):

    def setUp(self) -> None:
        self.cat = Cat("Test")

    def test_cat_init_creates_all_attributes(self):
        self.assertEqual("Test", self.cat.name)
        self.assertFalse(self.cat.sleepy)
        self.assertFalse(self.cat.fed)
        self.assertEqual(0, self.cat.size)

    def test_cat_size_is_increased_after_eat(self):
        self.assertEqual(0, self.cat.size)
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_cat_is_fed_after_eat(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_if_fed_raises(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        expected_result = "Already fed."
        self.assertEqual(expected_result, str(ex.exception))

    def test_cat_cannot_sleep_if_not_fed_raises(self):
        self.assertFalse(self.cat.fed)
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        expected_result = "Cannot sleep while hungry"
        self.assertEqual(expected_result, str(ex.exception))

    def test_cat_is_not_sleepy_after_sleep(self):
        self.assertFalse(self.cat.sleepy)
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()
