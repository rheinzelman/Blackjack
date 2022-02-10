class Dealer():
	def __init__(self, deck):
		self.deck = deck
		self.hand_value = 0
		self.hand = []

	def clear_hand(self):
		self.hand_value = 0
		self.hand = []

	def get_hand_value(self):
		return self.hand_value

	def get_hand(self):
		return self.hand

	def add_to_hand(self):
		card_value, card = self.draw()
		self.hand_value += card_value
		self.hand.append(card)

	def draw(self):
		return self.deck.draw()