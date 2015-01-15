rank_to_val = {'A':(1,11),'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
suits = set(['clubs','spades','hearts','diamonds'])

class Card:
	def __init__(self,rank,suit):#example- Card('9','spades') creates the 9 of spades
		if (rank not in rank_to_val.keys()):
			raise ValueError("rank must be one of :" + rank_to_val.keys())
		else:
			self.rank=rank
		if (suit not in suits):
			raise ValueError("suit must be one of :" + " ".join(list(suits)))
		else:
			self.suit=suit
	def value(self):
		return rank_to_val[self.rank]

	#Returns the max value of the hand that is < = 21
	def maxHandValue(hand):
		aces=0
		#calculate hand value sum
		sum=0
		for card in hand:
			m= card.value()
			if isinstance(m,list): #if we see an ace
				sum= sum + m[1]
				if sum >21:
					sum = sum - 10
				else:
					aces= aces+1
			else: #a non-ace
				sum=sum+m
			if (sum > 21) and (aces >0):
				aces = aces-1
				sum = sum - 10
		return sum
			                               
