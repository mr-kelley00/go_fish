# Go Fish by Avvery C. and Trinity G.
# Version 0.30a

from random import randint
from random import shuffle

print ("Welecome to Go Fish Version 0.0a")
user = input("Hello!  What is your name? [Type your name and press enter.] ")
print("Hello", user)

rules = int(input("Do you know how to play Go Fish. Enter 1 for NO and 2 for YES. "))
if rules == 1:
        print (" The object of the game is to win the most books of cards.")
        print ("A book is a set of cards. In total there should be 13 books of 4.")
        print ("The cards rank from the highest card (ace) the lowest (two).")
        print ("The dealer gives out a card to each player faced up. The player with the lowest card number is the dealer.")
        print ("The dealer deals out the cards cloclwise one at a time, and face down.")
        print ("If there are 2-3 players each one recieves 7 cards. If there are 4-5 players each one recieves 5 cards.")
        print ("The remainder of the cards are faced down on the table to be a stock.")
        print ("The player to the left of the dealer goes first.")
        print ("The player that goes first ask another opponent for a card ranking from ace to two.")
        print ("The player must have at least 1 card that the player asked for.")
        print ("The player that has been asked for the requested card must hand all of the cards asked for. For exmaple, if they asked for a 2 you must give them all your 2's.")
        print ("If the player who has been asked for a certain card does not have any of the cards requested must say 'Go Fish', and the player who requested for that card must grab one card from the top of the stock.")
        print ("If they get a match then they get to go again. The player keeps going until they get no more cards requested.")
        print ("If a player gets a book of 4 matching cards, they place them on the table facing up.")
        print ("If the player goes fishing without 'making a catch' of the requested cards, the turn passes to his left.")
        print ("If a player runs out of cards, they wait until it is there turn and pick from the stock. If there is no cards then the player is out.")
        print ("The game ends until all books have been won. The player with the most books wins.")
else:
    print ("Let's Start.")
deck = ["ace", "ace", "ace", "ace", "two", "two", "two", "two", "three", "three", "three", "three", "four", "four", "four", "four", "five", "five", "five", "five", "six", "six", "six", "six", "seven", "seven", "seven", "seven", "eight", "eight", "eight", "eight", "nine", "nine", "nine", "nine", "ten", "ten", "ten", "ten", "jack", "jack", "jack", "jack", "queen", "queen", "queen", "queen", "king", "king", "king", "king"]
# TELL THE PROGRAM WHAT EACH CARD IS WORTH. value = ["ace": 14, "king": 13, "queen": 12, "jack": 11, "ten": 10, "nine": 9, "eight": 8, "seven": 7, "six": 6, "five": 5, "four": 4, "three": 3, "two": 2]

print(deck)
shuffle(deck)
print(deck)


# FIGURE OUT WHO GOES FIRST
P1_deal = []
P2_deal = []
P3_deal = []
P4_deal = []

P1_deal.append(deck[0])
print (P1_deal)
deck.remove(deck[0])
P2_deal.append(deck[0])
print (P2_deal)
deck.remove(deck[0])
P3_deal.append(deck[0])
print (P3_deal)
P4_deal.append(deck[0])
print (P4_deal)
deck.remove(deck[0])

#DEAL OUT ONE CARD PER PLAYER
#CHECK FOR PLAYER WITH LOWEST CARD
#SHUFFLE THE DECK
#PERSON TO THE RIGHT CUT THE DECK

cards_dealt = 0
while cards_dealt < 5:
        

        cards_dealt += 1
"""
def dealer(person):
        print(dealer)
dealer(deck)
print(deck)
"""



        
        


