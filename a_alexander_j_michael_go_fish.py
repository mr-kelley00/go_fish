# By Alexander A. and Michael J.
# Version 0.1a
# 11/03/2016

from random import randint
from random import shuffle

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#This introduces the game to the player!
print("Welcome to Go Fish-bot Version 0.1a.\nI am the premier Go Fish program in the universe.")
user = input("Hello!  What is your name? [Type your name and press enter.] ")
print("Hello,", user, "today we are going to play Go Fish!")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#This explains the rules to the player!
rule = int(input("Do you know how to play Go-Fish? Enter 0 if you DON'T and 1 if you DO know the rules."))
AZAP = 0
while (AZAP == 0): #This makes a loop for the user to have unlimited chances to enter 0 or 1 if they accidently put something else.
        if rule == 0:
                print("What?! You don't know how to play Go-Fish? Well, here are the rules:")
                print("The goal of the game is to win the most books out of the four players. To get a book you need 4 of any kind of a card.")
                print("Each player receives seven cards, and they ask other players for the cards they want to make a book out of.")
                print("Whenever you ask somebody for a card you want, and they don't have it, you Go-Fish!\nIf they do have the card they give it to you, you get to ask someone to give you a card.\nIf they don't have it, you Go-Fish and you end your turn. If not, you keep on going with your turn.")
                print("To Go-Fish, you take a card out of the shuffled deck that's face down. And by doing this, you have a chance to get the card you were looking for!")
                AZAP += 1
        elif rule == 1:
                print("Great! You already know the rules, let's begin!")
                AZAP += 1       
        else:
                print("Remember, You MUST Enter 0 For NO or 1 For YES.")
                rule = int(input("Do you know how to play Go-Fish? Enter 0 for NO and 1 for YES."))
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

deck = ["2", "2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6", "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10", "Jack", "Jack", "Jack", "Jack", "Queen", "Queen", "Queen", "Queen", "King", "King" , "King", "King", "Ace", "Ace", "Ace", "Ace"]
value = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
 
shuffle(deck)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This let's the user to name the other players

player2 = input("What would you like to name player 2? [Type their name and press enter.] ")
print ("Player 2's name is " + player2)
player3 = input("What would you like to name player 3? [Type their name and press enter.] ")
print ("Player 3's name is " + player3)
player4 = input("What would you like to name player 4? [Type their name and press enter.] ")
print ("Player 4's name is " + player4)
