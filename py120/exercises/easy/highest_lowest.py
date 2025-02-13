"""
- init deck
- shuffle deck
- try to draw one card from shuffled deck
    if deck empty
        reinit deck
        shuffle deck
        draw a card from new deck
    else
        return card

"""

import random

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self.shuffled_deck = [Card(rank, suit) for suit in Deck.SUITS for rank in Deck.RANKS]
        random.shuffle(self.shuffled_deck)
    
    def draw(self):
        if not self.shuffled_deck:
            self.__init__()
        self.drawn_card = self.shuffled_deck.pop()
        return self.drawn_card

class Card:
    RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = Card.RANKS.index(self.rank)

    def __str__(self):
        return f'{self.rank} of {self.suit}'

    def __lt__(self, other):
        return self.value < other.value
    
    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit

deck = Deck()
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print((count_rank_5) == 4)     # True
print((count_hearts) == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).