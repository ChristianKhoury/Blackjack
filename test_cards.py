import unittest
import Cards

class TestCards(unittest.TestCase):

    def test_Card(self):
        test = Cards.Card('diamond', '10')
        self.assertEqual(test.val(), 10)

        test2 = Cards.Card('spades', 'J', 11)
        self.assertEqual(test2.val(), 11)

        test3 = Cards.Card('hearts', 'ace')
        self.assertEqual(test3.val(), (1, 11))
    

    def test_create_deck(self):
        deck = Cards.create_deck()
        self.assertEqual(len(deck), 52)
        ace_of_spades = Cards.Card('spades', 'ace')
        self.assertIn(ace_of_spades, deck)


if __name__ == '__main__':
    unittest.main()
