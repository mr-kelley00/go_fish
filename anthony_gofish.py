
#Anthony & Sean v0.1a 10/17/2016

# then go_fish:
from random import shuffle
from random import randint
card_types = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "QUeen", "King"] 
deck = 52
hand = 0
players = 1, 2, 3, 4		#Each player gets five cards
leftover_deck = deck - hand
go_fish = hand + deck
name = input("My name is Go Bot 5000 what is your name?")
name_q = input("Your name is " + name + " right? 1 or 0: 1 == yes 0 == no ")
if name_q == '1':
    print ("I like the name " + name, "!")
elif name_q == '0':
	
    print("Ok can you tell me again please?")
ask = input(name + " Would you like to play Go Fish? yes or no?: 1 or 0")
if ask == '1':
    print ('Okay then lets go!')
elif ask == '0':
    print ("Too bad we are playing anyways")
else:
    print ("You were trying to say yes right? Well anyways lets go!")

rules = int(input("Would you like to know what the rules are?")
if rules == '1':
    print ("The rules are simple one player asks another if they have a certain type of card if they do they give them the card if not they must say go fish.")
    print ("The point of the game is to get as many groups of four cards as possible")
elif rules == '0':
    print ("Oh lets keep going then!")
else:
    print("I don't think that was a yes let's just keep going")




print ("And now I will pick a dealer with the person picker 6000")
from random import shuffle
shuffle(players)
from random import shuffle
shuffle(deck) 
