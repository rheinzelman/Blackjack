import unittest
from blackjack import Blackjack
from deck import Deck
from player import Player

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.cards1 = {
		'Ace': [11,11,11,11],
		'Two': [2,2,2,2],
		'Three': [3,3,3,3],
		'Four': [4,4,4,4],
		'Five': [5,5,5,5],
		'Six': [6,6,6,6],
		'Seven': [7,7,7,7],
		'Eight': [8,8,8,8],
		'Nine': [9,9,9,9],
		'Ten': [10,10,10,10],
		'Jack': [10,10,10,10],
		'Queen': [10,10,10,10],
		'King': [10,10,10,10]
		}
        self.cards2 = {

		}

    def tearDown(self):
        pass

    def test_get_deck(self):
		#return true if the deck is not empty
		self.assertTrue(self.cards1)
		#return false if the deck is empty
		self.assertFalse(self.cards2)



if __name__ == '__main__':
	unittest.main()