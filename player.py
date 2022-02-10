class Player():
	def __init__(self, name, deck):
		self.name = name
		self.deck = deck
		self.hand_value = 0
		self.hand = []
		self.ace_as_one_bool = False

	def clear_hand(self):
		self.hand_value = 0
		self.hand = []

	def get_name(self):
		return self.name

	def get_hand(self):
		return self.hand

	def get_hand_value(self):
		return self.hand_value

	def add_to_hand(self):
		card_value, card = self.draw()

		#this will ensure that multiple aces can be drawn
		if(card == 'Ace'):
			self.ace_as_one_bool = False
		
		self.hand_value += card_value
		self.hand.append(card)

	def draw(self):
		return self.deck.draw()

	def ace_as_one(self):
		if(self.ace_as_one_bool == True):
			pass
		else:
			self.hand_value -= 10
			self.ace_as_one_bool = True