"""
play_game.py

Responsible for running the logic of the game
"""
import Cards


class Hand:

    def __init__(self, deck: [Cards.Card]):
        self.card1 = deck.pop()
        self.card2 = deck.pop()

        self.value = self.set_value()
    

    def set_value(self):
        if self.card1.name() == 'ace' and self.card2.name() == 'ace':
            return 12
        
        elif self.card1.name() == 'ace':
            return 11 + self.card2.val()
        
        elif self.card2.name() == 'ace':
            return 11 + self.card1.val()
        
        else:
            return self.card1.val() + self.card2.val()
            

def play_round():
    deck = Cards.create_deck()
    user = Hand(deck)
    dealer = Hand(deck)

    if dealer.value == 21:
        if user.value == 21:
            # trigger tie event: tie somehow return chips to user
            pass

        # trigger lose event: Loses chips starts new round
        pass
