from Card import *
from random import shuffle
NUM_DECK_CARDS = 52

class Deck:
	def __init__(self):
		self.cards=[]
		self.cardsDrawn=0
		for rank in rank_to_val.keys():
			for suit in suits:
				self.cards.append(Card(rank,suit))
		shuffle(self.cards)

	def drawCard(self):
		if (self.cardsDrawn) < NUM_DECK_CARDS:
			self.cardsDrawn = self.cardsDrawn + 1
		else:
			raise RuntimeError("There are no more cards left to draw from. " +str(self.cardsDrawn) + " cards have been drawn from the deck of " + str(NUM_DECK_CARDS))
		return self.cards[self.cardsDrawn-1]
		
		
