"""
Module holding all information for the deck of cards
"""

class Card:

    def __init__(self, suit: str, name, val: int = None):
        self._suit = suit

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