class Dealer():
	def __init__(self, deck):
		self.deck = deck
		self.hand = []

	def clear_hand(self):
		self.hand = []

	def get_hand(self):
		return sum(self.hand)

	def add_to_hand(self):
		self.hand.append(self.draw())

	def draw(self):
		return self.deck.draw()