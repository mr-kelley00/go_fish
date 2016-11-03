
# Go Fish Project by (T J), & (R B)
# Python verion (3.5.2)
# Project Version 1.1a updated 11/3/2016

user_input = input(" What\'s your name: ")
print(" Welcome",user_input,"to Go Fish!")
user_day = input(" Now, how\'s your day: ")            # This is the introduction into the program.
print(" Intresting...")
user_rules = input(" Do you know how to play go fish? Please Type 1 for yes and 2 for no and any other number or value to skip: " )
if (user_rules == '1'):
        print (" Good")
elif (user_rules == '2'):
        print("\n☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼\n     ▓▲▲▓▲▲▓  Go Fish is a fun game that will amuse and entertain even the youngest card players. It is similar to the game Authors.   ▓▲▲▓▲▲▓ \n     ▓▲▲▓▲▲▓  The standard 52-card pack is used. Some cards will be dealt and the rest will form the stock pile.                       ▓▲▲▓▲▲▓ \n     ▓▲▲▓▲▲▓  The goal is to win the most \'books\' of cards. A book is any four of a kind, such as four kings, four aces, and so on.    ▓▲▲▓▲▲▓ \n     ▓▲▲▓▲▲▓  You will choose from 3 other players decks. You can ask for any card from thier deck.                                    ▓▲▲▓▲▲▓\n☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼\n")
else:
        print (" You have successfully skipped the rules")

                   # This tells you how to play the game.  ⬆ (Added extra detail to make it look nice)

##########################################################################################################################################################################

import random   # This (Inports Random)

deck_of_cards = ["Ace ","Ace ","Ace ","Ace ","King ","King ","King ", "King ","Queen ","Queen ","Queen ", "Queen ","Jack ","Jack ","Jack ","Jack ","10 ","10 ","10 ","10 ","9 ","9 ","9 ",
"9 ","8 ","8 ","8 ","8 ","7 ","7 ","7 ","7 ","6 ","6 ","6 ","6 ","5 ","5 ","5 ","5 ","4 ","4 ","4 ","4 ","3 ","3 ","3 ","3 ","2 ","2 ","2 ","2 ",]
                                        # This is the deck.   ⬆


def shuffle_deck(deck_of_cards):
	shuffled_deck = deck_of_cards
	random.shuffle(shuffled_deck)         # This is the deck shuffle Function
	return shuffled_deck


#########################################################################################################################################################################

shuffled_deck = shuffle_deck(deck_of_cards)


player_hand = []
player_2_hand = []     # This creates a list for each players hand
player_3_hand = []
player_4_hand = []

player_hand[0:1] = deck_of_cards[0:1]
deck_of_cards = deck_of_cards[1:]

player_2_hand[0:1] = deck_of_cards[0:1]    # This distributes 1 card to each player to see who goes first
deck_of_cards = deck_of_cards[1:]

player_3_hand[0:1] = deck_of_cards[0:1]    
deck_of_cards = deck_of_cards[1:]

player_4_hand[0:1] = deck_of_cards[0:1]
deck_of_cards = deck_of_cards[1:]

Jack = 11
Queen = 12    # This sets a numarical value for all of the face cards
King = 13
Ace = 14

###########################################################################################################################################################################
print ("\n Now to decided the dealer and the player who goes first.")
print (" This is you card", player_hand)
print (" This is player two's card", player_2_hand)
print (" This is player three's card", player_3_hand)
print (" This is player four's card", player_4_hand)

First = 0       # This makes a variable called "First"

if (player_hand < player_2_hand and player_3_hand and player_4_hand):
        print(" Well,",user_input," Your the dealer today.")
        First =+ 2
elif (player_2_hand < player_hand and player_3_hand and player_4_hand):
        print(" Player 2 is the dealer")
        First =+ 3                                                           # This sets a value to the varuable "First"
elif (player_3_hand < player_hand and player_2_hand and player_4_hand):
        print(" Player 3 is the dealer")
        First =+ 4
else:
        print(" Player 4 is the dealer")
        First =+ 1
#########################################################################################################################################################################

deck_of_cards.append(player_hand)
deck_of_cards.append(player_2_hand)
deck_of_cards.append(player_3_hand)     # This puts the cards back into the deck. 
deck_of_cards.append(player_4_hand)

def shuffle_deck(deck_of_cards):
	shuffled_deck = deck_of_cards
	random.shuffle(shuffled_deck)         # This is the deck shuffle Function
	return shuffled_deck
print (" The cards have been returned to the deck")

if First == 4 or 2 or 3:
        print (" Player", First,"goes first.")

else:
        print ( user_input,"you are the dealer")
#########################################################################################################################################################################

print (" Now to deal the cards")
player_hand[0:5] = deck_of_cards[0:5]
deck_of_cards = deck_of_cards[5:]

player_2_hand[0:5] = deck_of_cards[0:5]
deck_of_cards = deck_of_cards[5:]

player_3_hand[0:5] = deck_of_cards[0:5]    # This distributes 5 cards to each player
deck_of_cards = deck_of_cards[5:]

player_4_hand[0:5] = deck_of_cards[0:5]
deck_of_cards = deck_of_cards[5:]

deck_length = len(deck_of_cards)	
print(" Here's your cards",(player_hand))
print(" There are",(deck_length),"cards left in the go fish deck.")

########################################################################################################################################################################
print (" Now the game begins")

#while(len(deck_of_cards) > 0):
        











     
