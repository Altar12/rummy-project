#this file includes the class definitions
from random import shuffle

class Card:
    def __init__(self, suit, face) -> None:
        self.suit = suit
        self.face = str(face).upper()
    def value(self) -> int:
        if '2' <= self.face <= '9' or self.face == '10':
            return int(self.face)
        if self.face == 'A':
            return 1
        return 10
    
class Player:
    def __init__(self, name, hand = []) -> None:
        self.name = name
        self.hand = hand
        self.sets = []

def shuffledDeck():
    suits = ['club', 'heart', 'diamond', 'spade']
    deck = []
    for suit in range(4):
        deck.append(Card(suits[suit], 'A'))
        for num in range(2, 11):
            deck.append(Card(suits[suit], num))
        deck.append(Card(suits[suit], 'K')) 
        deck.append(Card(suits[suit], 'Q'))
        deck.append(Card(suits[suit], 'J'))
    shuffle(deck)
    return deck       