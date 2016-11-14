# version 1.7
# written by Hunter and Kenneth 

p1 = []
p2 = []
p3 = []
p4 = []
p1_dealt = 0
p1_hand = []
p2_hand = []
p3_hand = []
p4_hand = []
print("Welcome to Go-fish")
p1_name = input("Enter name! ")
rules = int(input("if you know the rules press 1 if not press 2: "))
if  rules == 2:
         print(" The object of the game is to win the most books of cards.")
         print("A book is a set of cards. In total there should be 13 books of 4.")
         print("The cards rank from the highest card (ace) the lowest (two).")
         print("The dealer gives out a card to each player faced up. The player with the lowest card number is the dealer.")
         print("The dealer deals out the cards cloclwise one at a time, and face down.")
         print("If there are 2-3 players each one recieves 7 cards. If there are 4-5 players each one recieves 5 cards.")
         print("The remainder of the cards are faced down on the table to be a stock.")
         print("The player to the left of the dealer goes first.")
         print("The player that goes first ask another opponent for a card ranking from ace to two.")
         print("The player must have at least 1 card that the player asked for.")
         print("The player that has been asked for the requested card must hand all of the cards asked for. For exmaple, if they asked for a 2 you must give them all your 2's.")
         print("If the player who has been asked for a certain card does not have any of the cards requested must say 'Go Fish', and the player who requested for that card must grab one card from the top of the stock.")
         print("If they get a match then they get to go again. The player keeps going until they get no more cards requested.")
         print("If a player gets a book of 4 matching cards, they place them on the table facing up.")
         print("If the player goes fishing without 'making a catch' of the requested cards, the turn passes to his left.")
         print("If a player runs out of cards, they wait until it is there turn and pick from the stock. If there is no cards then the player is out.")
         print("The game ends until all books have been won. The player with the most books wins.")

elif rules != 1  :
         print ("Thats not what we asked", p1_name)
         rules = int(input("if you know the rules press 1 if not press 2"))
         print(" The object of the game is to win the most books of cards.")
         print("A book is a set of cards. In total there should be 13 books of 4.")
         print("The cards rank from the highest card (ace) the lowest (two).")
         print("The dealer gives out a card to each player faced up. The player with the lowest card number is the dealer.")
         print("The dealer deals out the cards cloclwise one at a time, and face down.")
         print("If there are 2-3 players each one recieves 7 cards. If there are 4-5 players each one recieves 5 cards.")
         print("The remainder of the cards are faced down on the table to be a stock.")
         print("The player to the left of the dealer goes first.")
         print("The player that goes first ask another opponent for a card ranking from ace to two.")
         print("The player must have at least 1 card that the player asked for.")
         print("The player that has been asked for the requested card must hand all of the cards asked for. For exmaple, if they asked for a 2 you must give them all your 2's.")
         print("If the player who has been asked for a certain card does not have any of the cards requested must say 'Go Fish', and the player who requested for that card must grab one card from the top of the stock.")
         print("If they get a match then they get to go again. The player keeps going until they get no more cards requested.")
         print("If a player gets a book of 4 matching cards, they place them on the table facing up.")
         print("If the player goes fishing without 'making a catch' of the requested cards, the turn passes to his left.")
         print("If a player runs out of cards, they wait until it is there turn and pick from the stock. If there is no cards then the player is out.")
         print("The game ends until all books have been won. The player with the most books wins.")
    
else:
         print ("Lets play a game")

from random import shuffle
deck = ["2","2","2","2","3","3","3","3","4","4","4","4","5","5","5","5","6","6","6","6","7","7","7","7","8","8","8","8","9","9","9","9","10","10","10","10","J","J","J","J","Q","Q","Q","Q","K","K","K","K","A","A","A","A"]
values = {"2": 2 , "3": 3 , "4": 4 , "5": 5 , "6": 6 , "7": 7 , "8": 8 ,"9": 9 ,  "10": 10 , "J": 11 , "Q": 12 ,"K": 13 , "A": 14}
shuffle(deck)
p1.append(deck[0])
deck.remove(deck[0])
print (p1, "This is your card")
p2.append(deck[0])
deck.remove(deck[0])
print (p2, "This is P2's card")
p3.append(deck[0])
deck.remove(deck[0])
print (p3, "This is P3's card")
p4.append(deck[0])
deck.remove(deck[0])
print (p4, "This is P4's card")
if p1 < p2 and p3 and p4:
    print (p1_name,"goes first")
elif p2 < p1 and p3 and p4:
    print ("P2 goes first")
elif p3 < p1 and p2 and p4:
    print ("P3 goes first")
else:
    print ("P4 goes first")
while p1_dealt != 5 :
   p1_hand.append(deck[0])
   deck.remove(deck[0])
   p2_hand.append(deck[0])
   deck.remove(deck[0])
   p3_hand.append(deck[0])
   deck.remove(deck[0])
   p4_hand.append(deck[0])
   deck.remove(deck[0])
   p1_dealt += 1 
# print (p1_hand,("This is your hand ask a player for a matching card")



 
