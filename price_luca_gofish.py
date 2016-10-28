#Author: Luca P.
#v0.02
#10/28/16
import time
def returnRealNumber(card):
	if "Ace" in card:
		return "Ace"
	elif "2" in card:
		return "2"
	elif "3" in card:
		return "3"
	elif "4" in card:
		return "4"
	elif "5" in card:
		return "5"
	elif "6" in card:
		return "6"
	elif "7" in card:
		return "7"
	elif "8" in card:
		return "8"
	elif "9" in card:
		return "9"
	elif "10" in card:
		return "10"
	elif "Jack" in card:
		return "Jack"
	elif "Queen" in card:
		return "Queen"
	elif "King" in card:
		return "King"
allcards = []
cards = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
suits = ["Diamonds","Clubs","Hearts","Spades"]
books = {}
for card in cards:
	for suit in suits:
		allcards.append(card+" of "+suit)
class GoFish:
	def __init__(self):
		if "y" in input("Enable cheats? (Yes or no) ").lower():
			self.enableCheatMode()
		else:
			print("Cheats disabled")
			self.cheats = False
		self.name = input("Welcome to Go Fish! What's your name? ")
		print("Hello " + self.name + "!")
		if "y" in input("Do you know how to play go fish? ").lower():
			print("Ok, good! Let's start!")
		else:
			import webbrowser
			webbrowser.open("http://www.bicyclecards.com/how-to-play/go-fish/")
			input("Press ENTER when you are done reading.")
		self.players = {self.name:[],"Machine":[],"Non-Human":[],"Artificial Intelligence":[], "Robot":[]}
		for playersbooks in self.players:
			books[playersbooks] = 0
		self.startGame()
		self.dealer = "TBD"
	def chooseTarget(self):
		thing = input("Choose who you want cards from: ")
		if thing != self.player1:
			if thing != self.player2:
				if thing != self.player3:
					if thing != self.player4:
						if thing != self.player5:
							print("Please choose a player!")
		elif thing == self.name:
			print("You can't take cards from yourself!")
		return thing	
	def chooseCardPlayer(self):
		RealCard = "none"
		playersCards = ""
		for pcards in self.players[self.name]:
			playersCards += pcards
		while RealCard == "none": # loop called when player needs to select a card to ask a bot, checks if card exists then if you have it
			playercardinput = input("Which card would you like to ask for? \nPlease put in just the number, ex '9' ")
			PCReal = returnRealNumber(playercardinput)
			if PCReal != None:
				if playercardinput in playersCards:
					RealCard = PCReal
				else:
					print("You do not have that card!")
			else:
				print("Please put in a real card!")
		return RealCard
	def chooseCardToPick(self, bot):
		cardlist = self.players[bot]
		from random import randint
		rc = randint(0, len(cardlist))
		return rc - 1 #function that chooses random card for bot to ask a random player
	def getRandomPlayer(self,playername):
		from random import randint
		pl = randint(0,3)
		pllist = []
		for playerss in self.players:
			if playerss == playername:
				pass
			else:
				pllist.append(playerss)
		return pllist[pl] #function that chooses random player for bot to ask for a card
	def startGame(self):
		tempP = ""
		for player in self.players:
			tempP += "" + player + ", "
		tempP = tempP[:-2]
		print("Current players: " + tempP)
		self.goesFirst()
	def randomCardWOS(self):
		import random
		return random.randint(0,len(cards)) - 1
	def goesFirst(self):
		print("Let's decide the dealer, lowest card wins")
		print("If 2 players draw the same, first draw wins"); time.sleep(2)
		players = ""
		for player in self.players:
			players += player+":"
		players = players[:-1]
		player1,player2,player3,player4,player5 = players.split(":")
		player1gf = self.randomCardWOS()
		print(player1 + " drew a " + cards[player1gf]); time.sleep(0.5)
		player2gf = self.randomCardWOS()
		print(player2 + " drew a " + cards[player2gf]); time.sleep(0.5)
		player3gf = self.randomCardWOS()
		print(player3 + " drew a " + cards[player3gf]); time.sleep(0.5)
		player4gf = self.randomCardWOS()
		print(player4 + " drew a " + cards[player4gf]); time.sleep(0.5)
		player5gf = self.randomCardWOS()
		print(player5 + " drew a " + cards[player5gf]); time.sleep(0.5)
		self.player1next = player5
		self.player2next = player1
		self.player3next = player2
		self.player4next = player3
		self.player5next = player4
		lowest = min(player1gf, player2gf, player3gf, player4gf, player5gf)
		if lowest == player1gf:
			print(player1+" drew the lowest card, a "+ cards[player1gf])
			self.dealer = player1
			self.left2dealer = player5
		elif lowest == player2gf:
			print(player2+" drew the lowest card, a "+ cards[player2gf])
			self.dealer = player2
			self.left2dealer = player1
		elif lowest == player3gf:
			print(player3+" drew the lowest card, a "+ cards[player3gf])
			self.dealer = player3
			self.left2dealer = player2
		elif lowest == player4gf:
			print(player4+" drew the lowest card, a "+ cards[player4gf])
			self.dealer = player4
			self.left2dealer = player3
		elif lowest == player5gf:
			print(player5+" drew the lowest card, a "+ cards[player5gf])
			self.dealer = player5
			self.left2dealer = player4
		else:
			print("A lowest player could not be determined.")
		print("The dealer is " + self.dealer); time.sleep(2)
		self.dealCards()
	def randomCardInt(self):
		if len(allcards) > 0:
			import random
			return random.randint(0, len(allcards)) - 1
		else:
			print("There are no cards left in the deck.")
	def dealCards(self):
		print("Time for "+self.dealer+" to deal the cards!")
		playerList = ""
		for player in self.players:
			playerList += player+":"
		playerList = playerList[:-1]
		self.player1,self.player2,self.player3,self.player4,self.player5 = playerList.split(":")
		for i in range(0,5):
			for playerfirst in self.players:
				rc = self.randomCardInt()
				self.players[playerfirst].append(allcards[rc])
				del allcards[rc]
				print(playerfirst+ " has drawn a card"); time.sleep(0.5)
		self.play()
	def play(self):
		print("Now that the cards are dealt, let's play!"); time.sleep(0.5)
		print(self.left2dealer+" will start the game because he is left to "+self.dealer+", the dealer.")
		self.currentPlayer = self.left2dealer; time.sleep(2)
		while True:
			print("It is "+self.currentPlayer+"'s turn."); time.sleep(3)
			if self.currentPlayer != self.name:
				target = self.getRandomPlayer(self.currentPlayer)
				print(self.currentPlayer+" looks at "+target); time.sleep(3)
				cn = self.chooseCardToPick(self.currentPlayer)
				rn = returnRealNumber(self.players[self.currentPlayer][cn])
				print(self.currentPlayer+": "+target+", got any "+rn+"s?"); time.sleep(3)
				tempaicard = ""
				for enemyhascard in self.players[target]:
					tempaicard += enemyhascard
				if rn in tempaicard:
					print(target+": Yes, I have some "+rn+"s."); time.sleep(2)
					tempaicardnum = 0
					for card in self.players[target]:
						if rn in card:
							print(target+": Here, have my "+card)
							self.players[self.currentPlayer].append(card)
							del self.players[target][tempaicardnum]; time.sleep(2)
							drawnaicards = {"Ace":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"Jack":0,"Queen":0,"King":0} 
							for aicards in self.players[self.currentPlayer]:
								if returnRealNumber(aicards) == "Ace":
									drawnaicards["Ace"] += 1
								elif returnRealNumber(aicards) == "2":
									drawnaicards["2"] += 1
								elif returnRealNumber(aicards) == "3":
									drawnaicards["3"] += 1
								elif returnRealNumber(aicards) == "4":
									drawnaicards["4"] += 1
								elif returnRealNumber(aicards) == "5":
									drawnaicards["5"] += 1
								elif returnRealNumber(aicards) == "6":
									drawnaicards["6"] += 1
								elif returnRealNumber(aicards) == "7":
									drawnaicards["7"] += 1
								elif returnRealNumber(aicards) == "8":
									drawnaicards["8"] += 1
								elif returnRealNumber(aicards) == "9":
									drawnaicards["9"] += 1
								elif returnRealNumber(aicards) == "10":
									drawnaicards["10"] += 1
								elif returnRealNumber(aicards) == "Jack":
									drawnaicards["Jack"] += 1
								elif returnRealNumber(aicards) == "Queen":
									drawnaicards["Queen"] += 1
								elif returnRealNumber(aicards) == "King":
									drawnaicards["King"] += 1
								else:
									pass
							for drawnaicard in drawnaicards:
								if drawnaicards[drawnaicard] == 4: # checks for a book
									print(str(self.currentPlayer) + " has collected a book of "+ str(returnRealNumber(str(drawnaicard))) +"!")
									books[self.currentPlayer] += 1
									print(self.currentPlayer + " has "+str(books[self.currentPlayer])+" books.")
									t = 0
									for bookcards in self.players[self.currentPlayer]:
										if returnRealNumber(bookcards) == drawnaicard:
											print("Discarding "+ bookcards)
											del self.players[self.currentPlayer][t]
											t += 1
										elif returnRealNumber(bookcards) != drawnaicard:
											t += 1
										else:
											t += 1
								elif drawnaicards[drawnaicard] <= 4: 
									pass
								else:
									pass
							tempaicardnum += 1
						else:
							tempaicardnum += 1
				else:
					print(target+": No, go fish!"); time.sleep(2)
					gofishcard = self.randomCardInt()
					self.players[self.currentPlayer].append(allcards[gofishcard])
					del allcards[gofishcard]
					print(self.currentPlayer + " drew a card."); time.sleep(2)					
					if self.currentPlayer == self.player1:
						self.currentPlayer = self.player1next
					elif self.currentPlayer == self.player2:
						self.currentPlayer = self.player2next
					elif self.currentPlayer == self.player3:
						self.currentPlayer = self.player3next
					elif self.currentPlayer == self.player4:
						self.currentPlayer = self.player4next
					elif self.currentPlayer == self.player5:
						self.currentPlayer = self.player5next
			elif self.currentPlayer == self.name:
				print("Your current cards:")
				for playersCards in self.players[self.currentPlayer]:
					print(playersCards)				
				print("Current askable players:")
				for player in self.players:
					if player != self.name:
						print(player)
						if self.cheats == True:
							print("(Cheat)Raw list of "+player+"'s cards: ")
							print(self.players[player])
					else:
						pass
				target = self.chooseTarget()
				print(self.currentPlayer + " looks at " + target); time.sleep(3)
				playerchoosecard = self.chooseCardPlayer()
				print(self.currentPlayer+": "+target+ ", do you have any "+playerchoosecard+"s?"); time.sleep(3)
				tempEnemyCards = ""
				for desiredCard in self.players[target]:
					tempEnemyCards += desiredCard
				aiDelCard = 0
				if playerchoosecard in tempEnemyCards:
					print(target+": Yes, I have some "+playerchoosecard+"s."); time.sleep(2)
					for aiCard in self.players[target]:
						if playerchoosecard in aiCard:
							print(target+": Here, have my "+aiCard); time.sleep(2)
							self.players[self.currentPlayer].append(aiCard)
							del self.players[target][aiDelCard]
							drawnaicards = {"Ace":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"Jack":0,"Queen":0,"King":0} 
							for aicards in self.players[self.currentPlayer]:
								if returnRealNumber(aicards) == "Ace":
									drawnaicards["Ace"] += 1
								elif returnRealNumber(aicards) == "2":
									drawnaicards["2"] += 1
								elif returnRealNumber(aicards) == "3":
									drawnaicards["3"] += 1
								elif returnRealNumber(aicards) == "4":
									drawnaicards["4"] += 1
								elif returnRealNumber(aicards) == "5":
									drawnaicards["5"] += 1
								elif returnRealNumber(aicards) == "6":
									drawnaicards["6"] += 1
								elif returnRealNumber(aicards) == "7":
									drawnaicards["7"] += 1
								elif returnRealNumber(aicards) == "8":
									drawnaicards["8"] += 1
								elif returnRealNumber(aicards) == "9":
									drawnaicards["9"] += 1
								elif returnRealNumber(aicards) == "10":
									drawnaicards["10"] += 1
								elif returnRealNumber(aicards) == "Jack":
									drawnaicards["Jack"] += 1
								elif returnRealNumber(aicards) == "Queen":
									drawnaicards["Queen"] += 1
								elif returnRealNumber(aicards) == "King":
									drawnaicards["King"] += 1
								else:
									pass
							for drawnaicard in drawnaicards:
								if drawnaicards[drawnaicard] == 4:
									print(str(self.currentPlayer) + " has collected a book of "+ str(returnRealNumber(str(drawnaicard))) +"s!")
									books[self.currentPlayer] += 1
									print(self.currentPlayer + " now has "+str(books[self.currentPlayer])+" books.")
									t = 0
									for bookcards in self.players[self.currentPlayer]:
										if returnRealNumber(bookcards) == drawnaicard:
											print("Discarding "+bookcards)
											del self.players[self.currentPlayer][t]
											t += 1
										elif returnRealNumber(bookcards) != drawnaicard:
											print("Skipped over non-similar " + bookcards)
											t += 1
										else:
											print("Couldn't identify " + bookcards)
											t += 1
								elif drawnaicards[drawnaicard] <= 4: 
									pass
								else:
									pass
							aiDelCard += 1
						else:
							aiDelCard += 1
				else:
					print(target+": No, go fish!")
					gofishrc = self.randomCardInt()
					print("You drew a "+allcards[gofishrc])
					self.players[self.currentPlayer].append(allcards[gofishrc])
					del allcards[gofishrc]
					if self.currentPlayer == self.player1:
						self.currentPlayer = self.player1next
					elif self.currentPlayer == self.player2:
						self.currentPlayer = self.player2next
					elif self.currentPlayer == self.player3:
						self.currentPlayer = self.player3next
					elif self.currentPlayer == self.player4:
						self.currentPlayer = self.player4next
					elif self.currentPlayer == self.player5:
						self.currentPlayer = self.player5next
	def enableCheatMode(self):
		self.cheats = True
		print("Cheats have been enabled")
print("Starting a game of Go Fish...")
game = GoFish()
