import random
from game.card import Card
from utils import SUITS, RANKS

class Deck:
    def __init__(self):
        self.cards = []    
        self.build()

    def build(self):
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                print(card)
                self.cards.append(card)
        print(len(self.cards))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() 


        