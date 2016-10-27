# Made by Connor M and Alec D
# Made on 9/29/16
# version 2.2a
from random import randint
from random import shuffle
import time
print("Welcome to Go Fish-bot Version 0.0a.  I am the premier Go Fish program in the universe.")
user = input("Hello!  What is your name? [Type your name and press enter.] ")
print("Hello,", user, "today we are going to play Go Fish!")
# CODE IN A CHECK TO KEEP FROM CRASHING WHEN NON-INTEGER IS ENTERED BELOW. 
rules = input("Do you know how to play Go Fish? Enter 0 for NO and 1 for YES. ")
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
print ("These are your cards!\n")

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
while cards_dealt < 5:
    card = full_deck[0]
    Hand1 = card
    full_deck.remove(card)
    shuffle(full_deck)
    card = full_deck[0]
    Hand2 = card
    full_deck.remove(card)
    shuffle(full_deck)
    card = full_deck[0]
    Hand3 = card
    full_deck.remove(card)
    shuffle(full_deck)
    card = full_deck[0]
    Hand4 = card
    full_deck.remove(card)
    print (Hand1)
    cards_dealt += 1
def turn_order(Hand1, Hand2, Hand3, Hand4):
    print(deck_value[Hand1])
    print(deck_value[Hand2])
    print(deck_value[Hand3])
    print(deck_value[Hand4])
    first = min(deck_value[Hand1],deck_value[Hand2],deck_value[Hand3],deck_value[Hand4])
    
    return first
first = turn_order(Hand1, Hand2, Hand3, Hand4)
print (first) 
    
