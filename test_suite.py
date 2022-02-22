import unittest
from test_blackjack import TestBlackjack
from test_deck import TestDeck
from test_player import TestPlayer

class TotalTestSuite(unittest.TestCase):
    def setUp(self):
        self.deck = TestDeck()
        self.player = TestPlayer()
        self.blackjack = TestBlackjack()

    def tearDown(self):
        self.blackjack.dispose()
        self.player.dispose()
        self.deck.dispose()

if __name__ == '__main__':
    unittest.main()
