import unittest
from deck import Deck

class TestDeck(unittest.TestCase):
	def setUp(self):
		self.test_deck1 = Deck()

	def tearDown(self):
		pass

	def test_get_deck(self):

		# return true if the deck is not empty
		self.assertTrue(self.test_deck1.get_deck())

		# return false if the deck is empty
		for i in range(52):
			self.test_deck1.draw()
		self.assertFalse(self.test_deck1.get_deck())

	def test_draw(self):
		for i in range(52):
			self.test_deck1.draw()
		self.assertEquals(self.test_deck1.draw(), 'Empty Deck')

	def test_reset(self):
		self.test_deck2 = Deck()
		for i in range(52):
			self.test_deck1.draw()
		self.assertFalse(self.test_deck1.get_deck())
		self.assertEquals(self.test_deck1.reset(), self.test_deck2.get_deck())