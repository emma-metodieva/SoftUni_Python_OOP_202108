from project.player.beginner import Beginner
from project.player.player import Player


class BattleField:

    @staticmethod
    def fight(attacker: Player, enemy: Player):

        players = [attacker, enemy]

        for player in players:
            if player.is_dead:
                raise ValueError("Player is dead!")

        for player in players:
            if isinstance(player, Beginner):
                player.health += 40
                for card in player.card_repository.cards:
                    card.damage_points += 30

        for player in players:
            for card in player.card_repository.cards:
                player.health += card.health_points

        for card in attacker.card_repository.cards:
            enemy.take_damage(card.damage_points)
            if enemy.is_dead:
                return

        for card in enemy.card_repository.cards:
            attacker.take_damage(card.damage_points)
            if attacker.is_dead:
                return
