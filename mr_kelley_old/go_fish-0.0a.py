# Go Fish by Ryan K. - ICT-3
# Version 0.5a - Published 11/04/2016

from random import randint 
from random import shuffle 
# These lines import useful functions from the random module. 

import webbrowser
# This line imports functions for the using the web browser. 

print("Welcome to Go Fish-bot Version 0.5a.\nI am the premier Go Fish program in the universe.\n")
user = input("Hello!  What is your name? [Type your name and press enter.]\n")
print("Hello,", user, "today we are going to play Go Fish!\n")
# These lines introduce the user to our program and records their name.

rules = int(input("Do you know how to play Go Fish? Enter 0 for NO and 1 for YES.\n"))

if rules == 0: # Fix this IF statement to print the rules.
    # Don't hate me, but I found an easy way to handle the rules.  
    webbrowser.open("http://www.bicyclecards.com/how-to-play/go-fish/") 
else:
    print("Ahh, an expert!  I hope you are more challenging than the last victim, err, player.\n") 

# Setup our deck of cards and assign values. 

deck_value = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
deck = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
full_deck = deck * 4
print (full_deck,"\n")
shuffle(full_deck)
print (full_deck) # Remove in final version to hide order from players. 

# DETERMINE FIRST PLAYER.

p1_dealt = []
p2_dealt = []
p3_dealt = []
p4_dealt = []
# Lines 35-38 create four empty lists for the player hands. 

p1_dealt.append(full_deck[0])
full_deck.remove(full_deck[0])
# Lines 41 and 42 ADD a card to player 1's hand and then REMOVE it from the full_deck.  

# Lines 46-51 finish the initial deal. 
p2_dealt.append(full_deck[0])
full_deck.remove(full_deck[0])
p3_dealt.append(full_deck[0])
full_deck.remove(full_deck[0])
p4_dealt.append(full_deck[0])
full_deck.remove(full_deck[0])

print (p1_dealt)
print (p2_dealt)
print (p3_dealt)
print (p4_dealt)

# This code should put you on the correct path to completing the project.
