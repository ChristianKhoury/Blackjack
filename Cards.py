"""
Module holding all information for the deck of cards
"""
import random

class Card:

    def __init__(self, suit: str, name, val: int = None):
        self._suit = suit

        if name == 'ace':
            val = (1, 11)
        if not val:
            val = int(name)
        
        self._name = name
        self._val = val


    def suit(self):
        return self._suit
    
    def name(self):
        return self._name
    
    def val(self):
        return self._val
    
    def __eq__(self, other):
        return (self._suit, self._name) == (other._suit, other._name)
    

def create_deck():
    deck = []

    suits = ('diamonds', 'hearts', 'spades', 'clubs')
    for suit in suits:
        # number cards:
        for num in range(2, 11):
            deck.append(Card(suit, num))
        
        # special crads:
        for card in ("king", 'queen', 'jack'):
            deck.append(Card(suit, card, 10))
        
        deck.append(Card(suit, 'ace'))
    
    return deck


def create_shuffled_deck():
    return random.shuffle(create_deck())
