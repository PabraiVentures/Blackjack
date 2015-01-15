from Card import *

class Player:
	def __init__(self,id):
		self.id=id
		self.hands=[] #a player's hands is a list of hands a player has
			      #a particular hand is a list of cards in one hand
			      # self.hands for example might have 2 hands => [ [J:diamonds, 2:hearts] , [J:hearts, A:spades]  ]
		self.bets=[] #bets correspond to hands of same index
		self.money=1000

	def getAndPlacePlayerBet(self):
		goodInput = False
		while(goodInput==False):
			response = raw_input("Player "+str(self.id)+ " has $"+ str(self.money) + ". Enter your bet between $1 to $"+str(self.money)+ "\n$")
			goodInput=response.isdigit() and (self.money-int(response) > -1 ) and int(response) >0
			if goodInput == False:
				print "Invalid bet"

		self.money = self.money - int(response)
		self.bets.append(int(response))
 
	def getPlayerDecisionForHand(self,handIdx): #gets one decision for one hand
		goodInput = False
		while(goodInput == False):
			
			if(len(self.hands[handIdx]) == 2):
				if((self.hands[handIdx][0].value() == self.hands[handIdx][1].value()) and (self.bets[handIdx] <= self.money ) ):
					#if same value and we have enough cash we can split
					response = raw_input("Player "+str(self.id)+ " has $"+ str(self.money) + ". Hand bet is $"+str(self.bets[handIdx])+".\nEnter your decision to choose between 'split', 'double', 'hit' and 'stand'\n")
					goodInput = response in ['split','double','hit','stand']
				elif(self.bets[handIdx] <= self.money): #allow double down
					response = raw_input("Player "+str(self.id)+ " has $"+ str(self.money) + ". Hand bet is $"+str(self.bets[handIdx])+".\nEnter your decision to choose between 'double', 'hit' and 'stand'\n")
					goodInput=response in ['double','hit','stand']
				else:
					response = raw_input("Player "+str(self.id)+ " has $"+ str(self.money) + ". Hand bet is $"+str(self.bets[handIdx])+".\nEnter your decision to choose between 'hit' and 'stand'\n")
                                        goodInput = response in ['hit','stand']
			else:
				 response = raw_input("Player "+str(self.id)+ " has $"+ str(self.money) + ". Hand bet is $"+str(self.bets[handIdx])+".\nEnter your decision to choose between 'hit' and 'stand'\n")
                                 goodInput = response in ['hit','stand']
			if (goodInput == False):
				 print "Invalid decision"

		return response

