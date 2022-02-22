import unittest
from deck import Deck
from player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.test_deck = Deck()
        self.test_player = Player('Ray', self.test_deck)

    def tearDown(self):
        pass

    def test_clear_hand(self):
        self.test_player.add_to_hand()
        self.assertTrue(self.test_player.hand)
        self.assertTrue(not self.test_player.hand_value == 0)
        self.test_player.clear_hand()
        self.assertFalse(self.test_player.hand)
        self.assertTrue(self.test_player.hand_value == 0)

    def test_get_name(self):
        self.assertEqual(self.test_player.get_name(), self.test_player.name)

    #stand in for the add_to_hand function, which calls on the draw_specific function
    def test_add_specific(self):
        self.test_player.add_specific('Ace')
        self.test_player.add_specific('King')
        self.assertEqual(self.test_player.get_hand(), ['Ace', 'King'])

    def test_ace_as_one(self):
        self.test_player.add_specific('Ace')
        self.test_player.add_specific('King')
        self.assertEqual(self.test_player.get_hand_value(), 21)
        self.test_player.clear_hand()
        self.test_deck.reset()

        self.test_player.add_specific('Ace')
        self.test_player.add_specific('Ace')
        self.assertEqual(self.test_player.get_hand_value(), 12)
        self.test_player.clear_hand()
        self.test_deck.reset()

        self.test_player.add_specific('Ace')
        self.test_player.add_specific('Eight')
        self.test_player.add_specific('Ace')
        self.assertEqual(self.test_player.get_hand_value(), 20)
        self.test_player.clear_hand()
        self.test_deck.reset()

        self.test_player.add_specific('Ace')
        self.test_player.add_specific('Eight')
        self.test_player.add_specific('Ace')
        self.test_player.add_specific('Ace')
        self.assertEqual(self.test_player.get_hand_value(), 21)
        self.test_player.clear_hand()
        self.test_deck.reset()
