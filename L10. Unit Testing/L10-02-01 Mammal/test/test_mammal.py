from project.mammal import Mammal

import unittest


class MammalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Eeyore", "dog", "Bark!")

    def test_mammal_init_attributes(self):
        self.assertEqual("Eeyore", self.mammal.name)
        self.assertEqual("dog", self.mammal.type)
        self.assertEqual("Bark!", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_mammal_make_sound(self):
        expected_result = "Eeyore makes Bark!"
        self.assertEqual(expected_result, self.mammal.make_sound())

    def test_mammal_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_mammal_info(self):
        expected_result = "Eeyore is of type dog"
        self.assertEqual(expected_result, self.mammal.info())


if __name__ == "__main__":
    unittest.main()
