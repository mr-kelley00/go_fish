
# Go Fish by Amar K. and Daniel R. - ICT-3
# Version 2.5 - Published 10/26/2016

import sys
import random
import time

from random import randint 
from random import shuffle  

print("Wlecome to Go Fish-bot Version 2.5 . I am the best Go Fish simulator in the nation!")
user = input("Wasssup!  What is your name? [Type your name and press enter.] ")
print("Hello,", user, "today we are going to play Go Fish!")

rules = int(input("Do you know how to play Go Fish? Enter 0 for NO and 1 or more for YES. ")) # This is where the user inputs their name so we can use it for later.

if rules == 0:
    print ("That is okay! I will tell you the rules,", user, "!")
    print ("The standard 52-card pack is used. Some cards will be dealt and the rest will form the stock pile.")
    print ("The goal is to win the most books of cards. A book is any four of a kind, such as four kings, four aces, and so on.")
    print ("The cards rank from ace (high) to two (low). The suits are not important, only the card numbers are relevant, such as two 3s, two 10s, and so on.")
    print ("Any player deals one card face up to each player. The player with the lowest card is the dealer. The dealer shuffles the cards, and the player on his right cuts them.")
    print ("The dealer completes the cut and deals the cards clockwise one at a time, face down, beginning with the player to his left. If two or three people are playing,")
    print ("each player receives seven cards. If four or five people are playing, each receives five cards. The remainder of the pack is placed face down on the table to form the stock.")
    print ("The player to the left of the dealer looks directly at any opponent and says, for example, Give me your kings, usually addressing the opponent by name and")
    print ("specifying the rank he wants, from ace down to two. The player who is fishing must have at least one card of the rank he asked for in his hand. ")
    print ("The player who is addressed must hand over all the cards requested. If he has none, he says, Go fish! and the player who made the request draws the top card of the stock and places it in his hand.")
    print ("If a player gets one or more cards of the named rank he asked for, he is entitled to ask the same or another player for a card. ")
    print ("He can ask for the same card or a different one. So long as he succeeds in getting cards (makes a catch), his turn continues. ")
    print ("When a player makes a catch, he must reveal the card so that the catch is verified. ")
    print ("If a player gets the fourth card of a book, he shows all four cards, places them on the table face up in front of him, and plays again.")
    print ("If the player goes fishing without making a catch (does not receive a card he asked for), the turn passes to his left.")
    print ("The game ends when all thirteen books have been won. The winner is the player with the most books. ")
    print ("During the game, if a player is left without cards, he may (when it's his turn to play), draw from the stock and then ask for cards of that rank. ")
    print ("If there are no cards left in the stock, he is out of the game.")

else: print ("Great! We are ready to play!")

def fours(name, hand): # Checks for a name/hand for wins
    for card in set(hand):
        if hand.count(card) == 4:
            for i in range(4):
                hands[name].remove(card)
            scores[name] += 1
            print('{} cleared the {}!'.format(name, card))

deck = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2", "Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2", "Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2", "Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
shuffle(deck)
print(deck)
    
scores = {name:0 for name in (sys.argv[1:] if sys.argv[2:] else list('1234'))}
names = list(scores)

if len(scores) > 4:
    hand_size = 5
else:
    hand_size = 5

hands = {name:[deck.pop() for i in range(hand_size)] for name in scores}

for name,hand in hands.items():
    fours(name, hand)

idx = 0
while 1:
    player = names[idx]
    if not hands[player]: # It deals with the player not having any cards
        if deck:
            hands[player].append(deck.pop())
        else:
            idx += 1
            if idx >= len(names):
                idx = 0
            continue
            
    if player.startswith('AI_'):
        ask = random.choice([name for name in names if name != player])
        card = random.choice(hands[player])
        print('{} asks for {} from {}.'.format(player, card, ask))
    else:
        while 1: # Deals with what you input and what is you have
            inp = input('{}\'s turn. Name and card? '.format(player))
            if inp:
                try:
                    ask, card = inp.split()
                except ValueError:
                    print('Enter a name and card, separated by spaces.')
                else:
                    card = card.upper()
                    if card in hands[player] and ask != player and ask in scores:
                        break
                    else:
                        print('Name must belong to a player other than yourself, and you must have the card.')
            else:
                print('Printing {}\'s hand for 5 seconds in 5 seconds.'.format(player))
                time.sleep(5)
                print(*sorted(hands[player]), sep='', end='\r', flush=True)
                time.sleep(5)
                print(' '*len(hands[player]), end='\r', flush=True)
                
    success = False
    while card in hands[ask]:
        hands[ask].remove(card)
        hands[player].append(card)
        success = True
    if not success:
        if deck:
            print('Go fish!')
            hands[player].append(deck.pop())
            if hands[player][-1] == card:
                success = True
                print('Fished the {}! Lucky!'.format(card))
        else:
            print('Can\'t fish - no deck.')
    else:
        print('{} got the {} from {}.'.format(player, card, ask))
    if not success:
        idx += 1
        if idx >= len(names):
            idx = 0
            
    fours(player, hands[player])
            
    if sum(scores.values()) == 13:
        print('Scores:')
        size = max(map(len, names))
        for k in sorted(scores, key=scores.get, reverse=True):
            print(k.ljust(size), scores[k])
        break
