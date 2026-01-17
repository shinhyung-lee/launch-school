from random import shuffle

class Card:
    VALUES = {
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        'Jack': 11,
        'Queen': 12,
        'King': 13,
        'Ace': 14,
    }
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
    def __lt__(self, other):
        # return self.value < other.value 
        return Card.VALUES[self.rank] < Card.VALUES[other.rank]
    
    def __le__(self, other):
        # return self.value <= other.value
        return Card.VALUES[self.rank] <= Card.VALUES[other.rank]
        
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit
    
    @property 
    def value(self):
        return Card.VALUES.get(self.rank, self.rank)     
    
    
class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self._reset()
        
    def draw(self):
        if not self._deck:
            self._reset()
        
        return self._deck.pop()
    
    def reset(self):
        self._deck = [Card(rank, suit)
                      for rank in Deck.RANKS
                      for suit in Deck.SUITS]
        
        shuffle(self._deck)
        
    
deck = Deck()
# for card in deck.cards:
#     print(card)
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).