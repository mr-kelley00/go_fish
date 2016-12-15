# Go Fish by Tristan and Karlos -ICT-3
# Version 0.0a - Published 10/11/16

print("Hello stranger")
player_1 = input("Whats your name? : ")

print("Hi", player_1, "would you like to play a game of Go Fish?")
rules = input( "type 1 for yes 2 for no :") #type yes or no here
if (rules == '1'):
    print ("Good! lets get started")
elif (rules == '2'):
    print ("Ok goodbye now")
    raise SystemExit
else:
    """Nothing"""
    
print ("Do you know know how to play Go Fish?") #type yes or no here
if rules == 'yes':
    print ("Ok lets begin")
else: 
    print ("go to http://www.bicyclecards.com/how-to-play/go-fish/ to learn more")
from random import randint
from random import shuffle
deck = ["Ace","Ace","Ace","Ace",2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"Jack","Jack","Jack","Jack","Queen","Queen","Queen","Queen","King","King","King","King"]
shuffle(deck)
print ("Ok", player_1, "Lets shuffle the deck")
p1_dealt = []
p2_dealt = []
p3_dealt = []
p4_dealt = []

