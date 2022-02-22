import random

class Deck():
	def __init__(self):
		self.cards = {
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

	#draw a random card and take it out of the card pool
	def draw(self):

		#if we have no remaining cards in the pool
		if(not self.cards):
			return 'Empty Deck'

		drawn_card = random.choice(list(self.cards.items()))

		#if we are attempting the last card of a rank, then we will delete that rank from the card pool
		if (len(self.cards[drawn_card[0]]) == 1):
			temp = self.cards[drawn_card[0]], drawn_card[0]
			del self.cards[drawn_card[0]]
			return temp
		
		return self.cards[drawn_card[0]].pop(), drawn_card[0]

	#for testing purposes only
	def draw_specific(self,card):
		return self.cards[card].pop()

	#get the remaining cards in the deck, for testing only
	def get_deck(self):
		return self.cards

	def reset(self):
		self.cards = {
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
