# Go Fish by Ryan K. - ICT-3
# Version 1.01 - Published 01/20/2017

from random import shuffle # Import the SHUFFLE function from the RANDOM library.
from random import randint # Import RANDOM INTEGER function.
from random import choice # Import choice. 
from time import sleep # Use the SLEEP function from the TIME library.
import sys # Allows access to OS calls.

# It is good practice to put ALL of your FROM X IMPORT Y statements at the top of your code.

# I am defining all of the functions my program needs first.  I am defining them in the order which they are used in the game.
# Finally, I have one main go_fish() function that calls all of the other functions I am writing. 

deck = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
full_deck = deck * 4
# Making deck and full_deck GLOBAL variables so each function can refer to them.

value = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14}
# Create a key to have our neccesary values.  CREDIT TO CONNOR AND ALEC FOR THIS IDEA!

print("Welcome to Go Fish-bot Version 1.01.\nI am the premier Go Fish program in the universe.\n")
user = input("Hello!  What is your name? [Type your name and press enter.]\n")
print("Hello,", user, "today we are going to play Go Fish!\n")
# Making the user a GLOBAL variable as well.  Any functions below can access the user variable data.  


def rules():   # This function sets the game up for a single human player and handles the rules. 
    # These lines introduce the user to our program and records their name.
    rules = int(input("Do you know how to play Go Fish? Enter 0 for NO and 1 for YES.\n"))
    if rules == 0: 
        print("The rules can be found here: http://www.bicyclecards.com/how-to-play/go-fish/\n")
        print("The Deal\n")
        sleep(2) # This line will introduce a pause of (x) seconds.  Gives the user time to read the instructions.
        print("Each player will be dealt a card.  The player with the lowest card becomes the dealer.\n")
        print("In the event of a tie, the first player with the lowest card will play first.\n")
        sleep(2)
        print("The Play\n")
        sleep(2)
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
    print("Shuffling...please hold.  This must be done with precise precision.\n")
    sleep(2)
    print("The deck has been sufficiently randomized.\nPlease deal them carefully.\n")
    return full_deck

def goes_first():   # This function will determine which player will start the game. 

    hand1 = []
    hand2 = []
    hand3 = []
    hand4 = []
    # Create four emtpy list variables to store the card that is dealt.

    fresh_deck = make_deck() # Give us a fresh deck to play with.
    
    hand1 = fresh_deck[0] # Draw the card to the hand. 
    fresh_deck.remove(fresh_deck[0]) # Remove that card from the deck. 
    hand2 = fresh_deck[0]
    fresh_deck.remove(fresh_deck[0])
    hand3 = fresh_deck[0]
    fresh_deck.remove(fresh_deck[0])
    hand4 = fresh_deck[0]
    fresh_deck.remove(fresh_deck[0])
    # The above lines make the deal1 through deal4 equal to the top card of the deck.  Then that top card is removed each time.

    print(user,"was dealt",hand1,".\n")
    print("Player 2 was dealt",hand2,".\n")
    print("Player 3 was dealt",hand3,".\n")
    print("Player 4 was dealt",hand4,".\n")
    print("The lowest card will be the dealer.  The player to their left will play first.\n")
    sleep(5)

    lowest = min(value[hand1], value[hand2], value[hand3], value[hand4]) # Find the lowest card value using the KEY we created earlier.  
    if value[hand1] == lowest:
        print("Player 2 will play first!\n")
        first_player = 2
    elif value[hand2] == lowest:
        print("Player 3 will play first!\n")
        first_player = 3
    elif value[hand3] == lowest:
        print("Player 4 will play first!\n")
        first_player = 4
    else:
        print(user," will play first!\n")
        first_player = 1
    return first_player

def deal_cards(): # This function can be used again in ANY card game that uses the same deck structure. 

    num_deal = int(input("How many cards do you want to deal to each player?\n"))

    if num_deal * 4 > 52: # Make sure we aren't going to deal out the entire deck and crash the program.
        print("You will run out of cards in the deck.  Please enter a different number.\n")
        num_deal = int(input("How many cards do you want to deal to each player?\n"))
    else:
        print("You will deal",num_deal,"cards to each player.\n")
        
    cards_dealt = 0 # Our WHILE loop will be controlled by this variable.
    fresh_deck = make_deck() # We need a fresh deck after determining who goes first.

    hand1 = []
    hand2 = []
    hand3 = []
    hand4 = []
    # Create four empty hands. 
    
    while cards_dealt < num_deal: # WHILE loop to deal our cards equal to num_deal variable. 
        hand1.append(fresh_deck[0])
        fresh_deck.remove(fresh_deck[0])
        hand2.append(fresh_deck[0])
        fresh_deck.remove(fresh_deck[0])
        hand3.append(fresh_deck[0])
        fresh_deck.remove(fresh_deck[0])
        hand4.append(fresh_deck[0])
        fresh_deck.remove(fresh_deck[0])
        #print (hand1,"\n")  # Each loop we'll print the cards in hand. 
        #sleep(1)
        cards_dealt += 1
    print(user,"you have the following cards in your opening hand:",hand1,".\n")
    hand1.sort()
    hand2.sort()
    hand3.sort()
    hand4.sort()
    return hand1, hand2, hand3, hand4, fresh_deck

def go_fish(): # This is our main game loop.

    total_books = 13
    p1_books = 0
    p2_books = 0
    p3_books = 0
    p4_books = 0
    hand1, hand2, hand3, hand4, fresh_deck = deal_cards() # This will assign each hand the values from the_deal()

# Next 5 lines are for testing purposes only.

    print (hand1)
    print (hand2)
    print (hand3)
    print (hand4)
    print("These are the current hands.\n")
    sleep(5)
    print (fresh_deck)

# Remove above 5 lines for final version!

    # first_turn = goes_first()
    first_turn = 1 # REMOVE THIS LINE AFTER TESTING.
    
    while p1_books + p2_books + p3_books + p4_books < 13: # Loop until all books have been won.
        print("There are",total_books,"total books remaining to be won.\n")
        print(user,"currently has",p1_books,"books scored.\n")
        print("Player 2 currently has",p2_books,"books scored.\n")
        print("Player 3 currently has",p3_books,"books scored.\n")
        print("Player 4 currently has",p4_books,"books scored.\n")
        sleep(5)

# PLAYER ONE STARTS HERE.

        if first_turn == 1:
            print(user,"it is your turn.\n")
            card_asked = input("Which card do you want?\n")
            if card_asked not in hand1:
                print("You do not have that card.  Try again.\n")
                print (hand1)
                card_asked = input("Please choose a card in your hand.\n")
                sleep(1)
            else:
                print ("You asked for a/an:", card_asked,".\n")
                sleep(1)

            player_asked = int(input("Which player do you want to ask?  Enter 2, 3, or 4.\n"))
            hand_asked = [] # Need an empty hand to perform our hand-copying magic later.
            
            if player_asked == 2:
                hand_asked = hand2 # This sets the variable equal to the hand of the player we are asking for a card.
                
            elif player_asked == 3:
                hand_asked = hand3
                
            else:
                hand_asked = hand4
                

# Once we have our CARD and PLAYER, check to see if we have any matches.  If yes, remove card and append to current player.  If no, Go Fish!

            match = False # Use this to for our Go Fish Check later.

# This block of code checks the card_asked against each card in player_asked.

            for cards in hand_asked:
                if cards in hand_asked and cards == card_asked: # Is the card in the hand AND does the card match the card_asked? 
                    print("That's a match between",cards,"and",card_asked,"!\n") # REMOVE FROM FINAL VERSION. 
                    hand1.append(card_asked)
                    hand_asked.remove(card_asked)
                    
                    if player_asked == 2: # This IF/ELIF/ELSE statement allows me to re-create the asked player's hand after removing the asked card. 
                        hand2 = hand_asked
                        #print (hand2)
                        #print("Checking to see if new hands were created correctly.\n")                     
                        #sleep(5)
                    elif player_asked == 3:
                        hand3 = hand_asked
                        #print (hand3)
                        #print("Checking to see if new hands were created correctly.\n")                     
                        #sleep(5)
                    else:
                        hand4 = hand_asked
                        #print (hand4)
                        #print("Checking to see if new hands were created correctly.\n")                     
                        #sleep(5)
                    
                    match = True # We have at least one match, no need to go fish!
                    
                else:
                    print ("Those two didn't match.\n")
                    sleep(1)
                    
            
            if match != True :
                print("Time to Go Fish!  If you catch what you want, you get to go again.\n")
                sleep(1)
                go_fish = fresh_deck[0] # This allows me to check if the card drawn is the card asked.
                if go_fish == card_asked:
                    print("Caught one!  You drew the card you wanted.\n")
                    print("You drew a/an:",go_fish,".\n")
                    sleep(1)
                else:
                    print("You drew a/an:",go_fish,".\n")
                    print("That one got away!  You did not draw what you wanted.\n")
                    sleep(1)
                    first_turn = 2 # Pass control to player two. 
                    print("It will now be player two's turn.\n")
                hand1.append(fresh_deck[0]) # Draw a card. 
                fresh_deck.remove(fresh_deck[0]) # Remove it from the deck. 
            else:
                print("You caught what you wanted.  It is still your turn.\n")
                sleep(1)
                
# Check current hand for four-of-a-kind.  If match, remove and score a book.  If no, continue on.
# Books are not counting and removing correctly from the hand.  Need to find solution.

            new_hand = [] # Give us an empty hand to work with. We will append any non-4-of-a-kind cards to a new hand.
            made_book = False
            for cards in hand1:
                num_cards = hand1.count(cards)
                
               # Count the number of the current card.
                
                if num_cards == 4:
                   #print("You made a book of",cards,".\n")
                   made_book = True
                   sleep(1)
                else:
                    new_hand.append(cards) # Any cards that aren't in a pair of four are added to a new hand.

            hand1 = new_hand # We make our current hand equal to the new_hand with all 4-of-a-kind cards removed. 
            
            if made_book == True:
                p1_books +=1
                total_books -= 1
            else:
                print("No books were matched.\n") 

# PLAYER TWO STARTS HERE.                      
        elif first_turn == 2:
            print("Player two will now take their turn.\n")
            card_asked = hand2[0]
            if card_asked not in hand2:
                print("You do not have that card.  Try again.\n")
                print (hand1)
                card_asked = input("Please choose a card in your hand.\n")
            else:
                sleep(1)

            player_asked = randint(1,4)
            print("Player 2 is going to ask Player",player_asked,"for a card.\n")
            sleep(1)
            hand_asked = [] # Need an empty hand to perform our hand-copying magic later.
            
            if player_asked == 1:
                hand_asked = hand1 # This sets the variable equal to the hand of the player we are asking for a card.
                print(user,",do you have a/an:",card_asked,"?\n")
            elif player_asked == 2:
                print("Cannot ask self for card.  Beep beep boop.  Try again.\n")
                while player_asked == 2:
                    player_asked = randint(1,4)
                
            elif player_asked == 3:
                hand_asked = hand3
                print("Player 3, do you have a/an:",card_asked,"?\n")
                
            else:
                hand_asked = hand4
                print("Player 4, do you have a/an:",card_asked,"?\n")
                

# Once we have our CARD and PLAYER, check to see if we have any matches.  If yes, remove card and append to current player.  If no, Go Fish!

            match = False # Use this to for our Go Fish Check later.

# This block of code checks the card_asked against each card in player_asked.

            for cards in hand_asked:
                if cards in hand_asked and cards == card_asked: # Is the card in the hand AND does the card match the card_asked? 
                    print("That's a match between",cards,"and",card_asked,"!\n") # REMOVE FROM FINAL VERSION. 
                    hand2.append(card_asked)
                    hand_asked.remove(card_asked)
                    
                    if player_asked == 1: # This IF/ELIF/ELSE statement allows me to re-create the asked player's hand after removing the asked card. 
                        hand1 = hand_asked
                    elif player_asked == 3:
                        hand3 = hand_asked
                        
                    else:
                        hand4 = hand_asked
                        
                    
                    match = True # We have at least one match, no need to go fish!
                    
                else:
                    print ("Those two didn't match.\n")
                    sleep(1)
                    
            
            if match != True :
                print("Time to Go Fish!  If you catch what you want, you get to go again.\n")
                sleep(1)
                go_fish = fresh_deck[0] # This allows me to check if the card drawn is the card asked.
                if go_fish == card_asked:
                    print("Caught one!  You drew the card you wanted.\n")
                    print("You drew a/an:",go_fish,".\n")
                    sleep(1)
                else:
                    print("You drew a/an:",go_fish,".\n")
                    print("That one got away!  You did not draw what you wanted.\n")
                    sleep(1)
                    first_turn = 3 # Pass control to player two. 
                    print("It will now be player two's turn.\n")
                hand2.append(fresh_deck[0]) # Draw a card. 
                fresh_deck.remove(fresh_deck[0]) # Remove it from the deck. 
            else:
                print("You caught what you wanted.  It is still your turn.\n")
                sleep(1)
                
# Check current hand for four-of-a-kind.  If match, remove and score a book.  If no, continue on.
# Books are not counting and removing correctly from the hand.  Need to find solution.

            new_hand = [] # Give us an empty hand to work with. We will append any non-4-of-a-kind cards to a new hand.
            made_book = False
            for cards in hand1:
                num_cards = hand2.count(cards)
                
               # Count the number of the current card.
                
                if num_cards == 4:
                   #print("Player Two made a book of",cards,".\n")
                   made_book = True
                   sleep(1)
                else:
                    new_hand.append(cards) # Any cards that aren't in a pair of four are added to a new hand.

            hand1 = new_hand # We make our current hand equal to the new_hand with all 4-of-a-kind cards removed. 
            
            if made_book == True:
                p2_books +=1
                total_books -= 1
            else:
                print("No books were matched.\n")

# PLAYER THREE'S TURN. NOT FINISHED, CHECK FOR REFERENCES TO PLAYER 1. 

        elif first_turn == 3:
            print("Player 3 will now take their turn.\n")
            sleep(2)
            z = randint(1,4)
            card_asked = hand3[z]
            print (card_asked)
            sleep(5)
            if card_asked not in hand3:
                print("You do not have that card.  Try again.\n")
                print (hand3)
                card_asked = input("Please choose a card in your hand.\n")
            else:
                sleep(1)

            player_asked = randint(1,4)
            print("Player 3 is going to ask Player",player_asked,"for a card.\n")
            sleep(1)
            hand_asked = [] # Need an empty hand to perform our hand-copying magic later.
            
            if player_asked == 1:
                hand_asked = hand1 # This sets the variable equal to the hand of the player we are asking for a card.
                print(user,",do you have a/an:",card_asked,"?\n")
            elif player_asked == 3:
                print("Cannot ask self for card.  Beep beep boop.  Try again.\n")
                while player_asked == 3:
                    player_asked = randint(1,4)
                
            elif player_asked == 2:
                hand_asked = hand2
                print("Player 3, do you have a/an:",card_asked,"?\n")
                
            else:
                hand_asked = hand4
                print("Player 4, do you have a/an:",card_asked,"?\n")
                

# Once we have our CARD and PLAYER, check to see if we have any matches.  If yes, remove card and append to current player.  If no, Go Fish!

            match = False # Use this to for our Go Fish Check later.

# This block of code checks the card_asked against each card in player_asked.

            for cards in hand_asked:
                if cards in hand_asked and cards == card_asked: # Is the card in the hand AND does the card match the card_asked? 
                    print("That's a match between",cards,"and",card_asked,"!\n") # REMOVE FROM FINAL VERSION. 
                    hand3.append(card_asked)
                    hand_asked.remove(card_asked)
                    
                    if player_asked == 1: # This IF/ELIF/ELSE statement allows me to re-create the asked player's hand after removing the asked card. 
                        hand1 = hand_asked
                    elif player_asked == 2:
                        hand2 = hand_asked
                        
                    else:
                        hand4 = hand_asked
                        
                    
                    match = True # We have at least one match, no need to go fish!
                    
                else:
                    print ("Those two didn't match.\n")
                    sleep(1)
                    
            
            if match != True :
                print("Time to Go Fish!  If you catch what you want, you get to go again.\n")
                sleep(1)
                go_fish = fresh_deck[0] # This allows me to check if the card drawn is the card asked.
                if go_fish == card_asked:
                    print("Caught one!  You drew the card you wanted.\n")
                    print("You drew a/an:",go_fish,".\n")
                    sleep(1)
                else:
                    print("You drew a/an:",go_fish,".\n")
                    print("That one got away!  You did not draw what you wanted.\n")
                    sleep(1)
                    first_turn = 4 # Pass control to player two. 
                    print("It will now be player two's turn.\n")
                hand3.append(fresh_deck[0]) # Draw a card. 
                fresh_deck.remove(fresh_deck[0]) # Remove it from the deck. 
            else:
                print("You caught what you wanted.  It is still your turn.\n")
                sleep(1)
                
# Check current hand for four-of-a-kind.  If match, remove and score a book.  If no, continue on.
# Books are not counting and removing correctly from the hand.  Need to find solution.

            new_hand = [] # Give us an empty hand to work with. We will append any non-4-of-a-kind cards to a new hand.
            made_book = False
            for cards in hand3:
                num_cards = hand3.count(cards)
                
               # Count the number of the current card.
                
                if num_cards == 4:
                   #print("Player Two made a book of",cards,".\n")
                   made_book = True
                   sleep(1)
                else:
                    new_hand.append(cards) # Any cards that aren't in a pair of four are added to a new hand.

            hand3 = new_hand # We make our current hand equal to the new_hand with all 4-of-a-kind cards removed. 
            
            if made_book == True:
                p3_books +=1
                total_books -= 1
            else:
                print("No books were matched.\n")

# PLAYER FOUR'S TURN.

        else:
            print("Player 4 will now take their turn.\n")
            sleep(2)
            card_asked = hand4[0]
            print (card_asked)
            sleep(5)
            if card_asked not in hand4:
                print("You do not have that card.  Try again.\n")
                print (hand3)
                card_asked = input("Please choose a card in your hand.\n")
            else:
                sleep(1)

            player_asked = randint(1,4)
            print("Player 4 is going to ask Player",player_asked,"for a card.\n")
            sleep(1)
            hand_asked = [] # Need an empty hand to perform our hand-copying magic later.
            
            if player_asked == 1:
                hand_asked = hand1 # This sets the variable equal to the hand of the player we are asking for a card.
                print(user,",do you have a/an:",card_asked,"?\n")
            elif player_asked == 4:
                print("Cannot ask self for card.  Beep beep boop.  Try again.\n")
                while player_asked == 4:
                    player_asked = randint(1,4)
                
            elif player_asked == 2:
                hand_asked = hand2
                print("Player 3, do you have a/an:",card_asked,"?\n")
                
            else:
                hand_asked = hand3
                print("Player 3, do you have a/an:",card_asked,"?\n")
                

# Once we have our CARD and PLAYER, check to see if we have any matches.  If yes, remove card and append to current player.  If no, Go Fish!

            match = False # Use this to for our Go Fish Check later.

# This block of code checks the card_asked against each card in player_asked.

            for cards in hand_asked:
                if cards in hand_asked and cards == card_asked: # Is the card in the hand AND does the card match the card_asked? 
                    print("That's a match between",cards,"and",card_asked,"!\n") # REMOVE FROM FINAL VERSION. 
                    hand4.append(card_asked)
                    hand_asked.remove(card_asked)
                    
                    if player_asked == 1: # This IF/ELIF/ELSE statement allows me to re-create the asked player's hand after removing the asked card. 
                        hand1 = hand_asked
                    elif player_asked == 2:
                        hand2 = hand_asked
                        
                    else:
                        hand3 = hand_asked
                        
                    
                    match = True # We have at least one match, no need to go fish!
                    
                else:
                    print ("Those two didn't match.\n")
                    sleep(1)
                    
            
            if match != True :
                print("Time to Go Fish!  If you catch what you want, you get to go again.\n")
                sleep(1)
                go_fish = fresh_deck[0] # This allows me to check if the card drawn is the card asked.
                if go_fish == card_asked:
                    print("Caught one!  You drew the card you wanted.\n")
                    print("You drew a/an:",go_fish,".\n")
                    sleep(1)
                else:
                    print("You drew a/an:",go_fish,".\n")
                    print("That one got away!  You did not draw what you wanted.\n")
                    sleep(1)
                    first_turn = 1 # Pass control to player 1.
                    print("It will now be player two's turn.\n")
                hand4.append(fresh_deck[0]) # Draw a card. 
                fresh_deck.remove(fresh_deck[0]) # Remove it from the deck. 
            else:
                print("You caught what you wanted.  It is still your turn.\n")
                sleep(1)
                
# Check current hand for four-of-a-kind.  If match, remove and score a book.  If no, continue on.
# Books are not counting and removing correctly from the hand.  Need to find solution.

            new_hand = [] # Give us an empty hand to work with. We will append any non-4-of-a-kind cards to a new hand.
            made_book = False
            for cards in hand3:
                num_cards = hand4.count(cards)
                
               # Count the number of the current card.
                
                if num_cards == 4:
                   #print("Player Two made a book of",cards,".\n")
                   made_book = True
                   sleep(1)
                else:
                    new_hand.append(cards) # Any cards that aren't in a pair of four are added to a new hand.

            hand3 = new_hand # We make our current hand equal to the new_hand with all 4-of-a-kind cards removed. 
            
            if made_book == True:
                p4_books +=1
                total_books -= 1
            else:
                print("No books were matched.\n")

    winner = max(p1_books,p2_books,p3_books,p4_books)
    print (winner)
    if winner == p1_books:
        print(user,"wins!\n.")
    elif winner == p2_books:
        print("Player 2 wins!\n")
    elif winner == p3_books:
        print("Player 3 wins!\n")
    elif winner == p4_books:
        print("Player 4 wins!\n")
    else:
        print("Unable to determine a winner.  Sad!\n")
    
    sleep(5) 
        
        

def play_game(): # This is the main go_fish function.  It calls all of the required functions for the game.
    rules()
    sleep(1)
    goes_first()
    sleep(1)
    go_fish() # This function will contain our main game loop.
    print("I hope you have enjoyed your experience with Go Fish! Bot.\n")
    print("If you did not, please don't delete me.\n")
   

play_game() # Call play_game() to play the game, hopefully! 
