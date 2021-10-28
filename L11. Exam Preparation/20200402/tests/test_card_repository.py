import unittest
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class CardRepositoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.card_repository = CardRepository()

    def test_card_repository_init_attributes(self):
        self.assertEqual(0, self.card_repository.count)
        self.assertEqual([], self.card_repository.cards)

    def test_card_repository_add(self):
        card = MagicCard("Test")
        self.card_repository.add(card)
        self.assertEqual(1, self.card_repository.count)
        self.assertEqual([card], self.card_repository.cards)

    def test_card_repository_add_existing_card_raises(self):
        card = MagicCard("Test")
        self.card_repository.add(card)
        with self.assertRaises(ValueError) as ex:
            self.card_repository.add(card)
        self.assertEqual("Card Test already exists!", str(ex.exception))

    def test_card_repository_remove(self):
        card = MagicCard("Test")
        self.card_repository.add(card)
        self.card_repository.remove("Test")
        self.assertEqual(0, self.card_repository.count)
        self.assertEqual([], self.card_repository.cards)

    def test_card_repository_remove_empty_string_for_username_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.card_repository.remove("")
        self.assertEqual("Card cannot be an empty string!", str(ex.exception))

    def test_card_repository_find(self):
        card = MagicCard("Test")
        self.card_repository.add(card)
        self.assertEqual(card, self.card_repository.find("Test"))


if __name__ == "__main__":
    unittest.main()