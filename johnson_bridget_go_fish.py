# Go Fish by Bridget J.
# Version 0.0a - Published 10/27/16

from random import randint
from random import shuffle

print("Welcome to Go Fish-bot Version 0.0a. I am the premier Go Fish program in the universe.")
user = input("Hello! What is your name? [Type your name and press enter.] ")
print("Hello,", user, "today we are going to play Go Fish!")


def rules():
rules = int(input("Do you know how to play Go Fish? Enter 0 for NO and 1 for Yes. "))
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
deck = ["ace": 14, "king": 13, "queen": 12, "jack": 11, "ten": 10, "nine": 9, "eight": 8, "seven": 7, "six": 6, "five": 5, "four": 4, "three": 3, "two":2]
full_deck = deck * 4

print(deck)
shuffle(deck)
print(deck)

def goes_first():
P1_deal = []
P2_deal = []
P3_deal = []
P4_deal = []

    fresh_deck = make_deck()
    P1_deal = fresh_deck[0]
    fresh_deck.remove(fresh_deck[0])
    P2_deal = fresh_deck[0]
    fresh_deck.remove(fresh_deck[0])
    P3_deal = fresh_deck[0]
 +    fresh_deck.remove(fresh_deck[0])
 +    P4_deal = fresh_deck[0]
 +    fresh_deck.remove(fresh_deck[0])
 
 print(user, " was dealt",P1_deal,".\n")
 +    print("Player 2 was dealt",P2_deal,".\n")
 +    print("Player 3 was dealt",P3_deal,".\n")
 +    print("Player 4 was dealt",P4_deal,".\n")
 +    lowest = min(value[P1_deal], value[P2_deal], value[P3_deal], value[P4_deal])
 +    if value[P1_deal1] == lowest:
 +        print(user, " will play first!\n")
 +        first_player = 1
 +    elif value[P2_deal] == lowest:
 +        print("Player 2 will play first!\n")
 +        first_player = 2
 +    elif value[P3_deal] == lowest:
 +        print("Player 3 will play first!\n")
 +        first_player = 3
 +    else:
 +        print("Player 4 will play first!\n")
 +        first_player = 4
 +    return first_player
 
 def the_deal():
 +
 +    # Need to add conditional statement to start with first_player
 +    
 +    num_deal = int(input("How many cards do you want to deal to each player?\n"))
 +
 +    if num_deal * 4 > 52: # Make sure we aren't going to deal out the entire deck and crash the program.
 +        print("You will run out of cards in the deck.  Please enter a different number.\n")
 +        num_deal = int(input("How many cards do you want to deal to each player?\n"))
 +    else:
 +        print("You will deal",num_deal,"cards to each player.\n")
 +        
 +    cards_dealt = 0 # Our WHILE loop will be controlled by this variable.
 +    fresh_deck = make_deck() # We need a fresh deck after determining who goes first.
 +
 +    P1_deal = []
 +    P2_deal = []
 +    P3_deal = []
 +    P4_deal = []
 +    # Create four empty hands. 
 +    
 +    while cards_dealt < num_deal: # WHILE loop to deal our cards equal to num_deal variable. 
 +        P1_deal.append(fresh_deck[0])
 +        fresh_deck.remove(fresh_deck[0])
 +        P2_deal.append(fresh_deck[0])
 +        fresh_deck.remove(fresh_deck[0])
 +        P3_deal.append(fresh_deck[0])
 +        fresh_deck.remove(fresh_deck[0])
 +        P4_deal.append(fresh_deck[0])
 +        fresh_deck.remove(fresh_deck[0])
 +        print (P1_deal,"\n")  # Each loop we'll print the cards in hand. 
 +        cards_dealt += 1
 +    return P1_deal, P2_deal, P3_deal, P4_deal
 +
 +def go_fish(): # This is the main go_fish function.  It calls all of the required functions for the game.
 +    rules()
 +    make_deck()
 +    goes_first()
 +    hand1, hand2, hand3, hand4 = the_deal() # This will assign each hand the values from the_deal()
 +    print(hand1)
 +    print(hand2)
 +    print(hand3)
 +    print(hand4)

