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

	def get_ace_as_one_bool(self):
		return self.ace_as_one_bool

	def add_to_hand(self):
		card_value, card = self.draw()

		#this will ensure that multiple aces can be drawn
		if(card == 'Ace'):
			self.ace_as_one_bool = False
		
		self.hand_value += card_value
		self.hand.append(card)

	def add_specific(self,card_to_draw):
		card_value, card = self.draw_specific(card_to_draw)

		# this will ensure that multiple aces can be drawn
		if (card == 'Ace'):
			self.ace_as_one_bool = False

		self.hand_value += card_value
		self.hand.append(card)

	def draw(self):
		drawn_card = self.deck.draw()
		if self.get_hand_value() + drawn_card[0] > 21 and self.ace_as_one_bool == False and 'Ace' in self.get_hand():
			self.ace_as_one()
		return drawn_card

	def draw_specific(self, card_to_draw):
		drawn_card = self.deck.draw_specific(card_to_draw)
		if self.get_hand_value() + drawn_card[0] > 21 and self.ace_as_one_bool == False:
			self.ace_as_one()
		return drawn_card

	def ace_as_one(self):
		if(self.ace_as_one_bool == True):
			pass
		else:
			self.hand_value -= 10
			self.ace_as_one_bool = True