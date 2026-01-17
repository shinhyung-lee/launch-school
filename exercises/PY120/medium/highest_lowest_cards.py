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
        self.cards = self.generate_cards()
        
    def generate_cards(self):
        cards = [ Card(rank, suit) 
                    for rank in self.__class__.RANKS 
                    for suit in self.__class__.SUITS ]
        shuffle(cards)
        return cards
    
    def draw(self):
        if len(self.cards) == 0:
            self.cards = self.generate_cards()
            
        card = self.cards.pop(0)
        return card
        
    
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