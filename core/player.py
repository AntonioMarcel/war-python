from .card import Card

class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []

    def receive_card(self, card: Card):
        self.hand.append(card)

    def receive_cards(self, cards: list[Card]):
        self.hand.extend(cards)

    def has_cards(self):
        return len(self.hand) > 0

    def play_card(self):
        return self.hand.pop(0)
    
    def cards_left(self):
        return len(self.hand)

    def can_play_war(self):
        return len(self.hand) >= 4
    
    def __str__(self):
        return f"{self.name} has {len(self.hand)} cards"