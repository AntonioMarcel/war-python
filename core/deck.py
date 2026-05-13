import random
from .card import Card
from utils import SUITS, RANKS

class Deck:
    def __init__(self):
        self.cards = []    
        self.build()

    def build(self):
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()
    
    def __str__(self):
        for card in self.cards:
            print(card)
        return f"Deck of {len(self.cards)} cards"

        