from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    # @property
    # def count(self):
    #     return len(self.cards)

    def add(self, card: Card):
        add_card_name = card.name
        card_names = [c.name for c in self.cards]

        if add_card_name in card_names:
            raise ValueError(f"Card {add_card_name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, name: str):
        if name == '':
            raise ValueError("Card cannot be an empty string!")

        card_to_remove = self.find(name)
        self.cards.remove(card_to_remove)
        self.count -= 1

    def find(self, name: str):
        card = [c for c in self.cards if c.name == name][0]
        return card
