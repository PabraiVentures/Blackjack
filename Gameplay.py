from Deck import *
from Card import *
from Player import *
from Dealer import *
class Gameplay:
	def __init__(self):
		#rn players money will reset each round... fix ltr 
		
		#find out how many players
		response = raw_input("How many players? [Enter a number 1 - 5]\n")
		if ( int(response) > 5 or int(response) < 1):
			raise ValueError("Invalid player number entered. Enter a number 1 - 5.")
		players=[]
		#create players
		for i in range(0,int(response)):
			players.append(Player(i))
		continuePlaying = True
		while(continuePlaying is True):
			
			#make shuffled deck
			deck = Deck()
		
			#give players 2 cards each
			for i in range(0,int(response)):
				#ask player for bet
				players[i].getAndPlacePlayerBet()
				players[i].hands.append([deck.drawCard(), deck.drawCard()])
		
			#create dealer and give them 2 cards
			dealer = Dealer()
			dealer.hand=[deck.drawCard(),deck.drawCard()]
			print "Dealer shows a " + dealer.hand[0].rank + " of " + dealer.hand[1].suit
			#we are ready to play
			#have each player make their decisions until they double, stand or bust
			letPlayersDecide(players,deck)
		
			print "Players done with turns"
			print "Dealers hand----------------------------------"
			dValue = maxHandValue(dealer.hand)
			while(dValue<17):
				printHand(dealer.hand)
				dealer.hand.append(deck.drawCard())
				dValue=maxHandValue(dealer.hand)
				if dValue > 21:
					print "Dealer busts"
			printHand(dealer.hand)
			dBlackjack = (dValue == 21 and len(dealer.hand)==2)
			
			
			#determine result for each players hand
			for player in players:
				for idx in range(0,len(player.hands)):
					pBlackjack=False
					pValue=maxHandValue(player.hands[idx])
					if len(player.hands[idx])==2 and pValue==21:
						pBlackjack=true
					if (pBlackjack and dBlackjack):
						player.money=player.money+player.bets[idx]
						print "Player "+str(player.id)+" draws"
					elif(pBlackjack):
						player.money=player.money+(2.5*player.bets[idx])
						print "Blackjack! Player "+str(player.id)+" wins $" +str(1.5*player.bets[idx]) 
						
					elif(pValue==dValue and pValue<22):
						player.money=player.money+player.bets[idx]
						print "Player "+str(player.id)+" draws"
					elif(pValue < 22 and pValue > dValue):
						player.money=player.money+2*player.bets[idx]
						print "Player "+str(player.id)+" wins $" +str(player.bets[idx])
					elif(pValue<22 and dValue>21):
						player.money=player.money+2*player.bets[idx]
						print "Player "+str(player.id)+" wins $" +str(player.bets[idx])	
						
					else:
						print "Player "+str(player.id)+" loses $" +str(player.bets[idx]) 
						
			#ask for new game
			for player in players:
				player.hands=[]
				player.bets=[]
				if player.money ==0:
					print "Player " + str(player.id) + " is broke. Conveniently he recieves a bailout for $1000"
					player.money = 1000
			continuePlaying=askForNewGame()
			
def askForNewGame():
	goodInput=False
	while(goodInput==False):
		response=raw_input("Play new game? Enter 'y' or 'n' \n")
		if str(response)  not in ['y','n']:
			goodInput=False
			print "Invalid input"
		else:
			goodInput=True
			if response == 'y':
				return True
			else:
				return False
def printHand(hand):
	print "Hand:"
	for card in hand:
		print '[ ' +card.rank+" of "+card.suit + ' ]'
def letPlayersDecide(players,deck):
		for player in players:
			
			completedHands=0
			playerHands=1
			while(completedHands<playerHands): #until we go through all of the players hands
				print "Player "+str(player.id)+" ---------------------------------------------"
				printHand(player.hands[completedHands])
				response=player.getPlayerDecisionForHand(completedHands)
				#need to increment playerHands if we split
				if response == 'split':
					player.hands.append(player.hands[completedHands][1],deck.drawCard())
					player.hands[completedHands][1]=deck.drawCard()
					playerHands=playerHands+1
				if response == 'double':
					player.money=player.money-player.bets[completedHands]
					player.bets[completedHands]=player.bets[completedHands]*2
					player.hands[completedHands].append(deck.drawCard())
					printHand(player.hands[completedHands])
					
					if maxHandValue(player.hands[completedHands]) > 21:
						print 'Player busts'
					
					completedHands=completedHands+1
					
				if response == 'hit':
					player.hands[completedHands].append(deck.drawCard())
					if maxHandValue(player.hands[completedHands]) > 21:
						printHand(player.hands[completedHands])
						print 'Player busts'
						completedHands=completedHands+1
				if response == 'stand':
					completedHands=completedHands+1
			