import unittest
from blackjack import Blackjack
from deck import Deck
from player import Player

class TestBlackjack(unittest.TestCase):

    def setUp(self):
        self.test_blackjack = Blackjack()
        self.test_deck = Deck()
        self.test_player = Player('Ray', self.test_deck)

    def tearDown(self):
        pass

    def test_play_player_turn(self):
        self.test_blackjack.play_player_turn()

    def test_play_dealer_turn(self):
        self.test_blackjack.play_dealer_turn()

    def test_play_game(self):
        self.test_blackjack.play_game()