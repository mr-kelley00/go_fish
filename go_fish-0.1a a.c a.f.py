#Group of Aidan Conlon and Allison Fisher
#Started working on 9/29/16
#Version 0.1a   


cards = [ "K", "K", "K", "K", "Q", "Q", "Q", "Q", "J", "J", "J", "J", "A", "A", "A", "A", "10", "10", "10", "10", "9", "9", "9", "9", "8", "8", "8", "8",
 "7", "7", "7", "7", "6", "6", "6", "6", "5", "5", "5", "5", "4", "4", "4", "4", "3", "3", "3", "3", "2", "2", "2", "2"] 
 
print("Welcome to Go Fish-bot Version 0.0a.  I am the premier Go Fish program in the universe.")
user = input("Hello!  What is your name? [Type your name and press enter.] ")
print("Hello,", user, "today we are going to play Go Fish!")
 
 
 
 
rules = int(input("Do you know how to play Go Fish? Enter 0 for NO and 1 for YES. "))

if rules == 0:
	print("OBJECT OF THE GAME.\n The goal is to win the most books of cards. A book is any four of a kind, such as four kings, four aces, and so on")
	print("RANK OF CARDS.\n The cards rank from ace (high) to two (low). The suits are not important, only the card numbers are relevant, such as two 3s, two 10s, and so on.")
	print("THE DEAL.\n Any player deals one card face up to each player. The player with the lowest card is the dealer. The dealer shuffles the cards, and the player on his right cuts them.\n The dealer completes the cut and deals the cards clockwise one at a time, face down, beginning with the player to his left. If two or three people are playing, each player receives seven cards. If four or five people are playing, each receives five cards. The remainder of the pack is placed face down on the table to form the stock.")
	print("THE PLAY.\n The player to the left of the dealer looks directly at any opponent and says, for example, 'Give me your kings,' usually addressing the opponent by name and specifying the rank he wants, from ace down to two. The player who is fishing must have at least one card of the rank he asked for in his hand. The player who is addressed must hand over all the cards requested. If he has none, he says, 'Go fish!' and the player who made the request draws the top card of the stock and places it in his hand.\n If a player gets one or more cards of the named rank he asked for, he is entitled to ask the same or another player for a card. He can ask for the same card or a different one. So long as he succeeds in getting cards (makes a catch), his turn continues. When a player makes a catch, he must reveal the card so that the catch is verified. If a player gets the fourth card of a book, he shows all four cards, places them on the table face up in front of him, and plays again.\n If the player goes fishing without making a catch (does not receive a card he asked for), the turn passes to his left.\n The game ends when all thirteen books have been won. The winner is the player with the most books. During the game, if a player is left without cards, he may (when it's his turn to play), draw from the stock and then ask for cards of that rank. If there are no cards left in the stock, he is out of the game.")



elif rules == 1:
	print("Congratulations! You know the rules! We can begin right away!")

else:
	print("I don't know what %s represents. Try Again"  % (rules))


from random import randint
from random import shuffle

shuffle(cards)

dealer_card1 = []
dealer_card2 = []
dealer_card3 = []
dealer_card4 = []



slice = cards[0]
dealer_card1.append(slice)
cards.remove(slice)
slice2 = cards[0]
dealer_card2.append(slice2)
cards.remove(slice2)
slice3 = cards[0]
dealer_card3.append(slice3)
cards.remove(slice3)
slice4 = cards[0]
dealer_card4.append(slice4)
cards.remove(slice4)







hand1 = randint(0,51) 
hand2 = randint(0,51)
hand3 = randint(0,51)
hand4 = randint(0,51)







































