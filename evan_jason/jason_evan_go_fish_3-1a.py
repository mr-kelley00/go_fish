# Go Fish Project - ICT-3 Project Created by Evan and Jason
# Version 3.1a
# Published 12/12/2016

# This makes the deck variable.

deck = ["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
value = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14}
full_deck = deck * 4
current_player = 0
asking_player = 0



# Now we shuffle the deck, randomness and sleep!

from time import sleep
from random import shuffle
shuffle(full_deck)

# Now let's introduce the program!

print("Welcome to Go Fish Version 3.1a! This program simulates the game Go Fish in a computer model!")
user = input("Before we start, what should I call you? [Type your name and press enter.] ")
print("Well, hello,", user, "we're almost ready to play Go Fish!")

# Now let's create a rules function!

def rules():
    rules = int(input("But before we start, do you know how to play Go Fish? Enter 0 for NO and 1 for YES. ")) 
    if rules == 0:
        print ("Okay then, well here are the rules!\n")
        sleep(2) # This creates a delay in when the next line is printed. 
        print ("THE PACK\n")
        print ("The standard 52-card pack is used. Some cards will be dealt and the rest will form the stock pile.\n")
        sleep(1)
        print ("OBJECT OF THE GAME\n")  
        print ("The goal is to win the most ""books"" of cards. A book is any four of a kind, such as four kings, four aces, and so on.\n")
        sleep(1)
        print ("RANK OF CARDS\n")    
        print ("The cards rank from ace (high) to two (low). The suits are not important, only the card numbers are relevant, such as two 3s, two 10s, and so on.\n")
        sleep(1)
        print ("THE DEAL\n")
        print ("Any player deals one card face up to each player. The player with the lowest card is the dealer. The dealer shuffles the cards, and the player on his right cuts them.")
        print ("The dealer completes the cut and deals the cards clockwise one at a time, face down, beginning with the player to his left. If two or three people are playing,")
        print ("each player receives seven cards. If four or five people are playing, each receives five cards. The remainder of the pack is placed face down on the table to form the stock.\n")
        sleep(1)
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
        rules = int(input("Input not correct. Please try again. Type 0 and then enter if you do not know how, type 1 if you already do! ")) # This line asks for the input of the user of a 0 or 1 to indicate if they have played Go Fish before or not.
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

    
# Now we set up the goes_first and book variables!
book1 = 0
book2 = 0
book3 = 0
book4 = 0
totalbooks = (book1 + book2 + book3 + book4)
# Now we set up the hand variables globally!

hand1 = []
hand2 = []
hand3 = []
hand4 = []

# Now we determine who goes first!

def who_goes_first():
        print ("Now we must determine who goes first.")
        hand1.append((full_deck[0]))
        full_deck.remove(full_deck[0])
        hand2.append((full_deck[0]))
        full_deck.remove(full_deck[0])
        hand3.append((full_deck[0]))
        full_deck.remove(full_deck[0])
        hand4.append((full_deck[0]))
        full_deck.remove(full_deck[0])
        
        print ("Here is your card,", user,":" , (hand1[0]))
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print ("Here are your oppenent's beginning cards!")
        print ("Player #2:" , (hand2[0]))
        print ("Player #3:" , (hand3[0]))
        print ("Player #4:" , (hand4[0]))
        sleep (7)
        print ()

        goes_first = min(value[hand1[0]], value[hand2[0]], value[hand3[0]], value[hand4[0]])    
        if value[hand1[0]] == goes_first:
            print (user,"goes first because they have the lowest card.")
            first_player = 1
        elif value[hand2[0]] == goes_first:
            print ("Player 2 goes first because they have the lowest card!.")
            first_Player = 2 
        elif value[hand3[0]] == goes_first:
            print ("Player 3 goes first because they have the lowest card!")
            first_player = 3   
        elif value[hand4[0]] == goes_first:
            print ("Player 4 goes first because they have the lowest card!")
            first_player = 4
        else:
             print ("I guess something happened. Please restart the program.")


print ("Now let's shuffle the deck to start!")

def reset_game():
    sleep(1)
    full_deck.append(hand1[0])
    full_deck.append(hand2[0])
    full_deck.append(hand3[0])
    full_deck.append(hand4[0])
    shuffle(full_deck)
    print ("Shuffling...")
    sleep(10)
    print ("Shuffling is now complete. The game is ready to begin.\n")

drawing_player = 0

    



def search_for_card_in_hand2_for_player_1():       
    print ("Here are your current cards:" ,hand1[0], ","  ,hand1[1],  ","  ,hand1[2],  "," ,hand1[3],  "and a" ,hand1[4], "!"  )
    
    acecount2 = hand2.count("Ace")
    kingcount2 = hand2.count("King")
    queencount2 = hand2.count("Queen")
    jackcount2 = hand2.count("Jack")
    twocount2 = hand2.count("Two")
    threecount2 = hand2.count("Three")
    fourcount2 = hand2.count("Four")
    fivecount2 = hand2.count("Five")
    sixcount2 = hand2.count("Six")
    sevencount2 = hand2.count("Seven")
    rightcount2 = hand2.count("Eight")
    ninecount2 = hand2.count("Nine")
    tencount2 = hand2.count("Ten")
    askingses = int(input("Type 1 for your first card, 2 for your second, 3 for your third, or 4 for your fourth.\n"))

    if askingses == 1:
        if hand1[0] == "Ace":
            if "Ace" not in hand2:
                print ("I do not have any Aces. Go fish!")
                drawing_player = 1
            elif "Ace" in hand2:
                if acecount2 == 1:
                    print ("I have one Ace. Here!")
                    hand2.remove("Ace")
                    hand1.append("Ace")
                    sleep (2)
                elif acecount2 == 2:
                    print ("I have two Aces. Here!")
                    while "Ace" in hand2:
                        hand2.remove("Ace")
                        hand1.append("Ace")
                elif acecount2 == 3:
                    print ("I have three Aces. Here!")
                    while "Ace" in hand2:
                        hand2.remove("Ace")
                        hand1.append("Ace")
                elif acecount2 == 4:
                    print ("I have four aces. Here...")
                    while "Ace" in hand2:
                        hand2.remove("Ace")
                        hand1.append("Ace")
                        
        elif hand1[0] == "King":
            if "King" not in hand2:
                print ("I do not have any Kings. Go fish!")
                drawing_player =1
            elif "King" in hand2:
                if kingcount2 == 1: 
                    print ("I have one King. Here!")
                    hand2.remove("King")
                    hand1.append("King")
                    sleep (2)
                elif kingcount2 == 2:
                    print ("I have two Kings. Here!")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                elif kingcount2 == 3:
                    print ("I have three Kings. Here!")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                elif kingcount2 == 4:
                    print ("I have four Kings. Here...")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                        
        elif hand1[0] == "Two":
            if "Two" not in hand2:
                print ("I do not have any Twos. Go fish!")
                drawing_player = 1
            elif "Two" in hand2:
                if twocount2 == 1:
                    print ("I have one Two. Here!")
                    hand2.remove("Two")
                    hand1.append("Two")
                    sleep (2)
                elif twocount2 == 2:
                    print ("I have two Twos. Here!")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                elif twocount2 == 3:
                    print ("I have three Twos. Here!")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                elif twocount2 == 4:
                    print ("I have four Twos. Here...")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                        
        elif hand1[0] == "Three":
            if "Three" not in hand2:
                print ("I do not have any Threes. Go fish!")
                drawing_player = 1
            elif "Three" in hand2:
                if threecount2 == 1:
                    print ("I have one Three. Here!")
                    hand2.remove("Three")
                    hand1.append("Three")
                    sleep (2)
                elif threecount2 == 2:
                    print ("I have two Threes. Here!")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")
                elif threecount2 == 3:
                    print ("I have three Threes. Here!")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")
                elif threecount2 == 4:
                    print ("I have four Threes. Here...")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")

            elif hand1[0] == "Four":
                if "Four" not in hand2:
                    print ("I do not have any Fours. Go fish!")
                    drawing_player = 1
                elif "Four" in hand2:
                    if fourcount2 == 1:
                        print ("I have one Four. Here!")
                        hand2.remove("Four")
                        hand1.append("Four")
                        sleep (2)
                    elif fourcount2 == 2:
                        print ("I have two Fours. Here!")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    elif fourcount2 == 3:
                        print ("I have three Fours. Here!")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    elif fourcount2 == 4:
                        print ("I have four Fours. Here...")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    
                    
            elif hand1[0] == "Five":
                if "Five" not in hand2:
                    print ("I do not have any Fives. Go fish!")
                    drawing_player = 1
                elif "Five" in hand2:
                    if fivecount2 == 1:
                        print ("I have one Five. Here!")
                        hand2.remove("Five")
                        hand1.append("Five")
                        sleep (2)
                    elif fivecount2 == 2:
                        print ("I have two Fives. Here!")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    elif fivecount2 == 3:
                        print ("I have three Fives. Here!")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    elif fivecount2 == 4:
                        print ("I have four Fives. Here...")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    

            elif hand1[0] == "Six":
                if "Six" not in hand2:
                    print ("I do not have any Sixes. Go fish!")
                    drawing_player = 1
                elif "Six" in hand2:
                    if sixcount2 == 1:
                        print ("I have one Six. Here!")
                        hand2.remove("Six")
                        hand1.append("Six")
                        sleep (2)
                    elif sixcount2 == 2:
                        print ("I have two Sixes. Here!")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    elif sixcount2 == 3:
                        print ("I have three Sixes. Here!")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    elif sixcount2 == 4:
                        print ("I have four Sixes. Here...")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    

            elif hand1[0] == "Seven":
                if "Seven" not in hand2:
                    print ("I do not have any Sevens. Go fish!")
                    drawing_player = 1
                elif "Seven" in hand2:
                    if sevencount2 == 1:
                        print ("I have one Seven. Here!")
                        hand2.remove("Seven")
                        hand1.append("Seven")
                        sleep (2)
                    elif sevencount2 == 2:
                        print ("I have two Sevens. Here!")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    elif sevencount2 == 3:
                        print ("I have three Sevens. Here!")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    elif sevencount2 == 4:
                        print ("I have four Sevens. Here...")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    

            elif hand1[0] == "Eight":
                if "Eight" not in hand2:
                    print ("I do not have any Eights. Go fish!")
                    drawing_player = 1
                elif "Eight" in hand2:
                    if eightcount2 == 1:
                        print ("I have one Eight. Here!")
                        hand2.remove("Eight")
                        hand1.append("Eight")
                        sleep (2)
                    elif eightcount2 == 2:
                        print ("I have two Eights. Here!")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    elif eightcount2 == 3:
                        print ("I have three Eights. Here!")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    elif eightcount2 == 4:
                        print ("I have four Eights. Here...")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    

            elif hand1[0] == "Nine":
                if "Nine" not in hand2:
                    print ("I do not have any Nines. Go fish!")
                    drawing_player = 1
                elif "Nine" in hand2:
                    if ninecount2 == 1:
                        print ("I have one Nine. Here!")
                        hand2.remove("Nine")
                        hand1.append("Nine")
                        sleep (2)
                    elif ninecount2 == 2:
                        print ("I have two Nines. Here!")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    elif ninecount2 == 3:
                        print ("I have three Nines. Here!")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    elif ninecount2 == 4:
                        print ("I have four Nines. Here...")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    

            elif hand1[0] == "Ten":
                if "Ten" not in hand2:
                    print ("I do not have any Tens. Go fish!")
                    drawing_player = 1
                elif "Ten" in hand2:
                    if tencount2 == 1:
                        print ("I have one Ten. Here!")
                        hand2.remove("Ten")
                        hand1.append("Ten")
                        sleep (2)
                    elif tencount2 == 2:
                        print ("I have two Tens. Here!")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    elif tencount2 == 3:
                        print ("I have three Tens. Here!")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    elif tencount2 == 4:
                        print ("I have four Tens. Here...")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    

            elif hand1[0] == "Jack":
                if "Jack" not in hand2:
                    print ("I do not have any Jacks. Go fish!")
                    drawing_player = 1
                elif "Jack" in hand2:
                    if jackcount2 == 1:
                        print ("I have one Jack. Here!")
                        hand2.remove("Jack")
                        hand1.append("Jack")
                        sleep (2)
                    elif jackcount2 == 2:
                        print ("I have two Jacks. Here!")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    elif jackcount2 == 3:
                        print ("I have three Jacks. Here!")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    elif jackcount2 == 4:
                        print ("I have four Jacks. Here...")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    

            elif hand1[0] == "Queen":
                if "Queen" not in hand2:
                    print ("I do not have any Queens. Go fish!")
                    drawing_player = 1
                elif "Queen" in hand2:
                    if queencount2 == 1:
                        print ("I have one Queen. Here!")
                        hand2.remove("Queen")
                        hand1.append("Queen")
                        sleep (2)
                    elif queencount2 == 2:
                        print ("I have two Queens. Here!")
                        while "Two" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")
                    elif queencount2 == 3:
                        print ("I have three Queen. Here!")
                        while "Queen" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")
                    elif queencount2 == 4:
                        print ("I have four Queens. Here...")
                        while "Queen" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")
                    
                        
    elif askingses == 2:
        if hand1[1] == "Ace":
            if "Ace" not in hand2:
                print ("I do not have any Aces. Go fish!")
                drawing_player = 1
            elif "Ace" in hand2:
                if acecount2 == 1:
                    print ("I have one Ace. Here!")
                    hand2.remove("Ace")
                    hand1.append("Ace")
                    sleep (2)
                elif acecount2 == 2:
                    print ("I have two Aces. Here!")
                    while "Ace" in hand2:
                        hand2.remove("Ace")
                        hand1.append("Ace")
                elif acecount2 == 3:
                    print ("I have three Aces. Here!")
                    while "Ace" in hand2:
                        hand2.remove("Ace")
                        hand1.append("Ace")
                elif acecount2 == 4:
                    print ("I have four aces. Here...")
                    while "Ace" in hand2:
                        hand2.remove("Ace")
                        hand1.append("Ace")
                        
        elif hand1[1] == "King":
            if "King" not in hand2:
                print ("I do not have any Kings. Go fish!")
                drawing_player =1
            elif "King" in hand2:
                if kingcount2 == 1: 
                    print ("I have one King. Here!")
                    hand2.remove("King")
                    hand1.append("King")
                    sleep (2)
                elif kingcount2 == 2:
                    print ("I have two Kings. Here!")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                elif kingcount2 == 3:
                    print ("I have three Kings. Here!")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                elif kingcount2 == 4:
                    print ("I have four Kings. Here...")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                        
        elif hand1[1] == "Two":
            if "Two" not in hand2:
                print ("I do not have any Twos. Go fish!")
                drawing_player = 1
            elif "Two" in hand2:
                if twocount2 == 1:
                    print ("I have one Two. Here!")
                    hand2.remove("Two")
                    hand1.append("Two")
                    sleep (2)
                elif twocount2 == 2:
                    print ("I have two Twos. Here!")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                elif twocount2 == 3:
                    print ("I have three Twos. Here!")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                elif twocount2 == 4:
                    print ("I have four Twos. Here...")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                        
        elif hand1[1] == "Three":
            if "Three" not in hand2:
                print ("I do not have any Threes. Go fish!")
                drawing_player = 1
            elif "Three" in hand2:
                if threecount2 == 1:
                    print ("I have one Three. Here!")
                    hand2.remove("Three")
                    hand1.append("Three")
                    sleep (2)
                elif threecount2 == 2:
                    print ("I have two Threes. Here!")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")
                elif threecount2 == 3:
                    print ("I have three Threes. Here!")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")
                elif threecount2 == 4:
                    print ("I have four Threes. Here...")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")

            elif hand1[1] == "Four":
                if "Four" not in hand2:
                    print ("I do not have any Fours. Go fish!")
                    drawing_player = 1
                elif "Four" in hand2:
                    if fourcount2 == 1:
                        print ("I have one Four. Here!")
                        hand2.remove("Four")
                        hand1.append("Four")
                        sleep (2)
                    elif fourcount2 == 2:
                        print ("I have two Fours. Here!")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    elif fourcount2 == 3:
                        print ("I have three Fours. Here!")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    elif fourcount2 == 4:
                        print ("I have four Fours. Here...")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    
                    
            elif hand1[1] == "Five":
                if "Five" not in hand2:
                    print ("I do not have any Fives. Go fish!")
                    drawing_player = 1
                elif "Five" in hand2:
                    if fivecount2 == 1:
                        print ("I have one Five. Here!")
                        hand2.remove("Five")
                        hand1.append("Five")
                        sleep (2)
                    elif fivecount2 == 2:
                        print ("I have two Fives. Here!")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    elif fivecount2 == 3:
                        print ("I have three Fives. Here!")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    elif fivecount2 == 4:
                        print ("I have four Fives. Here...")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    

            elif hand1[1] == "Six":
                if "Six" not in hand2:
                    print ("I do not have any Sixes. Go fish!")
                    drawing_player = 1
                elif "Six" in hand2:
                    if sixcount2 == 1:
                        print ("I have one Six. Here!")
                        hand2.remove("Six")
                        hand1.append("Six")
                        sleep (2)
                    elif sixcount2 == 2:
                        print ("I have two Sixes. Here!")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    elif sixcount2 == 3:
                        print ("I have three Sixes. Here!")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    elif sixcount2 == 4:
                        print ("I have four Sixes. Here...")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    

            elif hand1[1] == "Seven":
                if "Seven" not in hand2:
                    print ("I do not have any Sevens. Go fish!")
                    drawing_player = 1
                elif "Seven" in hand2:
                    if sevencount2 == 1:
                        print ("I have one Seven. Here!")
                        hand2.remove("Seven")
                        hand1.append("Seven")
                        sleep (2)
                    elif sevencount2 == 2:
                        print ("I have two Sevens. Here!")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    elif sevencount2 == 3:
                        print ("I have three Sevens. Here!")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    elif sevencount2 == 4:
                        print ("I have four Sevens. Here...")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    

            elif hand1[1] == "Eight":
                if "Eight" not in hand2:
                    print ("I do not have any Eights. Go fish!")
                    drawing_player = 1
                elif "Eight" in hand2:
                    if eightcount2 == 1:
                        print ("I have one Eight. Here!")
                        hand2.remove("Eight")
                        hand1.append("Eight")
                        sleep (2)
                    elif eightcount2 == 2:
                        print ("I have two Eights. Here!")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    elif eightcount2 == 3:
                        print ("I have three Eights. Here!")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    elif eightcount2 == 4:
                        print ("I have four Eights. Here...")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    

            elif hand1[1] == "Nine":
                if "Nine" not in hand2:
                    print ("I do not have any Nines. Go fish!")
                    drawing_player = 1
                elif "Nine" in hand2:
                    if ninecount2 == 1:
                        print ("I have one Nine. Here!")
                        hand2.remove("Nine")
                        hand1.append("Nine")
                        sleep (2)
                    elif ninecount2 == 2:
                        print ("I have two Nines. Here!")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    elif ninecount2 == 3:
                        print ("I have three Nines. Here!")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    elif ninecount2 == 4:
                        print ("I have four Nines. Here...")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    

            elif hand1[1] == "Ten":
                if "Ten" not in hand2:
                    print ("I do not have any Tens. Go fish!")
                    drawing_player = 1
                elif "Ten" in hand2:
                    if tencount2 == 1:
                        print ("I have one Ten. Here!")
                        hand2.remove("Ten")
                        hand1.append("Ten")
                        sleep (2)
                    elif tencount2 == 2:
                        print ("I have two Tens. Here!")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    elif tencount2 == 3:
                        print ("I have three Tens. Here!")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    elif tencount2 == 4:
                        print ("I have four Tens. Here...")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    

            elif hand1[1] == "Jack":
                if "Jack" not in hand2:
                    print ("I do not have any Jacks. Go fish!")
                    drawing_player = 1
                elif "Jack" in hand2:
                    if jackcount2 == 1:
                        print ("I have one Jack. Here!")
                        hand2.remove("Jack")
                        hand1.append("Jack")
                        sleep (2)
                    elif jackcount2 == 2:
                        print ("I have two Jacks. Here!")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    elif jackcount2 == 3:
                        print ("I have three Jacks. Here!")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    elif jackcount2 == 4:
                        print ("I have four Jacks. Here...")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    

            elif hand1[1] == "Queen":
                if "Queen" not in hand2:
                    print ("I do not have any Queens. Go fish!")
                    drawing_player = 1
                elif "Queen" in hand2:
                    if queencount2 == 1:
                        print ("I have one Queen. Here!")
                        hand2.remove("Queen")
                        hand1.append("Queen")
                        sleep (2)
                    elif queencount2 == 2:
                        print ("I have two Queens. Here!")
                        while "Two" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")
                    elif queencount2 == 3:
                        print ("I have three Queen. Here!")
                        while "Queen" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")
                    elif queencount2 == 4:
                        print ("I have four Queens. Here...")
                        while "Queen" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")
        
    elif askingses == 3:
        if hand1[2] == "Ace":
            if "Ace" not in hand2:
                print ("I do not have any Aces. Go fish!")
                drawing_player = 1
            elif "Ace" in hand2:
                if acecount2 == 1:
                    print ("I have one Ace. Here!")
                    hand2.remove("Ace")
                    hand1.append("Ace")
                    sleep (2)
                elif acecount2 == 2:
                    print ("I have two Aces. Here!")
                    while "Ace" in hand2:
                        hand2.remove("Ace")
                        hand1.append("Ace")
                elif acecount2 == 3:
                    print ("I have three Aces. Here!")
                    while "Ace" in hand2:
                        hand2.remove("Ace")
                        hand1.append("Ace")
                elif acecount2 == 4:
                    print ("I have four aces. Here...")
                    while "Ace" in hand2:
                        hand2.remove("Ace")
                        hand1.append("Ace")
                        
        elif hand1[2] == "King":
            if "King" not in hand2:
                print ("I do not have any Kings. Go fish!")
                drawing_player =1
            elif "King" in hand2:
                if kingcount2 == 1: 
                    print ("I have one King. Here!")
                    hand2.remove("King")
                    hand1.append("King")
                    sleep (2)
                elif kingcount2 == 2:
                    print ("I have two Kings. Here!")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                elif kingcount2 == 3:
                    print ("I have three Kings. Here!")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                elif kingcount2 == 4:
                    print ("I have four Kings. Here...")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                        
        elif hand1[2] == "Two":
            if "Two" not in hand2:
                print ("I do not have any Twos. Go fish!")
                drawing_player = 1
            elif "Two" in hand2:
                if twocount2 == 1:
                    print ("I have one Two. Here!")
                    hand2.remove("Two")
                    hand1.append("Two")
                    sleep (2)
                elif twocount2 == 2:
                    print ("I have two Twos. Here!")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                elif twocount2 == 3:
                    print ("I have three Twos. Here!")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                elif twocount2 == 4:
                    print ("I have four Twos. Here...")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                        
        elif hand1[2] == "Three":
            if "Three" not in hand2:
                print ("I do not have any Threes. Go fish!")
                drawing_player = 1
            elif "Three" in hand2:
                if threecount2 == 1:
                    print ("I have one Three. Here!")
                    hand2.remove("Three")
                    hand1.append("Three")
                    sleep (2)
                elif threecount2 == 2:
                    print ("I have two Threes. Here!")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")
                elif threecount2 == 3:
                    print ("I have three Threes. Here!")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")
                elif threecount2 == 4:
                    print ("I have four Threes. Here...")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")

            elif hand1[2] == "Four":
                if "Four" not in hand2:
                    print ("I do not have any Fours. Go fish!")
                    drawing_player = 1
                elif "Four" in hand2:
                    if fourcount2 == 1:
                        print ("I have one Four. Here!")
                        hand2.remove("Four")
                        hand1.append("Four")
                        sleep (2)
                    elif fourcount2 == 2:
                        print ("I have two Fours. Here!")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    elif fourcount2 == 3:
                        print ("I have three Fours. Here!")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    elif fourcount2 == 4:
                        print ("I have four Fours. Here...")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    
                    
            elif hand1[2] == "Five":
                if "Five" not in hand2:
                    print ("I do not have any Fives. Go fish!")
                    drawing_player = 1
                elif "Five" in hand2:
                    if fivecount2 == 1:
                        print ("I have one Five. Here!")
                        hand2.remove("Five")
                        hand1.append("Five")
                        sleep (2)
                    elif fivecount2 == 2:
                        print ("I have two Fives. Here!")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    elif fivecount2 == 3:
                        print ("I have three Fives. Here!")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    elif fivecount2 == 4:
                        print ("I have four Fives. Here...")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    

            elif hand1[2] == "Six":
                if "Six" not in hand2:
                    print ("I do not have any Sixes. Go fish!")
                    drawing_player = 1
                elif "Six" in hand2:
                    if sixcount2 == 1:
                        print ("I have one Six. Here!")
                        hand2.remove("Six")
                        hand1.append("Six")
                        sleep (2)
                    elif sixcount2 == 2:
                        print ("I have two Sixes. Here!")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    elif sixcount2 == 3:
                        print ("I have three Sixes. Here!")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    elif sixcount2 == 4:
                        print ("I have four Sixes. Here...")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    

            elif hand1[2] == "Seven":
                if "Seven" not in hand2:
                    print ("I do not have any Sevens. Go fish!")
                    drawing_player = 1
                elif "Seven" in hand2:
                    if sevencount2 == 1:
                        print ("I have one Seven. Here!")
                        hand2.remove("Seven")
                        hand1.append("Seven")
                        sleep (2)
                    elif sevencount2 == 2:
                        print ("I have two Sevens. Here!")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    elif sevencount2 == 3:
                        print ("I have three Sevens. Here!")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    elif sevencount2 == 4:
                        print ("I have four Sevens. Here...")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    

            elif hand1[2] == "Eight":
                if "Eight" not in hand2:
                    print ("I do not have any Eights. Go fish!")
                    drawing_player = 1
                elif "Eight" in hand2:
                    if eightcount2 == 1:
                        print ("I have one Eight. Here!")
                        hand2.remove("Eight")
                        hand1.append("Eight")
                        sleep (2)
                    elif eightcount2 == 2:
                        print ("I have two Eights. Here!")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    elif eightcount2 == 3:
                        print ("I have three Eights. Here!")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    elif eightcount2 == 4:
                        print ("I have four Eights. Here...")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    

            elif hand1[2] == "Nine":
                if "Nine" not in hand2:
                    print ("I do not have any Nines. Go fish!")
                    drawing_player = 1
                elif "Nine" in hand2:
                    if ninecount2 == 1:
                        print ("I have one Nine. Here!")
                        hand2.remove("Nine")
                        hand1.append("Nine")
                        sleep (2)
                    elif ninecount2 == 2:
                        print ("I have two Nines. Here!")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    elif ninecount2 == 3:
                        print ("I have three Nines. Here!")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    elif ninecount2 == 4:
                        print ("I have four Nines. Here...")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    

            elif hand1[2] == "Ten":
                if "Ten" not in hand2:
                    print ("I do not have any Tens. Go fish!")
                    drawing_player = 1
                elif "Ten" in hand2:
                    if tencount2 == 1:
                        print ("I have one Ten. Here!")
                        hand2.remove("Ten")
                        hand1.append("Ten")
                        sleep (2)
                    elif tencount2 == 2:
                        print ("I have two Tens. Here!")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    elif tencount2 == 3:
                        print ("I have three Tens. Here!")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    elif tencount2 == 4:
                        print ("I have four Tens. Here...")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    

            elif hand1[2] == "Jack":
                if "Jack" not in hand2:
                    print ("I do not have any Jacks. Go fish!")
                    drawing_player = 1
                elif "Jack" in hand2:
                    if jackcount2 == 1:
                        print ("I have one Jack. Here!")
                        hand2.remove("Jack")
                        hand1.append("Jack")
                        sleep (2)
                    elif jackcount2 == 2:
                        print ("I have two Jacks. Here!")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    elif jackcount2 == 3:
                        print ("I have three Jacks. Here!")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    elif jackcount2 == 4:
                        print ("I have four Jacks. Here...")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    

            elif hand1[2] == "Queen":
                if "Queen" not in hand2:
                    print ("I do not have any Queens. Go fish!")
                    drawing_player = 1
                elif "Queen" in hand2:
                    if queencount2 == 1:
                        print ("I have one Queen. Here!")
                        hand2.remove("Queen")
                        hand1.append("Queen")
                        sleep (2)
                    elif queencount2 == 2:
                        print ("I have two Queens. Here!")
                        while "Two" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")
                    elif queencount2 == 3:
                        print ("I have three Queen. Here!")
                        while "Queen" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")
                    elif queencount2 == 4:
                        print ("I have four Queens. Here...")
                        while "Queen" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")
    elif askingses == 4:
        if hand1[3] == "Ace":
            if "Ace" not in hand2:
                print ("I do not have any Aces. Go fish!")
                drawing_player = 1
            elif "Ace" in hand2:
                if acecount2 == 1:
                    print ("I have one Ace. Here!")
                    hand2.remove("Ace")
                    hand1.append("Ace")
                    sleep (2)
                elif acecount2 == 2:
                    print ("I have two Aces. Here!")
                    while "Ace" in hand2:
                        hand2.remove("Ace")
                        hand1.append("Ace")
                elif acecount2 == 3:
                    print ("I have three Aces. Here!")
                    while "Ace" in hand2:
                        hand2.remove("Ace")
                        hand1.append("Ace")
                elif acecount2 == 4:
                    print ("I have four aces. Here...")
                    while "Ace" in hand2:
                        hand2.remove("Ace")
                        hand1.append("Ace")
                        
        elif hand1[3] == "King":
            if "King" not in hand2:
                print ("I do not have any Kings. Go fish!")
                drawing_player =1
            elif "King" in hand2:
                if kingcount2 == 1: 
                    print ("I have one King. Here!")
                    hand2.remove("King")
                    hand1.append("King")
                    sleep (2)
                elif kingcount2 == 2:
                    print ("I have two Kings. Here!")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                elif kingcount2 == 3:
                    print ("I have three Kings. Here!")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                elif kingcount2 == 4:
                    print ("I have four Kings. Here...")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                        
        elif hand1[3] == "Two":
            if "Two" not in hand2:
                print ("I do not have any Twos. Go fish!")
                drawing_player = 1
            elif "Two" in hand2:
                if twocount2 == 1:
                    print ("I have one Two. Here!")
                    hand2.remove("Two")
                    hand1.append("Two")
                    sleep (2)
                elif twocount2 == 2:
                    print ("I have two Twos. Here!")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                elif twocount2 == 3:
                    print ("I have three Twos. Here!")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                elif twocount2 == 4:
                    print ("I have four Twos. Here...")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                        
        elif hand1[3] == "Three":
            if "Three" not in hand2:
                print ("I do not have any Threes. Go fish!")
                drawing_player = 1
            elif "Three" in hand2:
                if threecount2 == 1:
                    print ("I have one Three. Here!")
                    hand2.remove("Three")
                    hand1.append("Three")
                    sleep (2)
                elif threecount2 == 2:
                    print ("I have two Threes. Here!")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")
                elif threecount2 == 3:
                    print ("I have three Threes. Here!")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")
                elif threecount2 == 4:
                    print ("I have four Threes. Here...")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")

            elif hand1[3] == "Four":
                if "Four" not in hand2:
                    print ("I do not have any Fours. Go fish!")
                    drawing_player = 1
                elif "Four" in hand2:
                    if fourcount2 == 1:
                        print ("I have one Four. Here!")
                        hand2.remove("Four")
                        hand1.append("Four")
                        sleep (2)
                    elif fourcount2 == 2:
                        print ("I have two Fours. Here!")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    elif fourcount2 == 3:
                        print ("I have three Fours. Here!")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    elif fourcount2 == 4:
                        print ("I have four Fours. Here...")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    
                    
            elif hand1[3] == "Five":
                if "Five" not in hand2:
                    print ("I do not have any Fives. Go fish!")
                    drawing_player = 1
                elif "Five" in hand2:
                    if fivecount2 == 1:
                        print ("I have one Five. Here!")
                        hand2.remove("Five")
                        hand1.append("Five")
                        sleep (2)
                    elif fivecount2 == 2:
                        print ("I have two Fives. Here!")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    elif fivecount2 == 3:
                        print ("I have three Fives. Here!")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    elif fivecount2 == 4:
                        print ("I have four Fives. Here...")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    

            elif hand1[3] == "Six":
                if "Six" not in hand2:
                    print ("I do not have any Sixes. Go fish!")
                    drawing_player = 1
                elif "Six" in hand2:
                    if sixcount2 == 1:
                        print ("I have one Six. Here!")
                        hand2.remove("Six")
                        hand1.append("Six")
                        sleep (2)
                    elif sixcount2 == 2:
                        print ("I have two Sixes. Here!")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    elif sixcount2 == 3:
                        print ("I have three Sixes. Here!")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    elif sixcount2 == 4:
                        print ("I have four Sixes. Here...")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    

            elif hand1[3] == "Seven":
                if "Seven" not in hand2:
                    print ("I do not have any Sevens. Go fish!")
                    drawing_player = 1
                elif "Seven" in hand2:
                    if sevencount2 == 1:
                        print ("I have one Seven. Here!")
                        hand2.remove("Seven")
                        hand1.append("Seven")
                        sleep (2)
                    elif sevencount2 == 2:
                        print ("I have two Sevens. Here!")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    elif sevencount2 == 3:
                        print ("I have three Sevens. Here!")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    elif sevencount2 == 4:
                        print ("I have four Sevens. Here...")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    

            elif hand1[3] == "Eight":
                if "Eight" not in hand2:
                    print ("I do not have any Eights. Go fish!")
                    drawing_player = 1
                elif "Eight" in hand2:
                    if eightcount2 == 1:
                        print ("I have one Eight. Here!")
                        hand2.remove("Eight")
                        hand1.append("Eight")
                        sleep (2)
                    elif eightcount2 == 2:
                        print ("I have two Eights. Here!")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    elif eightcount2 == 3:
                        print ("I have three Eights. Here!")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    elif eightcount2 == 4:
                        print ("I have four Eights. Here...")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    

            elif hand1[3] == "Nine":
                if "Nine" not in hand2:
                    print ("I do not have any Nines. Go fish!")
                    drawing_player = 1
                elif "Nine" in hand2:
                    if ninecount2 == 1:
                        print ("I have one Nine. Here!")
                        hand2.remove("Nine")
                        hand1.append("Nine")
                        sleep (2)
                    elif ninecount2 == 2:
                        print ("I have two Nines. Here!")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    elif ninecount2 == 3:
                        print ("I have three Nines. Here!")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    elif ninecount2 == 4:
                        print ("I have four Nines. Here...")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    

            elif hand1[3] == "Ten":
                if "Ten" not in hand2:
                    print ("I do not have any Tens. Go fish!")
                    drawing_player = 1
                elif "Ten" in hand2:
                    if tencount2 == 1:
                        print ("I have one Ten. Here!")
                        hand2.remove("Ten")
                        hand1.append("Ten")
                        sleep (2)
                    elif tencount2 == 2:
                        print ("I have two Tens. Here!")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    elif tencount2 == 3:
                        print ("I have three Tens. Here!")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    elif tencount2 == 4:
                        print ("I have four Tens. Here...")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    

            elif hand1[3] == "Jack":
                if "Jack" not in hand2:
                    print ("I do not have any Jacks. Go fish!")
                    drawing_player = 1
                elif "Jack" in hand2:
                    if jackcount2 == 1:
                        print ("I have one Jack. Here!")
                        hand2.remove("Jack")
                        hand1.append("Jack")
                        sleep (2)
                    elif jackcount2 == 2:
                        print ("I have two Jacks. Here!")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    elif jackcount2 == 3:
                        print ("I have three Jacks. Here!")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    elif jackcount2 == 4:
                        print ("I have four Jacks. Here...")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    

            elif hand1[3] == "Queen":
                if "Queen" not in hand2:
                    print ("I do not have any Queens. Go fish!")
                    drawing_player = 1
                elif "Queen" in hand2:
                    if queencount2 == 1:
                        print ("I have one Queen. Here!")
                        hand2.remove("Queen")
                        hand1.append("Queen")
                        sleep (2)
                    elif queencount2 == 2:
                        print ("I have two Queens. Here!")
                        while "Two" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")
                    elif queencount2 == 3:
                        print ("I have three Queen. Here!")
                        while "Queen" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")
                    elif queencount2 == 4:
                        print ("I have four Queens. Here...")
                        while "Queen" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")
    elif askingses == 5:
        if hand1[4] == "Ace":
            if "Ace" not in hand2:
                print ("I do not have any Aces. Go fish!")
                drawing_player = 1
            elif "Ace" in hand2:
                if acecount2 == 1:
                    print ("I have one Ace. Here!")
                    hand2.remove("Ace")
                    hand1.append("Ace")
                    sleep (2)
                elif acecount2 == 2:
                    print ("I have two Aces. Here!")
                    while "Ace" in hand2:
                        hand2.remove("Ace")
                        hand1.append("Ace")
                elif acecount2 == 3:
                    print ("I have three Aces. Here!")
                    while "Ace" in hand2:
                        hand2.remove("Ace")
                        hand1.append("Ace")
                elif acecount2 == 4:
                    print ("I have four aces. Here...")
                    while "Ace" in hand2:
                        hand2.remove("Ace")
                        hand1.append("Ace")
                        
        elif hand1[4] == "King":
            if "King" not in hand2:
                print ("I do not have any Kings. Go fish!")
                drawing_player =1
            elif "King" in hand2:
                if kingcount2 == 1: 
                    print ("I have one King. Here!")
                    hand2.remove("King")
                    hand1.append("King")
                    sleep (2)
                elif kingcount2 == 2:
                    print ("I have two Kings. Here!")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                elif kingcount2 == 3:
                    print ("I have three Kings. Here!")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                elif kingcount2 == 4:
                    print ("I have four Kings. Here...")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                        
        elif hand1[4] == "Two":
            if "Two" not in hand2:
                print ("I do not have any Twos. Go fish!")
                drawing_player = 1
            elif "Two" in hand2:
                if twocount2 == 1:
                    print ("I have one Two. Here!")
                    hand2.remove("Two")
                    hand1.append("Two")
                    sleep (2)
                elif twocount2 == 2:
                    print ("I have two Twos. Here!")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                elif twocount2 == 3:
                    print ("I have three Twos. Here!")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                elif twocount2 == 4:
                    print ("I have four Twos. Here...")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                        
        elif hand1[4] == "Three":
            if "Three" not in hand2:
                print ("I do not have any Threes. Go fish!")
                drawing_player = 1
            elif "Three" in hand2:
                if threecount2 == 1:
                    print ("I have one Three. Here!")
                    hand2.remove("Three")
                    hand1.append("Three")
                    sleep (2)
                elif threecount2 == 2:
                    print ("I have two Threes. Here!")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")
                elif threecount2 == 3:
                    print ("I have three Threes. Here!")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")
                elif threecount2 == 4:
                    print ("I have four Threes. Here...")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")

            elif hand1[4] == "Four":
                if "Four" not in hand2:
                    print ("I do not have any Fours. Go fish!")
                    drawing_player = 1
                elif "Four" in hand2:
                    if fourcount2 == 1:
                        print ("I have one Four. Here!")
                        hand2.remove("Four")
                        hand1.append("Four")
                        sleep (2)
                    elif fourcount2 == 2:
                        print ("I have two Fours. Here!")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    elif fourcount2 == 3:
                        print ("I have three Fours. Here!")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    elif fourcount2 == 4:
                        print ("I have four Fours. Here...")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    
                    
            elif hand1[4] == "Five":
                if "Five" not in hand2:
                    print ("I do not have any Fives. Go fish!")
                    drawing_player = 1
                elif "Five" in hand2:
                    if fivecount2 == 1:
                        print ("I have one Five. Here!")
                        hand2.remove("Five")
                        hand1.append("Five")
                        sleep (2)
                    elif fivecount2 == 2:
                        print ("I have two Fives. Here!")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    elif fivecount2 == 3:
                        print ("I have three Fives. Here!")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    elif fivecount2 == 4:
                        print ("I have four Fives. Here...")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    

            elif hand1[4] == "Six":
                if "Six" not in hand2:
                    print ("I do not have any Sixes. Go fish!")
                    drawing_player = 1
                elif "Six" in hand2:
                    if sixcount2 == 1:
                        print ("I have one Six. Here!")
                        hand2.remove("Six")
                        hand1.append("Six")
                        sleep (2)
                    elif sixcount2 == 2:
                        print ("I have two Sixes. Here!")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    elif sixcount2 == 3:
                        print ("I have three Sixes. Here!")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    elif sixcount2 == 4:
                        print ("I have four Sixes. Here...")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    

            elif hand1[4] == "Seven":
                if "Seven" not in hand2:
                    print ("I do not have any Sevens. Go fish!")
                    drawing_player = 1
                elif "Seven" in hand2:
                    if sevencount2 == 1:
                        print ("I have one Seven. Here!")
                        hand2.remove("Seven")
                        hand1.append("Seven")
                        sleep (2)
                    elif sevencount2 == 2:
                        print ("I have two Sevens. Here!")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    elif sevencount2 == 3:
                        print ("I have three Sevens. Here!")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    elif sevencount2 == 4:
                        print ("I have four Sevens. Here...")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    

            elif hand1[4] == "Eight":
                if "Eight" not in hand2:
                    print ("I do not have any Eights. Go fish!")
                    drawing_player = 1
                elif "Eight" in hand2:
                    if eightcount2 == 1:
                        print ("I have one Eight. Here!")
                        hand2.remove("Eight")
                        hand1.append("Eight")
                        sleep (2)
                    elif eightcount2 == 2:
                        print ("I have two Eights. Here!")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    elif eightcount2 == 3:
                        print ("I have three Eights. Here!")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    elif eightcount2 == 4:
                        print ("I have four Eights. Here...")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    

            elif hand1[4] == "Nine":
                if "Nine" not in hand2:
                    print ("I do not have any Nines. Go fish!")
                    drawing_player = 1
                elif "Nine" in hand2:
                    if ninecount2 == 1:
                        print ("I have one Nine. Here!")
                        hand2.remove("Nine")
                        hand1.append("Nine")
                        sleep (2)
                    elif ninecount2 == 2:
                        print ("I have two Nines. Here!")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    elif ninecount2 == 3:
                        print ("I have three Nines. Here!")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    elif ninecount2 == 4:
                        print ("I have four Nines. Here...")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    

            elif hand1[4] == "Ten":
                if "Ten" not in hand2:
                    print ("I do not have any Tens. Go fish!")
                    drawing_player = 1
                elif "Ten" in hand2:
                    if tencount2 == 1:
                        print ("I have one Ten. Here!")
                        hand2.remove("Ten")
                        hand1.append("Ten")
                        sleep (2)
                    elif tencount2 == 2:
                        print ("I have two Tens. Here!")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    elif tencount2 == 3:
                        print ("I have three Tens. Here!")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    elif tencount2 == 4:
                        print ("I have four Tens. Here...")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    

            elif hand1[4] == "Jack":
                if "Jack" not in hand2:
                    print ("I do not have any Jacks. Go fish!")
                    drawing_player = 1
                elif "Jack" in hand2:
                    if jackcount2 == 1:
                        print ("I have one Jack. Here!")
                        hand2.remove("Jack")
                        hand1.append("Jack")
                        sleep (2)
                    elif jackcount2 == 2:
                        print ("I have two Jacks. Here!")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    elif jackcount2 == 3:
                        print ("I have three Jacks. Here!")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    elif jackcount2 == 4:
                        print ("I have four Jacks. Here...")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    

            elif hand1[4] == "Queen":
                if "Queen" not in hand2:
                    print ("I do not have any Queens. Go fish!")
                    drawing_player = 1
                elif "Queen" in hand2:
                    if queencount2 == 1:
                        print ("I have one Queen. Here!")
                        hand2.remove("Queen")
                        hand1.append("Queen")
                        sleep (2)
                    elif queencount2 == 2:
                        print ("I have two Queens. Here!")
                        while "Two" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")
                    elif queencount2 == 3:
                        print ("I have three Queen. Here!")
                        while "Queen" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")
                    elif queencount2 == 4:
                        print ("I have four Queens. Here...")
                        while "Queen" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")

        elif askingses == 6:
            if hand1[5] == "Ace":
                if "Ace" not in hand2:
                    print ("I do not have any Aces. Go fish!")
                    drawing_player = 1
                elif "Ace" in hand2:
                    if acecount2 == 1:
                        print ("I have one Ace. Here!")
                        hand2.remove("Ace")
                        hand1.append("Ace")
                        sleep (2)
                    elif acecount2 == 2:
                        print ("I have two Aces. Here!")
                        while "Ace" in hand2:
                            hand2.remove("Ace")
                            hand1.append("Ace")
                    elif acecount2 == 3:
                        print ("I have three Aces. Here!")
                        while "Ace" in hand2:
                            hand2.remove("Ace")
                            hand1.append("Ace")
                    elif acecount2 == 4:
                        print ("I have four aces. Here...")
                        while "Ace" in hand2:
                            hand2.remove("Ace")
                            hand1.append("Ace")
                        
        elif hand1[5] == "King":
            if "King" not in hand2:
                print ("I do not have any Kings. Go fish!")
                drawing_player =1
            elif "King" in hand2:
                if kingcount2 == 1: 
                    print ("I have one King. Here!")
                    hand2.remove("King")
                    hand1.append("King")
                    sleep (2)
                elif kingcount2 == 2:
                    print ("I have two Kings. Here!")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                elif kingcount2 == 3:
                    print ("I have three Kings. Here!")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                elif kingcount2 == 4:
                    print ("I have four Kings. Here...")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                        
        elif hand1[5] == "Two":
            if "Two" not in hand2:
                print ("I do not have any Twos. Go fish!")
                drawing_player = 1
            elif "Two" in hand2:
                if twocount2 == 1:
                    print ("I have one Two. Here!")
                    hand2.remove("Two")
                    hand1.append("Two")
                    sleep (2)
                elif twocount2 == 2:
                    print ("I have two Twos. Here!")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                elif twocount2 == 3:
                    print ("I have three Twos. Here!")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                elif twocount2 == 4:
                    print ("I have four Twos. Here...")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                        
        elif hand1[5] == "Three":
            if "Three" not in hand2:
                print ("I do not have any Threes. Go fish!")
                drawing_player = 1
            elif "Three" in hand2:
                if threecount2 == 1:
                    print ("I have one Three. Here!")
                    hand2.remove("Three")
                    hand1.append("Three")
                    sleep (2)
                elif threecount2 == 2:
                    print ("I have two Threes. Here!")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")
                elif threecount2 == 3:
                    print ("I have three Threes. Here!")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")
                elif threecount2 == 4:
                    print ("I have four Threes. Here...")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")

            elif hand1[5] == "Four":
                if "Four" not in hand2:
                    print ("I do not have any Fours. Go fish!")
                    drawing_player = 1
                elif "Four" in hand2:
                    if fourcount2 == 1:
                        print ("I have one Four. Here!")
                        hand2.remove("Four")
                        hand1.append("Four")
                        sleep (2)
                    elif fourcount2 == 2:
                        print ("I have two Fours. Here!")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    elif fourcount2 == 3:
                        print ("I have three Fours. Here!")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    elif fourcount2 == 4:
                        print ("I have four Fours. Here...")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    
                    
            elif hand1[5] == "Five":
                if "Five" not in hand2:
                    print ("I do not have any Fives. Go fish!")
                    drawing_player = 1
                elif "Five" in hand2:
                    if fivecount2 == 1:
                        print ("I have one Five. Here!")
                        hand2.remove("Five")
                        hand1.append("Five")
                        sleep (2)
                    elif fivecount2 == 2:
                        print ("I have two Fives. Here!")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    elif fivecount2 == 3:
                        print ("I have three Fives. Here!")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    elif fivecount2 == 4:
                        print ("I have four Fives. Here...")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    

            elif hand1[5] == "Six":
                if "Six" not in hand2:
                    print ("I do not have any Sixes. Go fish!")
                    drawing_player = 1
                elif "Six" in hand2:
                    if sixcount2 == 1:
                        print ("I have one Six. Here!")
                        hand2.remove("Six")
                        hand1.append("Six")
                        sleep (2)
                    elif sixcount2 == 2:
                        print ("I have two Sixes. Here!")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    elif sixcount2 == 3:
                        print ("I have three Sixes. Here!")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    elif sixcount2 == 4:
                        print ("I have four Sixes. Here...")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    

            elif hand1[5] == "Seven":
                if "Seven" not in hand2:
                    print ("I do not have any Sevens. Go fish!")
                    drawing_player = 1
                elif "Seven" in hand2:
                    if sevencount2 == 1:
                        print ("I have one Seven. Here!")
                        hand2.remove("Seven")
                        hand1.append("Seven")
                        sleep (2)
                    elif sevencount2 == 2:
                        print ("I have two Sevens. Here!")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    elif sevencount2 == 3:
                        print ("I have three Sevens. Here!")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    elif sevencount2 == 4:
                        print ("I have four Sevens. Here...")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    

            elif hand1[5] == "Eight":
                if "Eight" not in hand2:
                    print ("I do not have any Eights. Go fish!")
                    drawing_player = 1
                elif "Eight" in hand2:
                    if eightcount2 == 1:
                        print ("I have one Eight. Here!")
                        hand2.remove("Eight")
                        hand1.append("Eight")
                        sleep (2)
                    elif eightcount2 == 2:
                        print ("I have two Eights. Here!")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    elif eightcount2 == 3:
                        print ("I have three Eights. Here!")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    elif eightcount2 == 4:
                        print ("I have four Eights. Here...")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    

            elif hand1[5] == "Nine":
                if "Nine" not in hand2:
                    print ("I do not have any Nines. Go fish!")
                    drawing_player = 1
                elif "Nine" in hand2:
                    if ninecount2 == 1:
                        print ("I have one Nine. Here!")
                        hand2.remove("Nine")
                        hand1.append("Nine")
                        sleep (2)
                    elif ninecount2 == 2:
                        print ("I have two Nines. Here!")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    elif ninecount2 == 3:
                        print ("I have three Nines. Here!")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    elif ninecount2 == 4:
                        print ("I have four Nines. Here...")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    

            elif hand1[5] == "Ten":
                if "Ten" not in hand2:
                    print ("I do not have any Tens. Go fish!")
                    drawing_player = 1
                elif "Ten" in hand2:
                    if tencount2 == 1:
                        print ("I have one Ten. Here!")
                        hand2.remove("Ten")
                        hand1.append("Ten")
                        sleep (2)
                    elif tencount2 == 2:
                        print ("I have two Tens. Here!")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    elif tencount2 == 3:
                        print ("I have three Tens. Here!")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    elif tencount2 == 4:
                        print ("I have four Tens. Here...")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    

            elif hand1[5] == "Jack":
                if "Jack" not in hand2:
                    print ("I do not have any Jacks. Go fish!")
                    drawing_player = 1
                elif "Jack" in hand2:
                    if jackcount2 == 1:
                        print ("I have one Jack. Here!")
                        hand2.remove("Jack")
                        hand1.append("Jack")
                        sleep (2)
                    elif jackcount2 == 2:
                        print ("I have two Jacks. Here!")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    elif jackcount2 == 3:
                        print ("I have three Jacks. Here!")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    elif jackcount2 == 4:
                        print ("I have four Jacks. Here...")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    

            elif hand1[5] == "Queen":
                if "Queen" not in hand2:
                    print ("I do not have any Queens. Go fish!")
                    drawing_player = 1
                elif "Queen" in hand2:
                    if queencount2 == 1:
                        print ("I have one Queen. Here!")
                        hand2.remove("Queen")
                        hand1.append("Queen")
                        sleep (2)
                    elif queencount2 == 2:
                        print ("I have two Queens. Here!")
                        while "Two" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")
                    elif queencount2 == 3:
                        print ("I have three Queen. Here!")
                        while "Queen" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")
                    elif queencount2 == 4:
                        print ("I have four Queens. Here...")
                        while "Queen" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")

        elif askingses == 7:
            if hand1[6] == "Ace":
                if "Ace" not in hand2:
                    print ("I do not have any Aces. Go fish!")
                    drawing_player = 1
                elif "Ace" in hand2:
                    if acecount2 == 1:
                        print ("I have one Ace. Here!")
                        hand2.remove("Ace")
                        hand1.append("Ace")
                        sleep (2)
                    elif acecount2 == 2:
                        print ("I have two Aces. Here!")
                        while "Ace" in hand2:
                            hand2.remove("Ace")
                            hand1.append("Ace")
                    elif acecount2 == 3:
                        print ("I have three Aces. Here!")
                        while "Ace" in hand2:
                            hand2.remove("Ace")
                            hand1.append("Ace")
                    elif acecount2 == 4:
                        print ("I have four aces. Here...")
                        while "Ace" in hand2:
                            hand2.remove("Ace")
                            hand1.append("Ace")
                        
            elif hand1[6] == "King":
                if "King" not in hand2:
                    print ("I do not have any Kings. Go fish!")
                    drawing_player =1
                elif "King" in hand2:
                    if kingcount2 == 1: 
                        print ("I have one King. Here!")
                        hand2.remove("King")
                        hand1.append("King")
                        sleep (2)
                    elif kingcount2 == 2:
                        print ("I have two Kings. Here!")
                        while "King" in hand2:
                            hand2.remove("King")
                            hand1.append("King")
                    elif kingcount2 == 3:
                        print ("I have three Kings. Here!")
                        while "King" in hand2:
                            hand2.remove("King")
                            hand1.append("King")
                    elif kingcount2 == 4:
                        print ("I have four Kings. Here...")
                        while "King" in hand2:
                            hand2.remove("King")
                            hand1.append("King")
                        
            elif hand1[6] == "Two":
                if "Two" not in hand2:
                    print ("I do not have any Twos. Go fish!")
                    drawing_player = 1
                elif "Two" in hand2:
                    if twocount2 == 1:
                        print ("I have one Two. Here!")
                        hand2.remove("Two")
                        hand1.append("Two")
                        sleep (2)
                    elif twocount2 == 2:
                        print ("I have two Twos. Here!")
                        while "Two" in hand2:
                            hand2.remove("Two")
                            hand1.append("Two")
                    elif twocount2 == 3:
                        print ("I have three Twos. Here!")
                        while "Two" in hand2:
                            hand2.remove("Two")
                            hand1.append("Two")
                    elif twocount2 == 4:
                        print ("I have four Twos. Here...")
                        while "Two" in hand2:
                            hand2.remove("Two")
                            hand1.append("Two")
                        
            elif hand1[6] == "Three":
                if "Three" not in hand2:
                    print ("I do not have any Threes. Go fish!")
                    drawing_player = 1
                elif "Three" in hand2:
                    if threecount2 == 1:
                        print ("I have one Three. Here!")
                        hand2.remove("Three")
                        hand1.append("Three")
                        sleep (2)
                    elif threecount2 == 2:
                        print ("I have two Threes. Here!")
                        while "Three" in hand2:
                            hand2.remove("Three")
                            hand1.append("Three")
                    elif threecount2 == 3:
                        print ("I have three Threes. Here!")
                        while "Three" in hand2:
                            hand2.remove("Three")
                            hand1.append("Three")
                    elif threecount2 == 4:
                        print ("I have four Threes. Here...")
                        while "Three" in hand2:
                            hand2.remove("Three")
                            hand1.append("Three")

            elif hand1[6] == "Four":
                if "Four" not in hand2:
                    print ("I do not have any Fours. Go fish!")
                    drawing_player = 1
                elif "Four" in hand2:
                    if fourcount2 == 1:
                        print ("I have one Four. Here!")
                        hand2.remove("Four")
                        hand1.append("Four")
                        sleep (2)
                    elif fourcount2 == 2:
                        print ("I have two Fours. Here!")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    elif fourcount2 == 3:
                        print ("I have three Fours. Here!")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    elif fourcount2 == 4:
                        print ("I have four Fours. Here...")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    
                    
            elif hand1[6] == "Five":
                if "Five" not in hand2:
                    print ("I do not have any Fives. Go fish!")
                    drawing_player = 1
                elif "Five" in hand2:
                    if fivecount2 == 1:
                        print ("I have one Five. Here!")
                        hand2.remove("Five")
                        hand1.append("Five")
                        sleep (2)
                    elif fivecount2 == 2:
                        print ("I have two Fives. Here!")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    elif fivecount2 == 3:
                        print ("I have three Fives. Here!")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    elif fivecount2 == 4:
                        print ("I have four Fives. Here...")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    

            elif hand1[6] == "Six":
                if "Six" not in hand2:
                    print ("I do not have any Sixes. Go fish!")
                    drawing_player = 1
                elif "Six" in hand2:
                    if sixcount2 == 1:
                        print ("I have one Six. Here!")
                        hand2.remove("Six")
                        hand1.append("Six")
                        sleep (2)
                    elif sixcount2 == 2:
                        print ("I have two Sixes. Here!")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    elif sixcount2 == 3:
                        print ("I have three Sixes. Here!")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    elif sixcount2 == 4:
                        print ("I have four Sixes. Here...")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    

            elif hand1[6] == "Seven":
                if "Seven" not in hand2:
                    print ("I do not have any Sevens. Go fish!")
                    drawing_player = 1
                elif "Seven" in hand2:
                    if sevencount2 == 1:
                        print ("I have one Seven. Here!")
                        hand2.remove("Seven")
                        hand1.append("Seven")
                        sleep (2)
                    elif sevencount2 == 2:
                        print ("I have two Sevens. Here!")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    elif sevencount2 == 3:
                        print ("I have three Sevens. Here!")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    elif sevencount2 == 4:
                        print ("I have four Sevens. Here...")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    

            elif hand1[6] == "Eight":
                if "Eight" not in hand2:
                    print ("I do not have any Eights. Go fish!")
                    drawing_player = 1
                elif "Eight" in hand2:
                    if eightcount2 == 1:
                        print ("I have one Eight. Here!")
                        hand2.remove("Eight")
                        hand1.append("Eight")
                        sleep (2)
                    elif eightcount2 == 2:
                        print ("I have two Eights. Here!")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    elif eightcount2 == 3:
                        print ("I have three Eights. Here!")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    elif eightcount2 == 4:
                        print ("I have four Eights. Here...")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    

            elif hand1[6] == "Nine":
                if "Nine" not in hand2:
                    print ("I do not have any Nines. Go fish!")
                    drawing_player = 1
                elif "Nine" in hand2:
                    if ninecount2 == 1:
                        print ("I have one Nine. Here!")
                        hand2.remove("Nine")
                        hand1.append("Nine")
                        sleep (2)
                    elif ninecount2 == 2:
                        print ("I have two Nines. Here!")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    elif ninecount2 == 3:
                        print ("I have three Nines. Here!")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    elif ninecount2 == 4:
                        print ("I have four Nines. Here...")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    

            elif hand1[6] == "Ten":
                if "Ten" not in hand2:
                    print ("I do not have any Tens. Go fish!")
                    drawing_player = 1
                elif "Ten" in hand2:
                    if tencount2 == 1:
                        print ("I have one Ten. Here!")
                        hand2.remove("Ten")
                        hand1.append("Ten")
                        sleep (2)
                    elif tencount2 == 2:
                        print ("I have two Tens. Here!")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    elif tencount2 == 3:
                        print ("I have three Tens. Here!")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    elif tencount2 == 4:
                        print ("I have four Tens. Here...")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    

            elif hand1[6] == "Jack":
                if "Jack" not in hand2:
                    print ("I do not have any Jacks. Go fish!")
                    drawing_player = 1
                elif "Jack" in hand2:
                    if jackcount2 == 1:
                        print ("I have one Jack. Here!")
                        hand2.remove("Jack")
                        hand1.append("Jack")
                        sleep (2)
                    elif jackcount2 == 2:
                        print ("I have two Jacks. Here!")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    elif jackcount2 == 3:
                        print ("I have three Jacks. Here!")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    elif jackcount2 == 4:
                        print ("I have four Jacks. Here...")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    

            elif hand1[6] == "Queen":
                if "Queen" not in hand2:
                    print ("I do not have any Queens. Go fish!")
                    drawing_player = 1
                elif "Queen" in hand2:
                    if queencount2 == 1:
                        print ("I have one Queen. Here!")
                        hand2.remove("Queen")
                        hand1.append("Queen")
                        sleep (2)
                    elif queencount2 == 2:
                        print ("I have two Queens. Here!")
                        while "Two" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")
                    elif queencount2 == 3:
                        print ("I have three Queen. Here!")
                        while "Queen" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")
                    elif queencount2 == 4:
                        print ("I have four Queens. Here...")
                        while "Queen" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")

        elif askingses == 8:
            if hand1[7] == "Ace":
                if "Ace" not in hand2:
                    print ("I do not have any Aces. Go fish!")
                    drawing_player = 1
                elif "Ace" in hand2:
                    if acecount2 == 1:
                        print ("I have one Ace. Here!")
                        hand2.remove("Ace")
                        hand1.append("Ace")
                        sleep (2)
                    elif acecount2 == 2:
                        print ("I have two Aces. Here!")
                        while "Ace" in hand2:
                            hand2.remove("Ace")
                            hand1.append("Ace")
                    elif acecount2 == 3:
                        print ("I have three Aces. Here!")
                        while "Ace" in hand2:
                            hand2.remove("Ace")
                            hand1.append("Ace")
                    elif acecount2 == 4:
                        print ("I have four aces. Here...")
                        while "Ace" in hand2:
                            hand2.remove("Ace")
                            hand1.append("Ace")
                        
            elif hand1[7] == "King":
                if "King" not in hand2:
                    print ("I do not have any Kings. Go fish!")
                    drawing_player =1
                elif "King" in hand2:
                    if kingcount2 == 1: 
                        print ("I have one King. Here!")
                        hand2.remove("King")
                        hand1.append("King")
                        sleep (2)
                    elif kingcount2 == 2:
                        print ("I have two Kings. Here!")
                        while "King" in hand2:
                            hand2.remove("King")
                            hand1.append("King")
                    elif kingcount2 == 3:
                        print ("I have three Kings. Here!")
                        while "King" in hand2:
                            hand2.remove("King")
                            hand1.append("King")
                    elif kingcount2 == 4:
                        print ("I have four Kings. Here...")
                        while "King" in hand2:
                            hand2.remove("King")
                            hand1.append("King")
                        
            elif hand1[7] == "Two":
                if "Two" not in hand2:
                    print ("I do not have any Twos. Go fish!")
                    drawing_player = 1
                elif "Two" in hand2:
                    if twocount2 == 1:
                        print ("I have one Two. Here!")
                        hand2.remove("Two")
                        hand1.append("Two")
                        sleep (2)
                    elif twocount2 == 2:
                        print ("I have two Twos. Here!")
                        while "Two" in hand2:
                            hand2.remove("Two")
                            hand1.append("Two")
                    elif twocount2 == 3:
                        print ("I have three Twos. Here!")
                        while "Two" in hand2:
                            hand2.remove("Two")
                            hand1.append("Two")
                    elif twocount2 == 4:
                        print ("I have four Twos. Here...")
                        while "Two" in hand2:
                            hand2.remove("Two")
                            hand1.append("Two")
                        
            elif hand1[7] == "Three":
                if "Three" not in hand2:
                    print ("I do not have any Threes. Go fish!")
                    drawing_player = 1
                elif "Three" in hand2:
                    if threecount2 == 1:
                        print ("I have one Three. Here!")
                        hand2.remove("Three")
                        hand1.append("Three")
                        sleep (2)
                    elif threecount2 == 2:
                        print ("I have two Threes. Here!")
                        while "Three" in hand2:
                            hand2.remove("Three")
                            hand1.append("Three")
                    elif threecount2 == 3:
                        print ("I have three Threes. Here!")
                        while "Three" in hand2:
                            hand2.remove("Three")
                            hand1.append("Three")
                    elif threecount2 == 4:
                        print ("I have four Threes. Here...")
                        while "Three" in hand2:
                            hand2.remove("Three")
                            hand1.append("Three")

                elif hand1[7] == "Four":
                    if "Four" not in hand2:
                        print ("I do not have any Fours. Go fish!")
                        drawing_player = 1
                    elif "Four" in hand2:
                        if fourcount2 == 1:
                            print ("I have one Four. Here!")
                            hand2.remove("Four")
                            hand1.append("Four")
                            sleep (2)
                        elif fourcount2 == 2:
                            print ("I have two Fours. Here!")
                            while "Four" in hand2:
                                hand2.remove("Four")
                                hand1.append("Four")
                        elif fourcount2 == 3:
                            print ("I have three Fours. Here!")
                            while "Four" in hand2:
                                hand2.remove("Four")
                                hand1.append("Four")
                        elif fourcount2 == 4:
                            print ("I have four Fours. Here...")
                            while "Four" in hand2:
                                hand2.remove("Four")
                                hand1.append("Four")
                    
                    
                elif hand1[7] == "Five":
                    if "Five" not in hand2:
                        print ("I do not have any Fives. Go fish!")
                        drawing_player = 1
                    elif "Five" in hand2:
                        if fivecount2 == 1:
                            print ("I have one Five. Here!")
                            hand2.remove("Five")
                            hand1.append("Five")
                            sleep (2)
                        elif fivecount2 == 2:
                            print ("I have two Fives. Here!")
                            while "Five" in hand2:
                                hand2.remove("Five")
                                hand1.append("Five")
                        elif fivecount2 == 3:
                            print ("I have three Fives. Here!")
                            while "Five" in hand2:
                                hand2.remove("Five")
                                hand1.append("Five")
                        elif fivecount2 == 4:
                            print ("I have four Fives. Here...")
                            while "Five" in hand2:
                                hand2.remove("Five")
                                hand1.append("Five")
                    

                elif hand1[7] == "Six":
                    if "Six" not in hand2:
                        print ("I do not have any Sixes. Go fish!")
                        drawing_player = 1
                    elif "Six" in hand2:
                        if sixcount2 == 1:
                            print ("I have one Six. Here!")
                            hand2.remove("Six")
                            hand1.append("Six")
                            sleep (2)
                        elif sixcount2 == 2:
                            print ("I have two Sixes. Here!")
                            while "Six" in hand2:
                                hand2.remove("Six")
                                hand1.append("Six")
                        elif sixcount2 == 3:
                            print ("I have three Sixes. Here!")
                            while "Six" in hand2:
                                hand2.remove("Six")
                                hand1.append("Six")
                        elif sixcount2 == 4:
                            print ("I have four Sixes. Here...")
                            while "Six" in hand2:
                                hand2.remove("Six")
                                hand1.append("Six")
                    

                elif hand1[7] == "Seven":
                    if "Seven" not in hand2:
                        print ("I do not have any Sevens. Go fish!")
                        drawing_player = 1
                    elif "Seven" in hand2:
                        if sevencount2 == 1:
                            print ("I have one Seven. Here!")
                            hand2.remove("Seven")
                            hand1.append("Seven")
                            sleep (2)
                        elif sevencount2 == 2:
                            print ("I have two Sevens. Here!")
                            while "Seven" in hand2:
                                hand2.remove("Seven")
                                hand1.append("Seven")
                        elif sevencount2 == 3:
                            print ("I have three Sevens. Here!")
                            while "Seven" in hand2:
                                hand2.remove("Seven")
                                hand1.append("Seven")
                        elif sevencount2 == 4:
                            print ("I have four Sevens. Here...")
                            while "Seven" in hand2:
                                hand2.remove("Seven")
                                hand1.append("Seven")
                    

                elif hand1[7] == "Eight":
                    if "Eight" not in hand2:
                        print ("I do not have any Eights. Go fish!")
                        drawing_player = 1
                    elif "Eight" in hand2:
                        if eightcount2 == 1:
                            print ("I have one Eight. Here!")
                            hand2.remove("Eight")
                            hand1.append("Eight")
                            sleep (2)
                        elif eightcount2 == 2:
                            print ("I have two Eights. Here!")
                            while "Eight" in hand2:
                                hand2.remove("Eight")
                                hand1.append("Eight")
                        elif eightcount2 == 3:
                            print ("I have three Eights. Here!")
                            while "Eight" in hand2:
                                hand2.remove("Eight")
                                hand1.append("Eight")
                        elif eightcount2 == 4:
                            print ("I have four Eights. Here...")
                            while "Eight" in hand2:
                                hand2.remove("Eight")
                                hand1.append("Eight")
                    

                elif hand1[7] == "Nine":
                    if "Nine" not in hand2:
                        print ("I do not have any Nines. Go fish!")
                        drawing_player = 1
                    elif "Nine" in hand2:
                        if ninecount2 == 1:
                            print ("I have one Nine. Here!")
                            hand2.remove("Nine")
                            hand1.append("Nine")
                            sleep (2)
                        elif ninecount2 == 2:
                            print ("I have two Nines. Here!")
                            while "Nine" in hand2:
                                hand2.remove("Nine")
                                hand1.append("Nine")
                        elif ninecount2 == 3:
                            print ("I have three Nines. Here!")
                            while "Nine" in hand2:
                                hand2.remove("Nine")
                                hand1.append("Nine")
                        elif ninecount2 == 4:
                            print ("I have four Nines. Here...")
                            while "Nine" in hand2:
                                hand2.remove("Nine")
                                hand1.append("Nine")
                    

                elif hand1[7] == "Ten":
                    if "Ten" not in hand2:
                        print ("I do not have any Tens. Go fish!")
                        drawing_player = 1
                    elif "Ten" in hand2:
                        if tencount2 == 1:
                            print ("I have one Ten. Here!")
                            hand2.remove("Ten")
                            hand1.append("Ten")
                            sleep (2)
                        elif tencount2 == 2:
                            print ("I have two Tens. Here!")
                            while "Ten" in hand2:
                                hand2.remove("Ten")
                                hand1.append("Ten")
                        elif tencount2 == 3:
                            print ("I have three Tens. Here!")
                            while "Ten" in hand2:
                                hand2.remove("Ten")
                                hand1.append("Ten")
                        elif tencount2 == 4:
                            print ("I have four Tens. Here...")
                            while "Ten" in hand2:
                                hand2.remove("Ten")
                                hand1.append("Ten")
                    

                elif hand1[7] == "Jack":
                    if "Jack" not in hand2:
                        print ("I do not have any Jacks. Go fish!")
                        drawing_player = 1
                    elif "Jack" in hand2:
                        if jackcount2 == 1:
                            print ("I have one Jack. Here!")
                            hand2.remove("Jack")
                            hand1.append("Jack")
                            sleep (2)
                        elif jackcount2 == 2:
                            print ("I have two Jacks. Here!")
                            while "Jack" in hand2:
                                hand2.remove("Jack")
                                hand1.append("Jack")
                        elif jackcount2 == 3:
                            print ("I have three Jacks. Here!")
                            while "Jack" in hand2:
                                hand2.remove("Jack")
                                hand1.append("Jack")
                        elif jackcount2 == 4:
                            print ("I have four Jacks. Here...")
                            while "Jack" in hand2:
                                hand2.remove("Jack")
                                hand1.append("Jack")
                    

                elif hand1[7] == "Queen":
                    if "Queen" not in hand2:
                        print ("I do not have any Queens. Go fish!")
                        drawing_player = 1
                    elif "Queen" in hand2:
                        if queencount2 == 1:
                            print ("I have one Queen. Here!")
                            hand2.remove("Queen")
                            hand1.append("Queen")
                            sleep (2)
                        elif queencount2 == 2:
                            print ("I have two Queens. Here!")
                            while "Two" in hand2:
                                hand2.remove("Queen")
                                hand1.append("Queen")
                        elif queencount2 == 3:
                            print ("I have three Queen. Here!")
                            while "Queen" in hand2:
                                hand2.remove("Queen")
                                hand1.append("Queen")
                        elif queencount2 == 4:
                            print ("I have four Queens. Here...")
                            while "Queen" in hand2:
                                hand2.remove("Queen")
                                hand1.append("Queen")

        elif askingses == 9:
            if hand1[8] == "Ace":
                if "Ace" not in hand2:
                    print ("I do not have any Aces. Go fish!")
                    drawing_player = 1
                elif "Ace" in hand2:
                    if acecount2 == 1:
                        print ("I have one Ace. Here!")
                        hand2.remove("Ace")
                        hand1.append("Ace")
                        sleep (2)
                    elif acecount2 == 2:
                        print ("I have two Aces. Here!")
                        while "Ace" in hand2:
                            hand2.remove("Ace")
                            hand1.append("Ace")
                    elif acecount2 == 3:
                        print ("I have three Aces. Here!")
                        while "Ace" in hand2:
                            hand2.remove("Ace")
                            hand1.append("Ace")
                    elif acecount2 == 4:
                        print ("I have four aces. Here...")
                        while "Ace" in hand2:
                            hand2.remove("Ace")
                            hand1.append("Ace")
                        
            elif hand1[8] == "King":
                if "King" not in hand2:
                    print ("I do not have any Kings. Go fish!")
                    drawing_player =1
            elif "King" in hand2:
                if kingcount2 == 1: 
                    print ("I have one King. Here!")
                    hand2.remove("King")
                    hand1.append("King")
                    sleep (2)
                elif kingcount2 == 2:
                    print ("I have two Kings. Here!")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                elif kingcount2 == 3:
                    print ("I have three Kings. Here!")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                elif kingcount2 == 4:
                    print ("I have four Kings. Here...")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                        
        elif hand1[8] == "Two":
            if "Two" not in hand2:
                print ("I do not have any Twos. Go fish!")
                drawing_player = 1
            elif "Two" in hand2:
                if twocount2 == 1:
                    print ("I have one Two. Here!")
                    hand2.remove("Two")
                    hand1.append("Two")
                    sleep (2)
                elif twocount2 == 2:
                    print ("I have two Twos. Here!")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                elif twocount2 == 3:
                    print ("I have three Twos. Here!")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                elif twocount2 == 4:
                    print ("I have four Twos. Here...")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                        
        elif hand1[8] == "Three":
            if "Three" not in hand2:
                print ("I do not have any Threes. Go fish!")
                drawing_player = 1
            elif "Three" in hand2:
                if threecount2 == 1:
                    print ("I have one Three. Here!")
                    hand2.remove("Three")
                    hand1.append("Three")
                    sleep (2)
                elif threecount2 == 2:
                    print ("I have two Threes. Here!")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")
                elif threecount2 == 3:
                    print ("I have three Threes. Here!")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")
                elif threecount2 == 4:
                    print ("I have four Threes. Here...")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")

            elif hand1[8] == "Four":
                if "Four" not in hand2:
                    print ("I do not have any Fours. Go fish!")
                    drawing_player = 1
                elif "Four" in hand2:
                    if fourcount2 == 1:
                        print ("I have one Four. Here!")
                        hand2.remove("Four")
                        hand1.append("Four")
                        sleep (2)
                    elif fourcount2 == 2:
                        print ("I have two Fours. Here!")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    elif fourcount2 == 3:
                        print ("I have three Fours. Here!")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    elif fourcount2 == 4:
                        print ("I have four Fours. Here...")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    
                    
            elif hand1[8] == "Five":
                if "Five" not in hand2:
                    print ("I do not have any Fives. Go fish!")
                    drawing_player = 1
                elif "Five" in hand2:
                    if fivecount2 == 1:
                        print ("I have one Five. Here!")
                        hand2.remove("Five")
                        hand1.append("Five")
                        sleep (2)
                    elif fivecount2 == 2:
                        print ("I have two Fives. Here!")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    elif fivecount2 == 3:
                        print ("I have three Fives. Here!")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    elif fivecount2 == 4:
                        print ("I have four Fives. Here...")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    

            elif hand1[8] == "Six":
                if "Six" not in hand2:
                    print ("I do not have any Sixes. Go fish!")
                    drawing_player = 1
                elif "Six" in hand2:
                    if sixcount2 == 1:
                        print ("I have one Six. Here!")
                        hand2.remove("Six")
                        hand1.append("Six")
                        sleep (2)
                    elif sixcount2 == 2:
                        print ("I have two Sixes. Here!")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    elif sixcount2 == 3:
                        print ("I have three Sixes. Here!")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    elif sixcount2 == 4:
                        print ("I have four Sixes. Here...")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    

            elif hand1[8] == "Seven":
                if "Seven" not in hand2:
                    print ("I do not have any Sevens. Go fish!")
                    drawing_player = 1
                elif "Seven" in hand2:
                    if sevencount2 == 1:
                        print ("I have one Seven. Here!")
                        hand2.remove("Seven")
                        hand1.append("Seven")
                        sleep (2)
                    elif sevencount2 == 2:
                        print ("I have two Sevens. Here!")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    elif sevencount2 == 3:
                        print ("I have three Sevens. Here!")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    elif sevencount2 == 4:
                        print ("I have four Sevens. Here...")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    

            elif hand1[8] == "Eight":
                if "Eight" not in hand2:
                    print ("I do not have any Eights. Go fish!")
                    drawing_player = 1
                elif "Eight" in hand2:
                    if eightcount2 == 1:
                        print ("I have one Eight. Here!")
                        hand2.remove("Eight")
                        hand1.append("Eight")
                        sleep (2)
                    elif eightcount2 == 2:
                        print ("I have two Eights. Here!")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    elif eightcount2 == 3:
                        print ("I have three Eights. Here!")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    elif eightcount2 == 4:
                        print ("I have four Eights. Here...")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    

            elif hand1[8] == "Nine":
                if "Nine" not in hand2:
                    print ("I do not have any Nines. Go fish!")
                    drawing_player = 1
                elif "Nine" in hand2:
                    if ninecount2 == 1:
                        print ("I have one Nine. Here!")
                        hand2.remove("Nine")
                        hand1.append("Nine")
                        sleep (2)
                    elif ninecount2 == 2:
                        print ("I have two Nines. Here!")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    elif ninecount2 == 3:
                        print ("I have three Nines. Here!")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    elif ninecount2 == 4:
                        print ("I have four Nines. Here...")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    

            elif hand1[8] == "Ten":
                if "Ten" not in hand2:
                    print ("I do not have any Tens. Go fish!")
                    drawing_player = 1
                elif "Ten" in hand2:
                    if tencount2 == 1:
                        print ("I have one Ten. Here!")
                        hand2.remove("Ten")
                        hand1.append("Ten")
                        sleep (2)
                    elif tencount2 == 2:
                        print ("I have two Tens. Here!")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    elif tencount2 == 3:
                        print ("I have three Tens. Here!")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    elif tencount2 == 4:
                        print ("I have four Tens. Here...")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    

            elif hand1[8] == "Jack":
                if "Jack" not in hand2:
                    print ("I do not have any Jacks. Go fish!")
                    drawing_player = 1
                elif "Jack" in hand2:
                    if jackcount2 == 1:
                        print ("I have one Jack. Here!")
                        hand2.remove("Jack")
                        hand1.append("Jack")
                        sleep (2)
                    elif jackcount2 == 2:
                        print ("I have two Jacks. Here!")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    elif jackcount2 == 3:
                        print ("I have three Jacks. Here!")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    elif jackcount2 == 4:
                        print ("I have four Jacks. Here...")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    

            elif hand1[8] == "Queen":
                if "Queen" not in hand2:
                    print ("I do not have any Queens. Go fish!")
                    drawing_player = 1
                elif "Queen" in hand2:
                    if queencount2 == 1:
                        print ("I have one Queen. Here!")
                        hand2.remove("Queen")
                        hand1.append("Queen")
                        sleep (2)
                    elif queencount2 == 2:
                        print ("I have two Queens. Here!")
                        while "Two" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")
                    elif queencount2 == 3:
                        print ("I have three Queen. Here!")
                        while "Queen" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")
                    elif queencount2 == 4:
                        print ("I have four Queens. Here...")
                        while "Queen" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")

        elif askingses == 10:
            if hand1[9] == "Ace":
                if "Ace" not in hand2:
                    print ("I do not have any Aces. Go fish!")
                    drawing_player = 1
                elif "Ace" in hand2:
                    if acecount2 == 1:
                        print ("I have one Ace. Here!")
                        hand2.remove("Ace")
                        hand1.append("Ace")
                        sleep (2)
                elif acecount2 == 2:
                    print ("I have two Aces. Here!")
                    while "Ace" in hand2:
                        hand2.remove("Ace")
                        hand1.append("Ace")
                elif acecount2 == 3:
                    print ("I have three Aces. Here!")
                    while "Ace" in hand2:
                        hand2.remove("Ace")
                        hand1.append("Ace")
                elif acecount2 == 4:
                    print ("I have four aces. Here...")
                    while "Ace" in hand2:
                        hand2.remove("Ace")
                        hand1.append("Ace")
                        
        elif hand1[9] == "King":
            if "King" not in hand2:
                print ("I do not have any Kings. Go fish!")
                drawing_player =1
            elif "King" in hand2:
                if kingcount2 == 1: 
                    print ("I have one King. Here!")
                    hand2.remove("King")
                    hand1.append("King")
                    sleep (2)
                elif kingcount2 == 2:
                    print ("I have two Kings. Here!")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                elif kingcount2 == 3:
                    print ("I have three Kings. Here!")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                elif kingcount2 == 4:
                    print ("I have four Kings. Here...")
                    while "King" in hand2:
                        hand2.remove("King")
                        hand1.append("King")
                        
        elif hand1[9] == "Two":
            if "Two" not in hand2:
                print ("I do not have any Twos. Go fish!")
                drawing_player = 1
            elif "Two" in hand2:
                if twocount2 == 1:
                    print ("I have one Two. Here!")
                    hand2.remove("Two")
                    hand1.append("Two")
                    sleep (2)
                elif twocount2 == 2:
                    print ("I have two Twos. Here!")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                elif twocount2 == 3:
                    print ("I have three Twos. Here!")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                elif twocount2 == 4:
                    print ("I have four Twos. Here...")
                    while "Two" in hand2:
                        hand2.remove("Two")
                        hand1.append("Two")
                        
        elif hand1[9] == "Three":
            if "Three" not in hand2:
                print ("I do not have any Threes. Go fish!")
                drawing_player = 1
            elif "Three" in hand2:
                if threecount2 == 1:
                    print ("I have one Three. Here!")
                    hand2.remove("Three")
                    hand1.append("Three")
                    sleep (2)
                elif threecount2 == 2:
                    print ("I have two Threes. Here!")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")
                elif threecount2 == 3:
                    print ("I have three Threes. Here!")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")
                elif threecount2 == 4:
                    print ("I have four Threes. Here...")
                    while "Three" in hand2:
                        hand2.remove("Three")
                        hand1.append("Three")

            elif hand1[9] == "Four":
                if "Four" not in hand2:
                    print ("I do not have any Fours. Go fish!")
                    drawing_player = 1
                elif "Four" in hand2:
                    if fourcount2 == 1:
                        print ("I have one Four. Here!")
                        hand2.remove("Four")
                        hand1.append("Four")
                        sleep (2)
                    elif fourcount2 == 2:
                        print ("I have two Fours. Here!")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    elif fourcount2 == 3:
                        print ("I have three Fours. Here!")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    elif fourcount2 == 4:
                        print ("I have four Fours. Here...")
                        while "Four" in hand2:
                            hand2.remove("Four")
                            hand1.append("Four")
                    
                    
            elif hand1[9] == "Five":
                if "Five" not in hand2:
                    print ("I do not have any Fives. Go fish!")
                    drawing_player = 1
                elif "Five" in hand2:
                    if fivecount2 == 1:
                        print ("I have one Five. Here!")
                        hand2.remove("Five")
                        hand1.append("Five")
                        sleep (2)
                    elif fivecount2 == 2:
                        print ("I have two Fives. Here!")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    elif fivecount2 == 3:
                        print ("I have three Fives. Here!")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    elif fivecount2 == 4:
                        print ("I have four Fives. Here...")
                        while "Five" in hand2:
                            hand2.remove("Five")
                            hand1.append("Five")
                    

            elif hand1[9] == "Six":
                if "Six" not in hand2:
                    print ("I do not have any Sixes. Go fish!")
                    drawing_player = 1
                elif "Six" in hand2:
                    if sixcount2 == 1:
                        print ("I have one Six. Here!")
                        hand2.remove("Six")
                        hand1.append("Six")
                        sleep (2)
                    elif sixcount2 == 2:
                        print ("I have two Sixes. Here!")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    elif sixcount2 == 3:
                        print ("I have three Sixes. Here!")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    elif sixcount2 == 4:
                        print ("I have four Sixes. Here...")
                        while "Six" in hand2:
                            hand2.remove("Six")
                            hand1.append("Six")
                    

            elif hand1[9] == "Seven":
                if "Seven" not in hand2:
                    print ("I do not have any Sevens. Go fish!")
                    drawing_player = 1
                elif "Seven" in hand2:
                    if sevencount2 == 1:
                        print ("I have one Seven. Here!")
                        hand2.remove("Seven")
                        hand1.append("Seven")
                        sleep (2)
                    elif sevencount2 == 2:
                        print ("I have two Sevens. Here!")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    elif sevencount2 == 3:
                        print ("I have three Sevens. Here!")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    elif sevencount2 == 4:
                        print ("I have four Sevens. Here...")
                        while "Seven" in hand2:
                            hand2.remove("Seven")
                            hand1.append("Seven")
                    

            elif hand1[9] == "Eight":
                if "Eight" not in hand2:
                    print ("I do not have any Eights. Go fish!")
                    drawing_player = 1
                elif "Eight" in hand2:
                    if eightcount2 == 1:
                        print ("I have one Eight. Here!")
                        hand2.remove("Eight")
                        hand1.append("Eight")
                        sleep (2)
                    elif eightcount2 == 2:
                        print ("I have two Eights. Here!")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    elif eightcount2 == 3:
                        print ("I have three Eights. Here!")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    elif eightcount2 == 4:
                        print ("I have four Eights. Here...")
                        while "Eight" in hand2:
                            hand2.remove("Eight")
                            hand1.append("Eight")
                    

            elif hand1[9] == "Nine":
                if "Nine" not in hand2:
                    print ("I do not have any Nines. Go fish!")
                    drawing_player = 1
                elif "Nine" in hand2:
                    if ninecount2 == 1:
                        print ("I have one Nine. Here!")
                        hand2.remove("Nine")
                        hand1.append("Nine")
                        sleep (2)
                    elif ninecount2 == 2:
                        print ("I have two Nines. Here!")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    elif ninecount2 == 3:
                        print ("I have three Nines. Here!")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    elif ninecount2 == 4:
                        print ("I have four Nines. Here...")
                        while "Nine" in hand2:
                            hand2.remove("Nine")
                            hand1.append("Nine")
                    

            elif hand1[9] == "Ten":
                if "Ten" not in hand2:
                    print ("I do not have any Tens. Go fish!")
                    drawing_player = 1
                elif "Ten" in hand2:
                    if tencount2 == 1:
                        print ("I have one Ten. Here!")
                        hand2.remove("Ten")
                        hand1.append("Ten")
                        sleep (2)
                    elif tencount2 == 2:
                        print ("I have two Tens. Here!")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    elif tencount2 == 3:
                        print ("I have three Tens. Here!")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    elif tencount2 == 4:
                        print ("I have four Tens. Here...")
                        while "Ten" in hand2:
                            hand2.remove("Ten")
                            hand1.append("Ten")
                    

            elif hand1[9] == "Jack":
                if "Jack" not in hand2:
                    print ("I do not have any Jacks. Go fish!")
                    drawing_player = 1
                elif "Jack" in hand2:
                    if jackcount2 == 1:
                        print ("I have one Jack. Here!")
                        hand2.remove("Jack")
                        hand1.append("Jack")
                        sleep (2)
                    elif jackcount2 == 2:
                        print ("I have two Jacks. Here!")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    elif jackcount2 == 3:
                        print ("I have three Jacks. Here!")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    elif jackcount2 == 4:
                        print ("I have four Jacks. Here...")
                        while "Jack" in hand2:
                            hand2.remove("Jack")
                            hand1.append("Jack")
                    

            elif hand1[9] == "Queen":
                if "Queen" not in hand2:
                    print ("I do not have any Queens. Go fish!")
                    drawing_player = 1
                elif "Queen" in hand2:
                    if queencount2 == 1:
                        print ("I have one Queen. Here!")
                        hand2.remove("Queen")
                        hand1.append("Queen")
                        sleep (2)
                    elif queencount2 == 2:
                        print ("I have two Queens. Here!")
                        while "Two" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")
                    elif queencount2 == 3:
                        print ("I have three Queen. Here!")
                        while "Queen" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")
                    elif queencount2 == 4:
                        print ("I have four Queens. Here...")
                        while "Queen" in hand2:
                            hand2.remove("Queen")
                            hand1.append("Queen")

                            
def who_goes_first2():
    goes_first = min(value[hand1[0]], value[hand2[0]], value[hand3[0]], value[hand4[0]])    
    if value[hand1[0]] == goes_first:
            first_player = 1
    elif value[hand2[0]] == goes_first: 
            first_player = 2
    elif value[hand3[0]] == goes_first: 
            first_player = 3
    elif value[hand4[0]] == goes_first: 
            first_player = 4
    else:
             print ("I guess something happened. Please restart the program.")
		    
    first_player = 1 # Remove this after. 
    
    if first_player == 1:
        current_player = 1
        print ("Since you had the lowest card earlier, you get to go first.")
        first_move = int(input("Who do you want to ask for your card? Please type 2 for Player #2, 3 for Player #3, or 4 for Player #4.\n"))
        if first_move == 2:
                print (hand2)
                search_for_card_in_hand2_for_player_1()
        elif first_move == 3:
                print("Okay, which card do you want to ask Player 3 for?\n")   
        elif first_move == 4:
                print("Okay, which card do you want to ask Player 4 for?\n")
        else:
                print ("Go read the rules again, and then come try again. You clearly don't know how to play Go Fish!")                        
    elif first_player == 2:
                print ("Computer Player #2, what would you like to do?")   
                playerdeck()
    elif first_player == 3:
                print ("Computer Player #3, what would you like to do?")
                playerdeck2()
    elif first_player == 4:
                print ("Computer Player #4, what would you like to do?")
                playerdeck3()
    elif first_player == 0:
                print ("First_player is still 0. Something occured.")
    else:
                print ("No clue what happened, but please restart the program.")                             
                        

def random_card2():
    rcard2 = [(hand2[0]), (hand2[1]), (hand2[2]), (hand2[3]), (hand2[4])]
    shuffle(rcard2)
    p2what_card = rcard2[1]
    
    
# Okay, now let's deal out all the cards.
def deal_cards_out():
    cards_dealt = 0
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
    print ("Okay, your cards include: A" , (hand1[0]), ","  ,(hand1[1]),  ","  ,(hand1[2]),  "," ,(hand1[3]),  "and a" ,(hand1[4]), "!"  )

def playerdeck():
    pchooser = ["1", "3", "4"]
    shuffle(pchooser)
    result2 = pchooser[0]
    if pchooser[0] == "1":
        print ("Player #2 has chosen to ask Player #1 for a card.\n")
        random_card2()
        print ( user, ", do you have" (p2what_card) )
    elif pchooser[0] == "3":
        print ("Player #2 has chosen to ask Player #3 for a card.\n")
    elif pchooser[0] == "4":
        print ("Player #2 has chosen to ask Player #4 for a card.\n")
    else:
        print ("The player chooser messed up.\n")

def playerdeck2():
    pchooser = ["1", "2", "4"]
    shuffle(pchooser)
    result2 = pchooser[0]
    if pchooser[0] == "1":
        print ("Player #3 has chosen to ask Player #1 for a card.\n")
    elif pchooser[0] == "2":
        print ("Player #3 has chosen to ask Player #2 for a card.\n")
    elif pchooser[0] == "4":
        print ("Player #3 has chosen to ask Player #4 for a card.\n")
    else:
        print ("The player chooser messed up.\n")

def playerdeck3():
    pchooser = ["1", "3", "4"]
    shuffle(pchooser)
    result2 = pchooser[0]
    if pchooser[0] == "1":
        print ("Player #4 has chosen to ask Player #1 for a card.\n")
    elif pchooser[0] == "2":
        print ("Player #4 has chosen to ask Player #2 for a card.\n")
    elif pchooser[0] == "3":
        print ("Player #4 has chosen to ask Player #3 for a card.\n")
    else:
        print ("The player chooser messed up.\n")
    
   
def go_fish():
        rules()
        who_goes_first()
        reset_game()
        deal_cards_out()
        who_goes_first2()

go_fish()
print (hand1)
print (hand2)
