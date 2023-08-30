import unittest
import Cards

class TestCards(unittest.TestCase):

    def test_Card(self):
        test = Cards.Card('diamond', '10')
        self.assertEqual(test.val(), 10)

        test2 = Cards.Card('spades', 'J', 11)
        self.assertEqual(test2.val(), 11)


if __name__ == '__main__':
    unittest.main()