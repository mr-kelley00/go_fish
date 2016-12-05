# Go Fish Project - ICT-3 Project Created by Evan and Jason
# Version 1.25a
# Published 11/2/2016

# This makes the deck variable.

deck = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
deck_value = {'Two' : 2, 'Three' : 3, 'Four' : 4, 'Five' : 5, 'Six' : 6, 'Seven' : 7, 'Eight' : 8, 'Nine' : 9, 'Ten' : 10, 'Jack' : 11, 'Queen' : 12, 'King' : 13, 'Ace' : 14}
full_deck = deck * 4

# Now we set up the hand variables.
hand1 = []
hand2 = []
hand3 = []
hand4 = []

# Now we shuffle the deck.
from random import shuffle
shuffle(full_deck)

# Now we introduce the program! :D
print("Welcome to Go Fish Version 1.25a! This program simulates the game Go Fish in a computer model!")
user = input("Before we start, what should I call you? [Type your name and press enter.] ")
print("Well, hello,", user, "we're almost ready to play Go Fish!")

# Now we see if the user actually even knows how to play go fish.

rules = int(input("But before we start, do you know how to play Go Fish? Enter 0 for NO and 1 for YES. "))

# Now we create a conditional statement, displaying the rules if the user does not know how to play, but not displaying them if they know how to already.
    
if rules == 0:
    print ("Okay then, well here are the rules!\n")
    print ("THE PACK\n")
    print ("The standard 52-card pack is used. Some cards will be dealt and the rest will form the stock pile.\n")
    print ("OBJECT OF THE GAME\n")  
    print ("The goal is to win the most ""books"" of cards. A book is any four of a kind, such as four kings, four aces, and so on.\n")   
    print ("RANK OF CARDS\n")    
    print ("The cards rank from ace (high) to two (low). The suits are not important, only the card numbers are relevant, such as two 3s, two 10s, and so on.\n")    
    print ("THE DEAL\n")
    print ("Any player deals one card face up to each player. The player with the lowest card is the dealer. The dealer shuffles the cards, and the player on his right cuts them.")
    print ("The dealer completes the cut and deals the cards clockwise one at a time, face down, beginning with the player to his left. If two or three people are playing,")
    print ("each player receives seven cards. If four or five people are playing, each receives five cards. The remainder of the pack is placed face down on the table to form the stock.\n")   
    print ("THE PLAY\n")
    print ("The player to the left of the dealer looks directly at any opponent and says, for example, ""Give me your kings,"" usually addressing the opponent by name and specifying")
    print ("the rank he wants, from ace down to two. The player who is ""fishing"" must have at least one card of the rank he asked for in his hand. The player who is addressed must") 
    print ("hand over all the cards requested. If he has none, he says, ""Go fish!"" and the player who made the request draws the top card of the stock and places it in his hand.")
    print ("If a player gets one or more cards of the named rank he asked for, he is entitled to ask the same or another player for a card. He can ask for the same card or")
    print ("a different one. So long as he succeeds in getting cards (makes a catch), his turn continues. When a player makes a catch, he must reveal the card so that the catch is verified.")
    print ("If a player gets the fourth card of a book, he shows all four cards, places them on the table face up in front of him, and plays again.")
    print ("If the player goes fishing without ""making a catch"" (does not receive a card he asked for), the turn passes to his left.")
    print ("The game ends when all thirteen books have been won. The winner is the player with the most books. During the game, if a player is left without cards, he may")
    print ("(when it's his turn to play), draw from the stock and then ask for cards of that rank. If there are no cards left in the stock, he is out of the game.\n")   
    print ("Well those are all of the rules for Go Fish! from the Bicycle Cards website!")
elif rules == 1:
    print ("Good, job. You can play a game that everyone knows how to play.")
else:
    rules = int(input("Input not correct. Please try again. Type 0 and then enter if you do not know how, type 1 if you already do! "))
    if rules == 0:
        print ("Okay then, well here are the rules!\n")
        print ("THE PACK\n")
        print ("The standard 52-card pack is used. Some cards will be dealt and the rest will form the stock pile.\n")
        print ("OBJECT OF THE GAME\n")  
        print ("The goal is to win the most ""books"" of cards. A book is any four of a kind, such as four kings, four aces, and so on.\n")   
        print ("RANK OF CARDS\n")    
        print ("The cards rank from ace (high) to two (low). The suits are not important, only the card numbers are relevant, such as two 3s, two 10s, and so on.\n")    
        print ("THE DEAL\n")
        print ("Any player deals one card face up to each player. The player with the lowest card is the dealer. The dealer shuffles the cards, and the player on his right cuts them.")
        print ("The dealer completes the cut and deals the cards clockwise one at a time, face down, beginning with the player to his left. If two or three people are playing,")
        print ("each player receives seven cards. If four or five people are playing, each receives five cards. The remainder of the pack is placed face down on the table to form the stock.\n")   
        print ("THE PLAY\n")
        print ("The player to the left of the dealer looks directly at any opponent and says, for example, ""Give me your kings,"" usually addressing the opponent by name and specifying")
        print ("the rank he wants, from ace down to two. The player who is ""fishing"" must have at least one card of the rank he asked for in his hand. The player who is addressed must") 
        print ("hand over all the cards requested. If he has none, he says, ""Go fish!"" and the player who made the request draws the top card of the stock and places it in his hand.")
        print ("If a player gets one or more cards of the named rank he asked for, he is entitled to ask the same or another player for a card. He can ask for the same card or")
        print ("a different one. So long as he succeeds in getting cards (makes a catch), his turn continues. When a player makes a catch, he must reveal the card so that the catch is verified.\n")
        print ("\nIf a player gets the fourth card of a book, he shows all four cards, places them on the table face up in front of him, and plays again.")
        print ("If the player goes fishing without ""making a catch"" (does not receive a card he asked for), the turn passes to his left. (When it's his turn to play), draw")
        print ("The game ends when all thirteen books have been won. The winner is the player with the most books. During the game, if a player is left without cards, he may")
        print ("draw from the stock and then ask for cards of that rank. If there are no cards left in the stock, he is out of the game.\n")   
        print ("Well those are all of the rules for Go Fish! from the Bicycle Cards website!")
    elif rules == 1:
        print ("Good, job. You can play a game that everyone knows how to play.")
    else:
        print ("Well, we will just continue the game!")

    
# Now we define the books variable.
book1 = 1
book2 = 2
book3 = 0
book4 = 0
totalbooks = book1 + book2 + book3 + book4

print ("Now we must determine who goes first.")

# Now we deal out the beginning card.
# CARDS_DEALT = 0
# START A WHILE LOOP.  WHILE CARDS_DEALT < 5:
# DEAL CARD TO PLAYER 1
# REMOVE FROM DECK
# DEAL CARD TO PLAYER 2
# REMOVE FROM DECK
# DEAL CARD TO PLAYER 3
# REMOVE FROM DECK
# DEAL CARD TO PLAYER 4
# REMOVE FROM DECK
# CARDS_DEALT += 1
hand1.append((full_deck[0]))
full_deck.remove(full_deck[0])
hand2.append((full_deck[0]))
full_deck.remove(full_deck[0])
hand3.append((full_deck[0]))
full_deck.remove(full_deck[0])
hand4.append((full_deck[0]))
full_deck.remove(full_deck[0])

print ("Here is your card:" , (hand1[0]))
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print ("Here are your oppenent's beginning cards!")
print ("Oppenent #1:" , (hand2[0]))
print ("Oppenent #2:" , (hand3[0]))
print ("Oppenent #3:" , (hand4[0]))

# Now let's make the program see who has the highest ranked card! [SKIPPED]        
goes_first = min(hand1, hand2, hand3, hand4)
if goes_first == hand1:
    print ("Player 1 goes first because they have the lowest card!.")
elif goes_first == hand2:
    print ("Player 2 goes first because they have the lowest card!.")
elif goes_first == hand3:
    print ("Player 3 goes first because they have the lowest card!")
else:
    print ("Player 4 goes first because they have the lowest card!.")
# Now let's put the dealer cards BACK IN THE DECK AND SHUFFLE THE DECK AGAIN! :D 
full_deck.append(hand1[0])
full_deck.append(hand2[0])
full_deck.append(hand3[0])
full_deck.append(hand4[0])
shuffle(full_deck)
# Now we create a card length variable.
cards_dealt = 0
# Okay, now let's deal out all the cards.
while cards_dealt < 4:
	hand1.append(full_deck[0])
	full_deck.remove(full_deck[0])
	hand2.append(full_deck[0])
	full_deck.remove(full_deck[0])
	hand3.append(full_deck[0])
	full_deck.remove(full_deck[0])
	hand4.append(full_deck[0])
	full_deck.remove(full_deck[0])
	cards_dealt += 1
	
