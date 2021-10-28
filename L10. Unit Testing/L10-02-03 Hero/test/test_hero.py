import unittest
from project.hero import Hero


class HeroTest(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Gelman", 100, 5, 0.1)
        self.enemy_hero = Hero("Gelman's enemy", 100, 5, 0.1)
        self.strong_enemy_hero = Hero("Gelman's enemy", 100, 50, 0.5)
        self.weak_enemy_hero = Hero("Gelman's enemy", 100, 1, 0.01)

    def test_hero_init_attributes(self):
        self.assertEqual("Gelman", self.hero.username)
        self.assertEqual(100, self.hero.level)
        self.assertEqual(5, self.hero.health)
        self.assertEqual(0.1, self.hero.damage)

    def test_hero_battle_with_invalid_enemy_raises(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle("Gelman's enemy")

    def test_hero_battle_against_himself_raises(self):
        enemy_hero = self.hero
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_battle_with_no_health(self):
        health_values = [0, -1]
        for health_value in health_values:
            self.hero.health = health_value
            with self.assertRaises(ValueError) as ex:
                self.hero.battle(self.enemy_hero)
            self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_hero_battle_against_enemy_with_no_health(self):
        health_values = [0, -1]
        for health_value in health_values:
            self.enemy_hero.health = health_value
            with self.assertRaises(ValueError) as ex:
                self.hero.battle(self.enemy_hero)
            self.assertEqual("You cannot fight Gelman's enemy. He needs to rest", str(ex.exception))

    def test_hero_battle_hero_lose(self):
        self.assertEqual("You lose", self.hero.battle(self.strong_enemy_hero))

        self.assertEqual(-45.0, self.hero.health)
        self.assertEqual(100, self.hero.level)
        self.assertEqual(0.1, self.hero.damage)

        self.assertEqual(45.0, self.strong_enemy_hero.health)
        self.assertEqual(101, self.strong_enemy_hero.level)
        self.assertEqual(5.5, self.strong_enemy_hero.damage)

    def test_hero_battle_hero_win(self):
        self.assertEqual("You win", self.hero.battle(self.weak_enemy_hero))

        self.assertEqual(9.0, self.hero.health)
        self.assertEqual(101, self.hero.level)
        self.assertEqual(5.1, self.hero.damage)

        self.assertEqual(-9.0, self.weak_enemy_hero.health)
        self.assertEqual(100, self.weak_enemy_hero.level)
        self.assertEqual(0.01, self.weak_enemy_hero.damage)

    def test_hero_battle_draw(self):
        self.assertEqual("Draw", self.hero.battle(self.enemy_hero))

        self.assertEqual(-5.0, self.hero.health)
        self.assertEqual(100, self.hero.level)
        self.assertEqual(0.1, self.hero.damage)

        self.assertEqual(-5.0, self.enemy_hero.health)
        self.assertEqual(100, self.enemy_hero.level)
        self.assertEqual(0.1, self.enemy_hero.damage)

    def test_hero_str(self):
        expected_result = "Hero Gelman: 100 lvl\n"\
                          "Health: 5\n" \
                          "Damage: 0.1\n"
        self.assertEqual(expected_result, self.hero.__str__())


if __name__ == "__main__":
    unittest.main()
