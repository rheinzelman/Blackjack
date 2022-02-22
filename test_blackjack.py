import unittest
from blackjack import Blackjack
from deck import Deck
from player import Player

class TestBlackjack(unittest.TestCase):

    def test_play_player_turn(self):
        test_deck = Deck()
        test_player = Player('Ray', self.deck)