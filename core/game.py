from .deck import Deck
from .player import Player

class Game:
    def __init__(self, player1: str, player2: str):
        self.player1 = Player(player1)  
        self.player2 = Player(player2)
        self.deck = Deck()
        self.deck.shuffle()

    def setup_game(self):
        for _ in range(1):
            self.player1.receive_card(self.deck.deal())        
    
        for _ in range(1):
            self.player2.receive_card(self.deck.deal())

    
    def play_round(self):
        # Show players' current number of cards
        print(f"--- New Round ---")
        print(f"{self.player1}")
        print(f"{self.player2}")
        c1 = self.player1.play_card()
        c2 = self.player2.play_card()

        table_cards = [c1, c2]

        if c1.value > c2.value:
            print(f"{self.player1.name} wins with {c1} against {c2}")
            self.player1.receive_cards(table_cards)
        elif c2.value > c1.value:
            print(f"{self.player2.name} wins with {c2} against {c1}")
            self.player2.receive_cards(table_cards)
        else: # war
            print(f"Both players have cards with the same value: {c1} and {c2}")
        
    def play(self):
        self.setup_game()

        # Play until one player runs out of cards
        while self.player1.has_cards() and self.player2.has_cards():
            self.play_round()

        print("Game over!")
