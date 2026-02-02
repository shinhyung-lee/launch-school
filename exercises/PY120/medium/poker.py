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
    
    def _reset(self):
        self._deck = [Card(rank, suit)
                      for rank in Deck.RANKS
                      for suit in Deck.SUITS]
        
        shuffle(self._deck)
        
class PokerHand:
    
    def __init__(self, deck):
        self._deal_cards(deck)
        
    def _deal_cards(self, deck):
        self._cards = [deck.draw() for _ in range(5)]

    def print(self):
        for card in self._cards:
            print(card)

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _same_suit_cards(self):
        suits = set()
        for card in self._cards:
            suits.add(card.suit)
        return len(suits) == 1
        
    def _is_royal_flush(self):
        ROYAL_FLUSH_RANKS = [10, 'Jack', 'Queen', 'King', 'Ace']
        rank_in_royal_flush = []
        for card in self._cards:
            if card.rank in ROYAL_FLUSH_RANKS:
                rank_in_royal_flush.append(True)
            else:
                rank_in_royal_flush.append(False)
        return all(rank_in_royal_flush) and self._same_suit_cards()

    def _is_straight_flush(self):
        if not self._same_suit_cards():
            return False 
        
        straight_flush_values = {
            'Ace': 1,
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
        }
        card_ranks = [val for rank, val in straight_flush_values.items()]
        curr_ranks = []
        for card in self._cards:
            curr_ranks.append(straight_flush_values[card.rank])
        curr_ranks.sort()
        for idx in range(len(straight_flush_values) - 4):
            if curr_ranks == card_ranks[idx : idx + 5]:
                return True 
        
        return False 
        

    def _is_four_of_a_kind(self):
        ranks = [card.rank for card in self._cards]
        for idx in range(2):
            if ranks.count(ranks[idx]) == 4:
                return True 
        return False

    def _is_full_house(self):
        count = {} 
        for card in self._cards:
            if card.rank in count:
                count[card.rank] += 1
            else:
                count[card.rank] = 1
        count_set = {val for val in count.values()}
        return count_set == {2, 3}
        
    def _is_flush(self):
        return self._same_suit_cards() and not self._is_royal_flush() and not self._is_straight_flush()

    # helper for _is_straight 
    def _is_five_consecutive_cards(self):
        straight_flush_values = {
            'Ace': 1,
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
        }
        for card in self._cards:
            if card.rank in ['Jack', 'Queen', 'King']:
                straight_flush_values.update({'Ace': 14})
        card_ranks = sorted([val for val in straight_flush_values.values()])
        curr_ranks = []
        for card in self._cards:
            curr_ranks.append(straight_flush_values[card.rank])
        curr_ranks.sort()
        for idx in range(len(straight_flush_values) - 4):
            if curr_ranks == card_ranks[idx : idx + 5]:
                return True 
        
        return False  
    
    def _is_straight(self):
        return self._is_five_consecutive_cards() and not self._same_suit_cards()

    def _is_three_of_a_kind(self):
        three_of_a_kind_frequency = [1, 1, 3]
        rank_count = {}
        for card in self._cards:        
            if card.rank in rank_count:
                rank_count[card.rank] += 1
            else:
                rank_count[card.rank] = 1
                
        rank_count_frequency = sorted([val for val in rank_count.values()])
        return rank_count_frequency == three_of_a_kind_frequency
        
    def _is_two_pair(self):
        two_pair_frequency = [1, 2, 2]
        rank_count = {}
        for card in self._cards:        
            if card.rank in rank_count:
                rank_count[card.rank] += 1
            else:
                rank_count[card.rank] = 1
                
        rank_count_frequency = sorted([val for val in rank_count.values()])
        return rank_count_frequency == two_pair_frequency

    def _is_pair(self):
        one_pair_frequency = [1, 1, 1, 2]
        rank_count = {}
        for card in self._cards:        
            if card.rank in rank_count:
                rank_count[card.rank] += 1
            else:
                rank_count[card.rank] = 1
                
        rank_count_frequency = sorted([val for val in rank_count.values()])
        return rank_count_frequency == one_pair_frequency

#
#
# Testing Code

hand = PokerHand(Deck())
# hand.print()
# print(hand.evaluate())
# print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards

# All of these tests should return True

# hand = PokerHand(
#     TestDeck(
#         [
#             Card("Ace", "Hearts"),
#             Card("Queen", "Hearts"),
#             Card("King", "Hearts"),
#             Card("Jack", "Hearts"),
#             Card(10, "Hearts"),
#         ]
#     )
# )
# print(hand.evaluate() == "Royal flush")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(8, "Clubs"),
#             Card(9, "Clubs"),
#             Card("Queen", "Clubs"),
#             Card(10, "Clubs"),
#             Card("Jack", "Clubs"),
#         ]
#     )
# )

# print(hand.evaluate() == "Straight flush")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(3, "Hearts"),
#             Card(3, "Clubs"),
#             Card(5, "Diamonds"),
#             Card(3, "Spades"),
#             Card(3, "Diamonds"),
#         ]
#     )
# )
# print(hand.evaluate() == "Four of a kind")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(3, "Hearts"),
#             Card(3, "Clubs"),
#             Card(5, "Diamonds"),
#             Card(3, "Spades"),
#             Card(5, "Hearts"),
#         ]
#     )
# )
# print(hand.evaluate() == "Full house")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(10, "Hearts"),
#             Card("Ace", "Hearts"),
#             Card(2, "Hearts"),
#             Card("King", "Hearts"),
#             Card(3, "Hearts"),
#         ]
#     )
# )
# print(hand.evaluate() == "Flush")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(8, "Clubs"),
#             Card(9, "Diamonds"),
#             Card(10, "Clubs"),
#             Card(7, "Hearts"),
#             Card("Jack", "Clubs"),
#         ]
#     )
# )
# print(hand.evaluate() == "Straight")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card("Queen", "Clubs"),
#             Card("King", "Diamonds"),
#             Card(10, "Clubs"),
#             Card("Ace", "Hearts"),
#             Card("Jack", "Clubs"),
#         ]
#     )
# )
# print(hand.evaluate() == "Straight")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(3, "Hearts"),
#             Card(3, "Clubs"),
#             Card(5, "Diamonds"),
#             Card(3, "Spades"),
#             Card(6, "Diamonds"),
#         ]
#     )
# )
# print(hand._is_three_of_a_kind())
# print(hand.evaluate() == "Three of a kind")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(9, "Hearts"),
#             Card(9, "Clubs"),
#             Card(5, "Diamonds"),
#             Card(8, "Spades"),
#             Card(5, "Hearts"),
#         ]
#     )
# )
# print(hand.evaluate() == "Two pair")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(2, "Hearts"),
#             Card(9, "Clubs"),
#             Card(5, "Diamonds"),
#             Card(9, "Spades"),
#             Card(3, "Diamonds"),
#         ]
#     )
# )
# print(hand.evaluate() == "Pair")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(2, "Hearts"),
#             Card("King", "Clubs"),
#             Card(5, "Diamonds"),
#             Card(9, "Spades"),
#             Card(3, "Diamonds"),
#         ]
#     )
# )
# print(hand.evaluate() == "High card")