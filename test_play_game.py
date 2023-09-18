import unittest
import play_game
import Cards

class TestGame(unittest.TestCase):

    def test_1(self):
        deck = Cards.create_shuffled_deck()
        player = play_game.Hand(deck)
        self.assertIsInstance(player.value, int)
        self.assertLessEqual(player.value, 21)

if __name__ == '__main__':
    unittest.main()
