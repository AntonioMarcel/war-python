from .deck import Deck
from .player import Player
from utils import MAX_ROUNDS

class Game:
    def __init__(self, player1: str, player2: str):
        self.player1 = Player(player1)  
        self.player2 = Player(player2)
        self.deck = Deck()
        self.deck.shuffle()
        self.round_counter = 0

    def setup_game(self):
        for _ in range(26):
            self.player1.receive_card(self.deck.deal())        

        for _ in range(26):
            self.player2.receive_card(self.deck.deal())

    def play_round(self):
        self.round_counter += 1
        print(f"Round {self.round_counter}")
        
        # Show players' current number of cards
        print(f"--- New Round ---")
        print(f"{self.player1}")
        print(f"{self.player2}")
        
        c1 = self.player1.play_card()
        c2 = self.player2.play_card()

        print(f"{self.player1.name} played: {c1}")
        print(f"{self.player2.name} played: {c2}")

        table_cards = [c1, c2]

        if c1.value > c2.value:
            print(f"{self.player1.name} wins the round!")
            print(f"{self.player1.name} receives {len(table_cards)} cards")

            self.player1.receive_cards(table_cards)
        elif c2.value > c1.value:
            print(f"{self.player2.name} wins the round!")
            print(f"{self.player2.name} receives {len(table_cards)} cards")

            self.player2.receive_cards(table_cards)
        else: # war
            print(f"WAR! Both players played cards with the same value!")
            self.handle_war(table_cards)

        print(f"After round:")
        print(f"{self.player1}")
        print(f"{self.player2}")
        print("")

    def handle_war(self, table_cards: list):
        if self.player1.can_play_war() and self.player2.can_play_war():

            print("---War!---")
            print(f"{self.player1}")
            print(f"{self.player2}")

            print("Each player places 3 cards face down")

            for _ in range(3):
                table_cards.append(self.player1.play_card())
                table_cards.append(self.player2.play_card())

            c1 = self.player1.play_card()
            c2 = self.player2.play_card()

            table_cards.append(c1)
            table_cards.append(c2)

            print(f"{self.player1.name} played: {c1}")
            print(f"{self.player2.name} played: {c2}")

            print(f"Cards currently on table: {len(table_cards)}")

            if c1.value > c2.value:
                print(f"{self.player1.name} wins the WAR!")
                print(f"{self.player1.name} receives {len(table_cards)} cards")

                self.player1.receive_cards(table_cards)
            elif c2.value > c1.value:
                print(f"{self.player2.name} wins the WAR!")
                print(f"{self.player2.name} receives {len(table_cards)} cards")

                self.player2.receive_cards(table_cards)
            else: # novo war (recursão)
                print("Another WAR has started!")
                self.handle_war(table_cards)

            print(f"After WAR:")
            print(f"{self.player1}")
            print(f"{self.player2}")
            print("")

        else:
            if not self.player1.can_play_war():
                print(f"{self.player1.name} does not have enough cards for WAR! {self.player2.name} wins the game!")
                self.player2.receive_cards(table_cards + self.player1.hand)
                self.player1.hand.clear()
            else:
                print(f"{self.player2.name} does not have enough cards for WAR! {self.player1.name} wins the game!")
                self.player1.receive_cards(table_cards + self.player2.hand)
                self.player2.hand.clear()

    def play(self):
        self.setup_game()

        # Play until one player runs out of cards
        while self.player1.has_cards() and self.player2.has_cards() and self.round_counter < MAX_ROUNDS:  # safety limit to prevent infinite games
            self.play_round()

        if self.round_counter >= MAX_ROUNDS:
            print("Maximum rounds reached. It's a draw!")
        elif self.player1.has_cards():
            print(f"{self.player1.name} wins the game!")
        else:            
            print(f"{self.player2.name} wins the game!")   

