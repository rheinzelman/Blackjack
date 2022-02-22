import unittest
from blackjack import Blackjack

class TestBlackjack(unittest.TestCase):

    def setUp(self):
        self.test_blackjack = Blackjack()

    def tearDown(self):
        pass

    def test_play_game(self):
        self.test_blackjack.play_game()