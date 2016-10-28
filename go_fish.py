
# Go Fish by Ertis Seferi & Carter Richards - ICT-3
# Version 0.6a - Published 10/04/2016

from random import randint 
from random import shuffle 
# These lines import useful functions from the random module. 

print("Welcome to Go Fish-bot Version 0.6a. I am the premier Go Fish program in the universe.")
player1 = input("Hello!  What is your name? [Type your name and press enter.] ")
print("Hello,", player1, "today we are going to play Go Fish!")
# These lines introduce the user to our program and records their name.

rules = int(input("Do you know how to play Go Fish? Enter 0 for NO and 1 for YES. "))

if rules == 0:
    print ("The goal is to win the most books of cards. A book is any four of a kind, such as four kings, four aces, and so on.\
    The cards rank from ace (the highest rank) to two (the lowest rank). The suits are not important, only the card numbers are relevant, such as two 3s, two 10s, and so on.\
    Your goal is to ask other players for cards to try to get four of a kind.")
elif rules == 1:
    print ("Ok then. Lets get started!")
else:
    print ("That's not what we wanted you to put! Oh well I will still show you the instructions anyways. The goal is to win the most books of cards. A book is any four of a kind, such as four kings, four aces, and so on.\
    The cards rank from ace (high) to two (low). The suits are not important, only the card numbers are relevant, such as two 3s, two 10s, and so on.\
    Your goal is to ask other players for cards to try to get four of a kind.")
    
player2 = input("What would you like to name player 2? [Type their name and press enter.] ")
print ("Player 2's name is " + player2)
player3 = input("What would you like to name player 3? [Type their name and press enter.] ")
print ("Player 3's name is " + player3)
player4 = input("What would you like to name player 4? [Type their name and press enter.] ")
print ("Player 4's name is " + player4)

deck = ["2", "2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6", "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10", "Jack", "Jack", "Jack", "Jack", "Queen", "Queen", "Queen", "Queen", "King", "King" , "King", "King", "Ace", "Ace", "Ace", "Ace"]
value = {"2":2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

print (" ")

print ("Here's the deck order from low to high")
print(deck) # Make sure it worked.
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# How can we shuffle the deck.

shuffle(deck)
#print(deck)
# This code should put you on the correct path to completing the project.
print("Now we are going to deal each player a card to see who goes first.\n The game order will go from lowest to highest card.")


#print (deck[0])
player1hand = deck[0]
deck.remove(deck[0])
print (player1 + " got a", player1hand)
player2hand = deck[0]
deck.remove(deck[0])
print (player2 + " got a", player2hand)
player3hand = deck[0]
deck.remove(deck[0])
print (player3 + " got a", player3hand)
player4hand = deck[0]
deck.remove(deck[0])
print (player4 + " got a", player4hand)

#Jack = 11
#Queen = 12
#King = 13
#Ace = 14

print (" ")

goes_first = 0
if (player1hand < player2hand and player3hand and player4hand):
    print (player1 , " will deal the cards")
    goes_first = player1
elif (player2hand < player1hand and player3hand and player4hand):
    print (player2 , " will deal the cards")
    goes_first = player2
elif (player3hand < player1hand and player2hand and player4hand):
    print (player3 , " will deal the cards")
    goes_first = player3
elif (player4hand < player1hand and player2hand and player3hand):
    print (player4 , " will deal the cards")
    goes_first = player4
else:
    print ("Lets deal the cards again.")

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

