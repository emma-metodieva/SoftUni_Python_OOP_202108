import unittest
from project.player.player_repository import PlayerRepository
from project.player.beginner import Beginner


class PlayerRepositoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.player_repository = PlayerRepository()

    def test_player_repository_init_attributes(self):
        self.assertEqual(0, self.player_repository.count)
        self.assertEqual([], self.player_repository.players)

    def test_player_repository_add(self):
        player = Beginner("Test")
        self.player_repository.add(player)
        self.assertEqual(1, self.player_repository.count)
        self.assertEqual([player], self.player_repository.players)

    def test_player_repository_add_existing_player_raises(self):
        player = Beginner("Test")
        self.player_repository.add(player)
        with self.assertRaises(ValueError) as ex:
            self.player_repository.add(player)
        self.assertEqual("Player Test already exists!", str(ex.exception))

    def test_player_repository_remove(self):
        player = Beginner("Test")
        self.player_repository.add(player)
        self.player_repository.remove("Test")
        self.assertEqual(0, self.player_repository.count)
        self.assertEqual([], self.player_repository.players)

    def test_player_repository_remove_empty_string_for_username_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.player_repository.remove("")
        self.assertEqual("Player cannot be an empty string!", str(ex.exception))

    def test_player_repository_find(self):
        player = Beginner("Test")
        self.player_repository.add(player)
        self.assertEqual(player, self.player_repository.find("Test"))


if __name__ == "__main__":
    unittest.main()