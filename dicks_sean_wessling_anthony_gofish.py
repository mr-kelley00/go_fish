#Sean Dicks and Anthony Wessling v0.6a 1/11/2017

from random import shuffle
from random import randint
from time import sleep

name = input("My name is Go Bot 5000 what is your name? ")
#name_q = input("Your name is " + name + " right? 1 or 0: 1 == yes 0 == no ")
#if name_q == '1':
print ("I like the name " + name, "!\n")
#elif name_q == '0':
#print("Ok can you tell me again please?\n")
#name = input("So what would you like me to call you?")
#else:
#print("Um... let's just start")

sleep(1)




ask = input(name + " would you like to play Go Fish? yes or no?: 1 or 0\n")

if ask == '1':
    print ('Okay then lets go!\n')
elif ask == '0':
    print ("Too bad we are playing anyways.\n")
else:
    print ("You were trying to say yes right? Well anyways lets go!\n")

sleep(2)




rules = input("Would you like to know what the rules are? Put 1 for yes and 0 for no.\n")
if rules == '1':
    print ("The rules are simple one player asks another if they have a certain type of card\n if they do they give them the card if not they must say go fish.")
    print ("The point of the game is to get as many groups of four cards as possible. These are called books.")
    print ("For today's occation, we will start dealing with five cards each, for how many players there are.\n")
    sleep(2)
elif rules == '0':
    print ("Oh lets keep going then!\n")
else:
    print("I don't think that was a yes let's just keep going\n")

sleep(3)




card_types = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"] 
deck = card_types * 4
value = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14}




print("As you see, this is a normal 52 card deck.\n")
print(deck)
sleep(2)
print("")




whole_deck = card_types * 4




def create_deck():
    print ("I will now show you the shuffled deck.\n")
    shuffle(deck)
    print(deck)
    sleep(3)
    print("\n")

create_deck()




print("We will choose the dealer by temporarily pulling out a card\nfrom the deck and decide by who's card is lowest.\n")
 
hand1 = []
hand2 = []
hand3 = []
hand4 = []
#def append(deck)
from random import randint
hand1 = deck[0]
deck.remove(deck[0])
hand2 = deck[0]
deck.remove(deck[0])
hand3 = deck[0]
deck.remove(deck[0])
hand4 = deck[0]
deck.remove(deck[0])

print("Here is your card")
print(hand1)
sleep(2)
print("")
print("Here is player two's card")
print(hand2)
sleep(2)
print("")
print("Here is player three's card")
print(hand3)
sleep(2)
print("")
print("Here is player four's card")
print(hand4)
sleep(2)
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("")
print("")

first = min(value[hand1], value[hand2], value[hand3], value[hand4])

#print("Whoever has this card will deal first")
#print(first)

if first == value[hand1]:
    print(name + ", you go first since you had the lowest card.\n")
    #first_player = 1
elif first == value[hand2]:
    print("Player 2 goes first since they have the lowest card.\n")
    #first_player = 2
elif first == value[hand3]:
    print("Player 3 goes first since they have the lowest card.\n")
    #first_player = 3
else:
    print("Player 4 goes first since they have the lowest card.\n")
    first_player = 4
#return first_player

#return
print("Ok, I will take the cards back and reshuffle the deck.\n")
sleep(3)
#create_deck


'''book_amount = 13

hand1_books = 0
hand2_books = 0
hand3_books = 0
hand4_books = 0


while hand1_books + hand2_books + hand3_books + hand4_books < 13:
    print("There are still", book_amount,"books available")
    hand1_books += 1
'''


play_deck = card_types * 4
shuffle(play_deck)
print(play_deck + "\n")
print("Done! Now let's get down with business!")

def make_deals():
    deal_amount = input("How many cards would you like each player to have?\n")

'''if deal_amount * 4 > 52:
    print("Wow! Way too much, dial it down a little, ok?\n Let's try that again")
    deal_amount = input("How many cards will you deal to each player?\n(Just make sure it's at most 13 ")
else:
    print("Ok, you're dealing each player" + deal_amount, "cards.")
'''
