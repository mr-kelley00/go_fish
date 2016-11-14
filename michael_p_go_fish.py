# Go fish by Palkowski Michael 

from random import randint
from random import shuffle

print ("Welcome to go fish-bot Version 0.0a.")
user = input("Hello!  What is your name? [Type your name and press enter.] ")
print ("Hello,", user, "today we are going to play Go Fish!")

rules = int(input("Do you know how to play Go Fish? Enter 0 for NO and 1 for YES. "))

if rules == 0:
    print ("standerd 52 card deck somecards will be dealt and the rest will form from the stockpile")
    print ("the goal is to win the most books of cards a book is any four of a kind like such as four kings also four aces")        
    print ("the cards rank from ace which is the highest to two which is the lowest the symbol on the card is not important it just matters to have two of a kind")
    print ("any player deals one card face up to each player the player with the lowest card is the dealer dealer shuffles cards and person right of dealer cuts cards")
    print ("dealer deals the the cards clockwise starting with the person to the left of the dealer and the cards are facing down and 1 at a time")
    print ("if there are two to three players playing at the time including the card dealer then each player will receive 7 cards each")
    print ("if four or five people are playing at the time including the dealer than each player will get five cards each")
    print ("the rest of the cards are placed face down on the table to form the stock")
    print ("the player to the left of the dealer asks one of the players if they have a certain rank of cards here is an example give me all of your kings")
    print ("if the person who is being asked for a certain rank of card doesn't have any of that card they say go fish to the person so they take 1 card from the stock")
    print ("if the person who asked for a certain rank of card gets a card from the person than they are allowed to ask another person for a rank of card again")
    print ("if the player asking for a rank of card does not get any cards the person to the left of the asker gets to start his turn")
    print ("if a player has no cards in their hand then they take 7 cards from the stock pile")
    print ("the game of go fish ends when all thirteen books of cards have been collocted any played")
else:
    print ("well good for you,", user,)

print("this is the deck cards types and order from least to greatest")
import random
def makedeck():
    deck = []
    c = 0
    values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "Quee", "king"]
    suits = ["Hearts", "Spades", "Diamonds", "Clubs"]

    for v in values:
        for s in suits:
            deck.append([v,s])

    random.shuffle(deck)

    return deck
    print()
    
    

















 
 

