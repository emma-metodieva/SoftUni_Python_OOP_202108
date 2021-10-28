import unittest
from project.controller import Controller
# from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class ControllerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.controller = Controller()

    def test_controller_init_attributes(self):
        self.assertIsInstance(self.controller.player_repository, PlayerRepository)
        self.assertEqual(0, self.controller.player_repository.count)
        self.assertEqual([], self.controller.player_repository.players)
        self.assertIsInstance(self.controller.card_repository, CardRepository)
        self.assertEqual(0, self.controller.card_repository.count)
        self.assertEqual([], self.controller.card_repository.cards)

    def test_controller_add_player_beginner(self):
        self.assertEqual("Successfully added player of type Beginner with username: B",
                         self.controller.add_player("Beginner", "B"))
        self.assertEqual(1, self.controller.player_repository.count)
        self.assertIsInstance(self.controller.player_repository.players[0], Beginner)
        self.assertEqual("B", self.controller.player_repository.players[0].username)

    def test_controller_add_player_advanced(self):
        self.assertEqual("Successfully added player of type Advanced with username: A",
                         self.controller.add_player("Advanced", "A"))
        self.assertEqual(1, self.controller.player_repository.count)
        self.assertIsInstance(self.controller.player_repository.players[0], Advanced)
        self.assertEqual("A", self.controller.player_repository.players[0].username)

    def test_controller_add_magic_card(self):
        self.assertEqual("Successfully added card of type MagicCard with name: M",
                         self.controller.add_card("Magic", "M"))
        self.assertEqual(1, self.controller.card_repository.count)
        self.assertIsInstance(self.controller.card_repository.cards[0], MagicCard)
        self.assertEqual("M", self.controller.card_repository.cards[0].name)

    def test_controller_add_trap_card(self):
        self.assertEqual("Successfully added card of type TrapCard with name: T",
                         self.controller.add_card("Trap", "T"))
        self.assertEqual(1, self.controller.card_repository.count)
        self.assertIsInstance(self.controller.card_repository.cards[0], TrapCard)
        self.assertEqual("T", self.controller.card_repository.cards[0].name)

    def test_controller_add_player_card(self):
        self.controller.add_player("Beginner", "B")
        self.controller.add_card("Magic", "M")
        self.assertEqual("Successfully added card: M to user: B", self.controller.add_player_card("B", "M"))
        self.assertEqual(1, self.controller.player_repository.players[0].card_repository.count)
        self.assertIsInstance(self.controller.player_repository.players[0].card_repository.cards[0], MagicCard)
        self.assertEqual("M", self.controller.player_repository.players[0].card_repository.cards[0].name)

    def test_controller_fight(self):
        self.controller.add_player("Beginner", "B")
        self.controller.add_player("Beginner", "A")
        self.controller.add_card("Magic", "M")
        self.controller.add_card("Trap", "T")
        self.controller.add_player_card("B", "T")
        self.controller.add_player_card("A", "M")

        self.assertEqual("Attack user health 60 - Enemy user health 20",
                         self.controller.fight("B", "A"))

    def test_controller_fight_dead_raises(self):
        self.controller.add_player("Beginner", "B")
        self.controller.add_player("Beginner", "A")
        self.controller.add_card("Magic", "M")
        self.controller.add_card("Trap", "T")
        self.controller.add_player_card("B", "T")
        self.controller.add_player_card("A", "M")

        self.controller.player_repository.players[1].health = 0
        self.assertTrue(self.controller.player_repository.players[1].is_dead)

        with self.assertRaises(ValueError) as ex:
            self.controller.fight("B", "A")
        self.assertEqual("Player is dead!", str(ex.exception))

    def test_controller_report(self):
        self.controller.add_player("Beginner", "B")
        self.controller.add_player("Beginner", "A")
        self.controller.add_card("Magic", "M")
        self.controller.add_card("Trap", "T")
        self.controller.add_player_card("B", "T")
        self.controller.add_player_card("A", "M")

        expected_result = f"Username: B - Health: 50 - Cards 1\n" \
                          f"### Card: T - Damage: 120\n" \
                          f"Username: A - Health: 50 - Cards 1\n" \
                          f"### Card: M - Damage: 5\n"

        self.assertEqual(expected_result, self.controller.report())


if __name__ == "__main__":
    unittest.main()