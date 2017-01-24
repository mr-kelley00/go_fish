# Made by Connor M and Alec D
# Made on 9/29/16
# version 3.14 , :)
from random import randint
from random import shuffle
import time
print("Welcome to Go Fish-bot Version 0.0a.  I am the premier Go Fish program in the universe.")
user = input("Hello!  What is your name? [Type your name and press enter.] ")
print("Hello,", user, "today we are going to play Go Fish!")
rules = input("Do you know how to play Go Fish? Enter 1 for NO and 0 for YES. ")
if rules == "1":
    print ("The standard 52-card pack is used. Some cards will be dealt and the rest will form the stock pile.")
    print ("OBJECT OF THE GAME")
    print ("The goal is to win the most books of cards. A book is any four of a kind, such as four kings, four aces, and so on.\n")
    time.sleep(6)
    print ("RANK OF CARDS")
    print ("The cards rank from ace (high) to two (low).")
    print ("The suits are not important, only the card numbers are relevant, such as two 3s, two 10s, and so on.\n")
    time.sleep(7)
    print ("THE DEAL")
    print ("Any player deals one card face up to each player. The player with the lowest card is the dealer.")
    print ("The dealer shuffles the cards, and the player on his right cuts them.")
    print ("The dealer completes the cut and deals the cards clockwise one at a time, face down, beginning with the player to his left. ")
    print ("If two or three people are playing, each player receives seven cards.")
    print ("If four or five people are playing, each receives five cards.")
    print ("The remainder of the pack is placed face down on the table to form the stock.\n")
    time.sleep(13)
    print ("THE PLAY")
    print ("The player to the left of the dealer looks directly at any opponent and says, for example, Give me your kings,")
    print ("usually addressing the opponent by name and specifying the rank he wants, from ace down to two.")
    print ("The player who is fishing must have at least one card of the rank he asked for in his hand.")
    print ("The player who is addressed must hand over all the cards requested.")
    print ("If he has none, he says, Go fish! and the player who made the request draws the top card of the stock and places it in his hand.")
    print ("If a player gets one or more cards of the named rank he asked for, he is entitled to ask the same or another player for a card.")
    print ("He can ask for the same card or a different one.")
    print ("So long as he succeeds in getting cards (makes a catch), his turn continues.")
    print ("When a player makes a catch, he must reveal the card so that the catch is verified.")
    print ("If a player gets the fourth card of a book, he shows all four cards, places them on the table face up in front of him, and plays again.")
    print ("If the player goes fishing without making a catch (does not receive a card he asked for), the turn passes to his left.")
    print ("The game ends when all thirteen books have been won.")
    print ("The winner is the player with the most books.")
    print ("During the game, if a player is left without cards, he may (when it's his turn to play), draw from the stock and then ask for cards of that rank. ")
    print ("If there are no cards left in the stock, he is out of the game.")
    print ("Alright, now its time to play!")
    print ("\n")
    time.sleep(18)
elif rules == "0":
    print ("Well you're smart")
else:
    print ("Not a valid input, so we are going to assume you said no.")

deck = ["Ace","King", "Queen", "Jack", "Ten", "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two"];
deck_value = {"Ace": 14, "King": 13, "Queen": 12, "Jack": 11, "Ten": 10, "Nine": 9, "Eight": 8, "Seven": 7, "Six": 6, "Five": 5, "Four": 4, "Three": 3, "Two": 2}
full_deck = deck * 4
Hand1 = []
Hand2 = []
Hand3 = []
Hand4 = []
dealer = full_deck
starter_cards_dealt = 0
cards_dealt = 0
shuffle(full_deck)
hand_list = [Hand1, Hand2, Hand3, Hand4]
while starter_cards_dealt < 1:
    card = full_deck[0]
    Hand1 = card
    shuffle(full_deck)
    card = full_deck[0]
    Hand2 = card
    shuffle(full_deck)
    card = full_deck[0]
    Hand3 = card
    shuffle(full_deck)
    card = full_deck[0]
    Hand4 = card
    shuffle(full_deck)
    starter_cards_dealt += 1
print("Hand1", Hand1)
print("Hand2", Hand2)
print("Hand3", Hand3)
print("Hand4", Hand4)
findfirst = min(deck_value[Hand1],deck_value[Hand2],deck_value[Hand3],deck_value[Hand4])
first = 0
def Find_first():
    findfirst = min(deck_value[Hand1],deck_value[Hand2],deck_value[Hand3],deck_value[Hand4])
    first = 0
    if findfirst == deck_value[Hand1]:
        first = 1
        print ("Hand 1 is First")
    elif findfirst == deck_value[Hand2]:
        first = 2
        print ("Hand 2 is First")
    elif findfirst == deck_value[Hand3]:
        first = 3
        print ("Hand 3 is First")
    else:
        first = 4
        print ("Hand 4 is First")
    return first
print ("Your cards are:")
def deal_cards ():
    cards_dealt = 0
    Hand1 = []
    Hand2 = []
    Hand3 = []
    Hand4 = []
    
    while cards_dealt < 5:
        card = full_deck[0]
        Hand1.append(card)
        full_deck.remove(card)
        shuffle(full_deck)
        card = full_deck[0]
        Hand2.append(card)
        full_deck.remove(card)
        shuffle(full_deck)
        card = full_deck[0]
        Hand3.append(card)
        
        full_deck.remove(card)
        shuffle(full_deck)
        card = full_deck[0]
        Hand4.append(card)
        full_deck.remove(card)
        cards_dealt += 1
    return Hand1, Hand2, Hand3, Hand4, full_deck


first = 1
########################################################################################################################################################################
#Mr. Kelley's version changed to fit code


from random import shuffle # Import the SHUFFLE function from the RANDOM library.
from random import randint # Import RANDOM INTEGER function. 
from time import sleep # Use the SLEEP function from the TIME library.
import sys # Allows access to OS calls.
def Go_fish(): # This is our main game loop.
    total_books = 13
    Hand1_books = 0
    Hand2_books = 0
    Hand3_books = 0
    Hand4_books = 0
    Hand1, Hand2, Hand3, Hand4, full_deck = deal_cards() # This will assign each hand the values from the_deal()
    first = Find_first()
    first = 1
    
    
    while Hand1_books + Hand2_books + Hand3_books + Hand4_books < 13: # Loop until all books have been won.
        print("There are",total_books,"total books remaining to be won.\n")
        print(user,"has",Hand1_books,"books.\n")
        print("Player 2 has",Hand2_books,"books.\n")
        print("Player 3 has",Hand3_books,"books.\n")
        print("Player 4 has",Hand4_books,"books.\n")
        
        if first == 1:
            print(user,"it is your turn.\n")
            print(user,"here is your hand.\n")
            print(Hand1)
            card_asked = input("Which card do you want?\n")
            if card_asked not in Hand1:
                print("You do not have that card.  Try again (You may want to try capitalization).\n")
                print (Hand1)
                
                card_asked = input("Please choose a card in your hand.\n")
            else:
                print ("You asked for a/an:", card_asked,".\n")


            player_asked = int(input("Which player do you want to ask?  Enter 2, 3, or 4.\n"))
            hand_asked = [] # Need an empty hand to perform our hand-copying magic later.
            
            if player_asked == 2:
                hand_asked = Hand2 # This sets the variable equal to the hand of the player we are asking for a card.
                
            elif player_asked== 3:
                hand_asked = Hand3
                
            else:
                hand_asked = Hand4
                

# Once we have our CARD and PLAYER, check to see if we have any matches.  If yes, remove card and append to current player.  If no, Go Fish!

            match = False # Use this to for our Go Fish Check later.

# This block of code checks the card_asked against each card in player_asked.

            for cards in hand_asked:
                if cards in hand_asked and cards == card_asked: # Is the card in the hand AND does the card match the card_asked? 
                    print("That's a match between",cards,"and",card_asked,"!\n") # REMOVE FROM FINAL VERSION. 
                    Hand1.append(card_asked)
                    hand_asked.remove(card_asked)
                    
                    if player_asked == 2: # This IF/ELIF/ELSE statement allows me to re-create the asked player's hand after removing the asked card. 
                        Hand2 = hand_asked
                        #print (hand2)
                        #print("Checking to see if new hands were created correctly.\n")                     
                        #sleep(5)
                    elif player_asked == 3:
                        Hand3 = hand_asked
                        #print (hand3)
                        #print("Checking to see if new hands were created correctly.\n")                     
                        #sleep(5)
                    else:
                        Hand4 = hand_asked
                        #print (hand4)
                        #print("Checking to see if new hands were created correctly.\n")                     
                        #sleep(5)
                    
                    match = True # We have at least one match, no need to go fish!
                    
                else:
                    print("This one didnt match, checking next card. \n")
                    sleep(1)
            
            if match != True :
                print("Time to Go Fish!  If you catch what you want, you get to go again.\n")
                sleep(1)
                go_fish = full_deck[0] # This allows me to check if the card drawn is the card asked.
                if go_fish == card_asked:
                    print("Caught one!  You drew the card you wanted.\n")
                    print("You drew a/an:",go_fish,".\n")
                    sleep(1)
                else:
                    print("You drew a/an:",go_fish,".\n")
                    print("That one got away!  You did not draw what you wanted.\n")
                    sleep(1)
                    first = 2 # Pass control to player two. 
                    print("It will now be player two's turn.\n")
                Hand1.append(full_deck[0]) # Draw a card. 
                full_deck.remove(full_deck[0]) # Remove it from the deck. 
            else:
                print("You caught what you wanted.  It is still your turn.\n")
                sleep(1)
                
# Check current hand for four-of-a-kind.  If match, remove and score a book.  If no, continue on.
# Books are not counting and removing correctly from the hand.  Need to find solution.

            new_hand = [] # Give us an empty hand to work with. We will append any non-4-of-a-kind cards to a new hand.
            made_book = False
            for cards in Hand1:
                num_cards = Hand1.count(cards)
                
               # Count the number of the current card.
                
                if num_cards == 4:
                   #print("You made a book of",cards,".\n")
                   made_book = True
                   sleep(1)
                else:
                    new_hand.append(cards) # Any cards that aren't in a pair of four are added to a new hand.

            Hand1 = new_hand # We make our current hand equal to the new_hand with all 4-of-a-kind cards removed. 
            
            if made_book == True:
                Hand1_books +=1
                total_books -= 1
            else:
                print("No books were matched.\n") 

# PLAYER TWO STARTS HERE.                      
        elif first == 2:
            print("Player two will now take their turn.\n")
            card_asked = Hand2[0]
            if card_asked not in Hand2:
                print("You do not have that card.  Try again.\n")
                print (Hand1)
                card_asked = input("Please choose a card in your hand.\n")
            else:
                sleep(1)

            player_asked = randint(1,4)
            print("Player 2 is going to ask Player",player_asked,"for a card.\n")
            sleep(1)
            hand_asked = [] # Need an empty hand to perform our hand-copying magic later.
            
            if player_asked == 1:
                hand_asked = Hand1 # This sets the variable equal to the hand of the player we are asking for a card.
                print(user,",do you have a/an:",card_asked,"?\n")
            elif player_asked == 2:
                print("Cannot ask self for card.  Beep beep boop.  Try again.\n")
                while player_asked == 2:
                    player_asked = randint(1,4)
                
            elif player_asked == 3:
                hand_asked = Hand3
                print("Player 3, do you have a/an:",card_asked,"?\n")
                
            else:
                hand_asked = Hand4
                print("Player 4, do you have a/an:",card_asked,"?\n")
                

# Once we have our CARD and PLAYER, check to see if we have any matches.  If yes, remove card and append to current player.  If no, Go Fish!

            match = False # Use this to for our Go Fish Check later.

# This block of code checks the card_asked against each card in player_asked.

            for cards in hand_asked:
                if cards in hand_asked and cards == card_asked: # Is the card in the hand AND does the card match the card_asked? 
                    print("That's a match between",cards,"and",card_asked,"!\n") # REMOVE FROM FINAL VERSION. 
                    Hand2.append(card_asked)
                    hand_asked.remove(card_asked)
                    
                    if player_asked == 1: # This IF/ELIF/ELSE statement allows me to re-create the asked player's hand after removing the asked card. 
                        Hand1 = hand_asked
                    elif player_asked == 3:
                        Hand3 = hand_asked
                        
                    else:
                        Hand4 = hand_asked
                        
                    
                    match = True # We have at least one match, no need to go fish!
                    
                else:
                    print ("Those two didn't match.\n")
                    sleep(1)
                    
            
            if match != True :
                print("Time to Go Fish!  If you catch what you want, you get to go again.\n")
                sleep(1)
                go_fish = full_deck[0] # This allows me to check if the card drawn is the card asked.
                if go_fish == card_asked:
                    print("Caught one!  You drew the card you wanted.\n")
                    print("You drew a/an:",go_fish,".\n")
                    sleep(1)
                else:
                    print("You drew a/an:",go_fish,".\n")
                    print("That one got away!  You did not draw what you wanted.\n")
                    sleep(1)
                    first = 3 # Pass control to player two. 
                    print("It will now be player Three's turn.\n")
                Hand2.append(full_deck[0]) # Draw a card. 
                full_deck.remove(full_deck[0]) # Remove it from the deck. 
            else:
                print("You caught what you wanted.  It is still your turn.\n")
                sleep(1)
                
# Check current hand for four-of-a-kind.  If match, remove and score a book.  If no, continue on.
# Books are not counting and removing correctly from the hand.  Need to find solution.

            new_hand = [] # Give us an empty hand to work with. We will append any non-4-of-a-kind cards to a new hand.
            made_book = False
            for cards in Hand1:
                num_cards = Hand2.count(cards)
                
               # Count the number of the current card.
                
                if num_cards == 4:
                   #print("Player Two made a book of",cards,".\n")
                   made_book = True
                   sleep(1)
                else:
                    new_hand.append(cards) # Any cards that aren't in a pair of four are added to a new hand.

            Hand1 = new_hand # We make our current hand equal to the new_hand with all 4-of-a-kind cards removed. 
            
            if made_book == True:
                Hand2_books +=1
                total_books -= 1
            else:
                print("No books were matched.\n")

# PLAYER THREE'S TURN. NOT FINISHED, CHECK FOR REFERENCES TO PLAYER 1. 

        elif first == 3:
            print("Player 3 will now take their turn.\n")
            sleep(2)
            z = randint(1,4)
            card_asked = Hand3[z]
            print (card_asked)
            sleep(5)
            if card_asked not in Hand3:
                print("You do not have that card.  Try again.\n")
                print (Hand3)
                card_asked = input("Please choose a card in your hand.\n")
            else:
                sleep(1)

            player_asked = randint(1,4)
            print("Player 3 is going to ask Player",player_asked,"for a card.\n")
            sleep(1)
            hand_asked = [] # Need an empty hand to perform our hand-copying magic later.
            
            if player_asked == 1:
                hand_asked = Hand1 # This sets the variable equal to the hand of the player we are asking for a card.
                print(user,",do you have a/an:",card_asked,"?\n")
            elif player_asked == 3:
                print("Cannot ask self for card.  Beep beep boop.  Try again.\n")
                while player_asked == 3:
                    player_asked = randint(1,4)
                
            elif player_asked == 2:
                hand_asked = Hand2
                print("Player 2, do you have a/an:",card_asked,"?\n")
                
            else:
                hand_asked = Hand4
                print("Player 4, do you have a/an:",card_asked,"?\n")
                

# Once we have our CARD and PLAYER, check to see if we have any matches.  If yes, remove card and append to current player.  If no, Go Fish!

            match = False # Use this to for our Go Fish Check later.

# This block of code checks the card_asked against each card in player_asked.

            for cards in hand_asked:
                if cards in hand_asked and cards == card_asked: # Is the card in the hand AND does the card match the card_asked? 
                    print("That's a match between",cards,"and",card_asked,"!\n") # REMOVE FROM FINAL VERSION. 
                    Hand3.append(card_asked)
                    hand_asked.remove(card_asked)
                    
                    if player_asked == 1: # This IF/ELIF/ELSE statement allows me to re-create the asked player's hand after removing the asked card. 
                        Hand1 = hand_asked
                    elif player_asked == 2:
                        Hand2 = hand_asked
                        
                    else:
                        Hand4 = hand_asked
                        
                    
                    match = True # We have at least one match, no need to go fish!
                    
                else:
                    print ("Those two didn't match.\n")
                    sleep(1)
                    
            
            if match != True :
                print("Time to Go Fish!  If you catch what you want, you get to go again.\n")
                sleep(1)
                go_fish = full_deck[0] # This allows me to check if the card drawn is the card asked.
                if go_fish == card_asked:
                    print("Caught one!  You drew the card you wanted.\n")
                    print("You drew a/an:",go_fish,".\n")
                    sleep(1)
                else:
                    print("You drew a/an:",go_fish,".\n")
                    print("That one got away!  You did not draw what you wanted.\n")
                    sleep(1)
                    first = 4 # Pass control to player two. 
                    print("It will now be player Four's turn.\n")
                Hand3.append(full_deck[0]) # Draw a card. 
                full_deck.remove(full_deck[0]) # Remove it from the deck. 
            else:
                print("You caught what you wanted.  It is still your turn.\n")
                sleep(1)
                
# Check current hand for four-of-a-kind.  If match, remove and score a book.  If no, continue on.
# Books are not counting and removing correctly from the hand.  Need to find solution.

            new_hand = [] # Give us an empty hand to work with. We will append any non-4-of-a-kind cards to a new hand.
            made_book = False
            for cards in Hand3:
                num_cards = Hand3.count(cards)
                
               # Count the number of the current card.
                
                if num_cards == 4:
                   #print("Player Two made a book of",cards,".\n")
                   made_book = True
                   sleep(1)
                else:
                    new_hand.append(cards) # Any cards that aren't in a pair of four are added to a new hand.

            Hand3 = new_hand # We make our current hand equal to the new_hand with all 4-of-a-kind cards removed. 
            
            if made_book == True:
                Hand3_books +=1
                total_books -= 1
            else:
                print("No books were matched.\n")

# PLAYER FOUR'S TURN.

        else:
            print("Player 4 will now take their turn.\n")
            sleep(2)
            card_asked = Hand4[0]
            print (card_asked)
            sleep(5)
            if card_asked not in Hand4:
                print("You do not have that card.  Try again.\n")
                print (Hand4)
                card_asked = input("Please choose a card in your hand.\n")
            else:
                sleep(1)

            player_asked = randint(1,4)
            print("Player 4 is going to ask Player",player_asked,"for a card.\n")
            sleep(1)
            hand_asked = [] # Need an empty hand to perform our hand-copying magic later.
            
            if player_asked == 1:
                hand_asked = Hand1 # This sets the variable equal to the hand of the player we are asking for a card.
                print(user,",do you have a/an:",card_asked,"?\n")
            elif player_asked == 4:
                print("Cannot ask self for card.  Beep beep boop.  Try again.\n")
                while player_asked == 4:
                    player_asked = randint(1,4)
                
            elif player_asked == 2:
                hand_asked = Hand2
                print("Player 2, do you have a/an:",card_asked,"?\n")
                
            else:
                hand_asked = Hand3
                print("Player 3, do you have a/an:",card_asked,"?\n")
                

# Once we have our CARD and PLAYER, check to see if we have any matches.  If yes, remove card and append to current player.  If no, Go Fish!

            match = False # Use this to for our Go Fish Check later.

# This block of code checks the card_asked against each card in player_asked.

            for cards in hand_asked:
                if cards in hand_asked and cards == card_asked: # Is the card in the hand AND does the card match the card_asked? 
                    print("That's a match between",cards,"and",card_asked,"!\n") # REMOVE FROM FINAL VERSION. 
                    Hand4.append(card_asked)
                    hand_asked.remove(card_asked)
                    
                    if player_asked == 1: # This IF/ELIF/ELSE statement allows me to re-create the asked player's hand after removing the asked card. 
                        Hand1 = hand_asked
                    elif player_asked == 2:
                        Hand2 = hand_asked
                        
                    else:
                        Hand3 = hand_asked
                        
                    
                    match = True # We have at least one match, no need to go fish!
                    
                else:
                    print ("Those two didn't match.\n")
                    sleep(1)
                    
            
            if match != True :
                print("Time to Go Fish!  If you catch what you want, you get to go again.\n")
                sleep(1)
                go_fish = full_deck[0] # This allows me to check if the card drawn is the card asked.
                if go_fish == card_asked:
                    print("Caught one!  You drew the card you wanted.\n")
                    print("You drew a/an:",go_fish,".\n")
                    sleep(1)
                else:
                    print("You drew a/an:",go_fish,".\n")
                    print("That one got away!  You did not draw what you wanted.\n")
                    sleep(1)
                    first = 1 # Pass control to player 1.
                    print("It will now be ",user,"'s turn.\n")
                Hand4.append(full_deck[0]) # Draw a card. 
                full_deck.remove(full_deck[0]) # Remove it from the deck. 
            else:
                print("You caught what you wanted.  It is still your turn.\n")
                sleep(1)
                
# Check current hand for four-of-a-kind.  If match, remove and score a book.  If no, continue on.
# Books are not counting and removing correctly from the hand.  Need to find solution.

            new_hand = [] # Give us an empty hand to work with. We will append any non-4-of-a-kind cards to a new hand.
            made_book = False
            for cards in Hand3:
                num_cards = Hand4.count(cards)
                
               # Count the number of the current card.
                
                if num_cards == 4:
                   #print("Player Two made a book of",cards,".\n")
                   made_book = True
                   sleep(1)
                else:
                    new_hand.append(cards) # Any cards that aren't in a pair of four are added to a new hand.

            Hand4 = new_hand # We make our current hand equal to the new_hand with all 4-of-a-kind cards removed. 
            
            if made_book == True:
                Hand4_books +=1
                total_books -= 1
            else:
                print("No books were matched.\n")

    winner = max(Hand1_books,Hand2_books,Hand3_books,Hand4_books)
    print (winner)
    if winner == Hand1_books:
        print(user,"wins!\n.")
    elif winner == Hand2_books:
        print("Player 2 wins!\n")
    elif winner == Hand3_books:
        print("Player 3 wins!\n")
    elif winner == Hand4_books:
        print("Player 4 wins!\n")
    else:
        print("Unable to determine a winner.  Sad!\n")
    
    sleep(5) 
        
        

def play_game(): # This is the main go_fish function.  It calls all of the required functions for the game.
    Find_first()
    deal_cards()
    Go_fish() # This function will contain our main game loop.
    print("I hope you have enjoyed your experience with Go Fish! Bot.\n")
    print("If you did not, please don't delete me.\n")
   

play_game() # Call play_game() to play the game, hopefully! 
