#notes
# might need to change player and dealer hand to simply be an int to be able to do the Ace mechanic

from deck import Deck
from dealer import Dealer
from player import Player

import time

class Blackjack():

	def __init__(self):
		
		print("What's your name cowpoke? ", end="")
		playerName = 'Ray'
		print("Alright lets play...")
		
		self.deck = Deck()
		self.dealer = Dealer(self.deck)
		self.player = Player(playerName, self.deck)

		self.keep_playing = True

		self.player_bust = False
		self.dealer_bust = False

		self.MAX_HAND = 21

	def play_game(self):
		
		#while the player wishes to keep playing and the deck has cards
		while(self.keep_playing and self.deck.get_deck()):

			self.player.add_to_hand()
			print(self.player.get_hand())
			print("Hit? (Y/N): ", end="")

			hit_decision = input()

			while(hit_decision.lower() in ['y'] and self.deck.get_deck()):
				
				self.player.add_to_hand()
				print(self.player.get_hand())

				if(self.player.get_hand() > self.MAX_HAND):
					self.player_bust = True
					print("Bust...")
					time.sleep(1)
					break
				if(self.player.get_hand() == self.MAX_HAND):
					print("Woah mama!")
					time.sleep(1)
					break

				print("Hit? (Y/N)", end="")
				hit_decision = input()

			print('Dealer\'s turn')

			while(self.deck.get_deck()):

				self.dealer.add_to_hand()
				print(self.dealer.get_hand())
				time.sleep(0.5)

				if(self.dealer.get_hand() > self.MAX_HAND):
					self.dealer_bust = True
					print("Dealer busted!")
					break
				if(self.dealer.get_hand() == self.MAX_HAND):
					print('Dealer ballin!')
					break

			if(self.dealer_bust and self.player_bust):
				print('Both a y\'all lose!')
			elif(self.dealer_bust):
				print('Player wins!')
			elif(self.player_bust):
				print('Dealer wins...')

			print("Keep playing cowpoke? (Y/N): ", end="")
			self.keep_playing = input()
			if(not self.keep_playing.lower() in ['y']):
				self.keep_playing = False
			else:
				print("New deck? (Y/N): ", end="")
				new_deck = input()
				if(new_deck.lower() in ['y']):
					self.reset(True)
				else:
					self.reset(False)

			print(self.deck.get_deck())

			

	def reset(self, new_deck):
		
		self.player.clear_hand()
		self.dealer.clear_hand()

		if(new_deck == True):
			print("A new deck is being used")
			self.deck.reset()
		else:
			print("Same deck is being used")

if __name__ == "__main__":

	WorldsBestBlackjack = Blackjack()
	WorldsBestBlackjack.play_game()