# Go Fish by Ryan K. - ICT-3
# Version 0.5.03a - Published 11/07/2016

from random import shuffle # Import the SHUFFLE function from the RANDOM library. 
from time import sleep # Use the SLEEP function from the TIME library.
# It is good practice to put ALL of your FROM X IMPORT Y statements at the top of your code.

# I am defining all of the functions my program needs first.  I am defining them in the order which they are used in the game.
# Finally, I have one main go_fish() function that calls all of the other functions I am writing. 

deck = ["a Two", "a Three", "a Four", "a Five", "a Six", "a Seven", "an Eight", "a Nine", "a Ten", "a Jack", "a Queen", "a King", "an Ace"]
full_deck = deck * 4
# Making deck and full_deck GLOBAL variables so each function can refer to them.

value = {"a Two":2, "a Three":3, "a Four":4, "a Five":5, "a Six":6, "a Seven":7, "an Eight":8, "a Nine":9, "a Ten":10, "a Jack":11, "a Queen":12, "a King":13, "an Ace":14}
# Create a key to have our neccesary values.  CREDIT TO CONNOR FOR THIS IDEA!

print("Welcome to Go Fish-bot Version 0.5.03a.\nI am the premier Go Fish program in the universe.\n")
user = input("Hello!  What is your name? [Type your name and press enter.]\n")
print("Hello,", user, "today we are going to play Go Fish!\n")
# Making the user a GLOBAL variable as well. 


def rules():   # This function sets the game up for a single human player and handles the rules. 
    # These lines introduce the user to our program and records their name.
    rules = int(input("Do you know how to play Go Fish? Enter 0 for NO and 1 for YES.\n"))
    if rules == 0: 
        print("The rules can be found here: http://www.bicyclecards.com/how-to-play/go-fish/\n")
        print("The Deal\n")
        sleep(1) # This line will introduce a pause of (x) seconds.  Gives the user time to read the instructions.
        print("Each player will be dealt a card.  The player with the lowest card becomes the dealer.\n")
        print("In the event of a tie, the first player with the lowest card will play first.\n")
        sleep(1)
        print("The Play\n")
        sleep(1)
        print("The goal of Go Fish! is to complete a book which is four-of-a-kind.\n")
        print("Starting with the first player, players will take turns asking each other for one card already in hand.\n")
        print("For example, player 2 starts with an Ace, two Four's, a King, and a Jack.\n")
        print("Player 2 can ask any other player for an Ace, a Four, a King, or a Jack.\n")
        sleep(2)
        print("If the player being asked for a card has at least one of those cards, that player must hand over all the cards to the asking player.\n")
        print("If the player being asked does not have a card, they say, \"Go Fish!\"\n")
        print("The player that asked for the card then takes a card from the stock.\n")
        sleep(2)
    else:
        print("Ahh, an expert!  I hope you are more challenging than the last victim, err, player.\n") 
    

def make_deck():   # This fucntion will shuffle the new deck. 
    shuffle(full_deck)
    print("Shuffling...please hold.  This is extremely precise.\n")
    sleep(5)
    print("The deck has been sufficiently randomized.\n")
    print (full_deck,"\n") # REMOVE FROM FINAL CODE. 
    return full_deck

def goes_first():   # This function will determine which player will start the game. 
    # Call our new_player()
    deal1 = []
    deal2 = []
    deal3 = []
    deal4 = []
    # Create four emtpy list variables to store the card that is dealt.
    fresh_deck = make_deck()
    deal1 = fresh_deck[0]
    fresh_deck.remove(fresh_deck[0])
    deal2 = fresh_deck[0]
    fresh_deck.remove(fresh_deck[0])
    deal3 = fresh_deck[0]
    fresh_deck.remove(fresh_deck[0])
    deal4 = fresh_deck[0]
    fresh_deck.remove(fresh_deck[0])
    # The above lines make the deal1 through deal4 equal to the top card of the deck.  Then that top card is removed each time.
    print(user, " was dealt",deal1,".\n")
    print("Player 2 was dealt",deal2,".\n")
    print("Player 3 was dealt",deal3,".\n")
    print("Player 4 was dealt",deal4,".\n")
    lowest = min(value[deal1], value[deal2], value[deal3], value[deal4])
    print (lowest) # REMOVE FROM FINAL VERSION. 
    if value[deal1] == lowest:
        print(user, " will play first!\n")
        first_player = 1
    elif value[deal2] == lowest:
        print("Player 2 will play first!\n")
        first_player = 2
    elif value[deal3] == lowest:
        print("Player 3 will play first!\n")
        first_player = 3
    else:
        print("Player 4 will play first!\n")
        first_player = 4
    return first_player

def the_deal():

    # Need to add conditional statement to start with first_player
    
    num_deal = int(input("How many cards do you want to deal to each player?\n"))

    if num_deal * 4 > 52: # Make sure we aren't going to deal out the entire deck and crash the program.
        print("You will run out of cards in the deck.  Please enter a different number.\n")
        num_deal = int(input("How many cards do you want to deal to each player?\n"))
    else:
        print("You will deal",num_deal,"cards to each player.\n")
        
    cards_dealt = 0 # Our WHILE loop will be controlled by this variable.
    fresh_deck = make_deck() # We need a fresh deck after determining who goes first.

    deal1 = []
    deal2 = []
    deal3 = []
    deal4 = []
    # Create four empty hands. 
    
    while cards_dealt < num_deal: # WHILE loop to deal our cards equal to num_deal variable. 
        deal1.append(fresh_deck[0])
        fresh_deck.remove(fresh_deck[0])
        deal2.append(fresh_deck[0])
        fresh_deck.remove(fresh_deck[0])
        deal3.append(fresh_deck[0])
        fresh_deck.remove(fresh_deck[0])
        deal4.append(fresh_deck[0])
        fresh_deck.remove(fresh_deck[0])
        print (deal1,"\n")  # Each loop we'll print the cards in hand. 
        sleep(1)
        print (deal2,"\n")  # REMOVE THESE LINES IN FINAL VERSION. 
        sleep(1)            # REMOVE FROM FINAL
        print (deal3,"\n")  # REMOVE FROM FINAL
        sleep(1)            # REMOVE FROM FINAL
        print (deal4,"\n")  # REMOVE FROM FINAL
        sleep(1)            # REMOVE FROM FINAL
        cards_dealt += 1
    return deal1, deal2, deal3, deal4

def go_fish(): # This is the main go_fish function.  It calls all of the required functions for the game.
    rules()
    sleep(5)
    make_deck()
    sleep(5)
    goes_first()
    sleep(5)
    hand1, hand2, hand3, hand4 = the_deal() # This will assign each hand the values from the_deal()
    print(hand1)
    print(hand2)
    print(hand3)
    print(hand4)

go_fish() # Call go_fish() to play the game, hopefully! 
