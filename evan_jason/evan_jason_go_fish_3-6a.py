# Go Fish Project - ICT-3 Project Created by Evan and an Invisible Jason
# Version 3.6a
# Published 1/21/2017


deck = ["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
value = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14}
full_deck = deck * 4
hand0 = []
looker = hand0
first_player = 0

# Now we shuffle the deck, randomness and sleep!

from time import sleep
from random import shuffle
shuffle(full_deck)

# Now let's introduce the program!

print("Welcome to Go Fish Version 3.6a! This program simulates the game Go Fish in a computer model!")
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

    
# Now we set up the hand variables globally!

hand1 = []
hand2 = []
hand3 = []
hand4 = []

# Now we determine who goes first!

def who_goes_first():
        print ("Now we must determine who goes first.")
        print ()
        sleep(2)
        hand1.append((full_deck[0]))
        full_deck.remove(full_deck[0])
        hand2.append((full_deck[0]))
        full_deck.remove(full_deck[0])
        hand3.append((full_deck[0]))
        full_deck.remove(full_deck[0])
        hand4.append((full_deck[0]))
        full_deck.remove(full_deck[0])
        
        print ("Here is your card,", user,":" , (hand1[0]))
        print ()
        sleep(2)
        print ("Here are your opponents' beginning cards!")
        sleep(2)
        print ("Player #2:" , (hand2[0]))
        sleep(1)
        print ("Player #3:" , (hand3[0]))
        sleep(1)
        print ("Player #4:" , (hand4[0]))
        sleep (3)
        print ()
        
        goes_first = min(value[hand1[0]], value[hand2[0]], value[hand3[0]], value[hand4[0]])    
        if value[hand1[0]] == goes_first:
            print (user,"goes first because they have the lowest card.")
            print ()
            first_player = 1
        elif value[hand2[0]] == goes_first:
            print ("Player #2 goes first because they have the lowest card!.")
            print ()
            first_player = 2 
        elif value[hand3[0]] == goes_first:
            print ("Player #3 goes first because they have the lowest card!")
            print ()
            first_player = 3
        elif value[hand4[0]] == goes_first:
            print ("Player #4 goes first because they have the lowest card!")
            print ()
            first_player = 4
        else:
             print ("I guess something happened. Please restart the program.")
    

def reset_game():
    sleep(1)
    full_deck.append(hand1[0])
    full_deck.append(hand2[0])
    full_deck.append(hand3[0])
    full_deck.append(hand4[0])
    shuffle(full_deck)
    print ("Shuffling...")
    sleep(6)
    print ("Shuffling is now complete. The game is ready to begin.\n")                        
           
    
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

    
def go_fish():


    def turns():
        if drawfromdeck == asked_card:
            print("He/she got what they wanted!")
            sleep(2)
            print("Now, they get to go again!")
            
        elif drawfromdeck != asked_card:
             print ("Player",first_move ,", it is now your turn!")
        
        
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

    books1 = 0
    books2 = 0
    books3 = 0
    books4 = 0
    total_books = 13

    
    def drawit():
        drawfromdeck = full_deck[0]
        if first_player == 1:
            print ("Let's see what you draw from the deck!")
            sleep(1)
            print ("Choosing card....")
            sleep(3)
            print ("You got a/an", drawfromdeck, "from the deck!")
            hand1.append(drawfromdeck)
            full_deck.remove(full_deck[0])

            
        elif first_player == 2:
            print ("Let's see what Player #2 draws from the deck!")
            sleep(1)
            print ("Choosing card....")
            sleep(3)
            print ("Player #2 got a/an", drawfromdeck, "from the deck!")
            hand2.append(drawfromdeck)
            full_deck.remove(full_deck[0])

            
        elif first_player == 3:
            print ("Let's see what Player #3 draws from the deck!")
            sleep(1)
            print ("Choosing card....")
            sleep(3)
            print ("Player #3 got a/an", drawfromdeck, "from the deck!")
            hand3.append(drawfromdeck)
            full_deck.remove(full_deck[0])

        elif first_player == 4:
            print ("Let's see what Player #4 draws from the deck!")
            sleep(1)
            print ("Choosing card....")
            sleep(3)
            print ("Player #4 got a/an", drawfromdeck, "from the deck!")
            hand4.append(drawfromdeck)
            full_deck.remove(full_deck[0])
            
    
    def playerdeck():
        pchooser = ["1", "2", "3", "4"]
        if first_player == 2:
            shuffle(hand2)
            random_pick = hand2[0]

        elif first_player == 3:
            shuffle(hand3)
            random_pick = hand3[0]

        elif first_player == 4:
            shuffle(hand4)
            random_pick = hand4[0]


        def random_player():
            shuffle(pchooser)

            if first_player == 2:
                pchooser.remove("2")
                if pchooser[0] == "1":
                    print ("Player #2 has chosen to ask" , user, "for a/an",random_pick ,"!\n")
                    looker = hand1
            
                elif pchooser[0] == "3":
                    print ("Player #2 has chosen to ask Player #3 for a/an",random_pick ,"!\n")
                    looker = hand3
        
                elif pchooser[0] == "4":
                    print ("Player #2 has chosen to ask Player #4 for a/an",random_pick ,"!\n")
                    looker = hand4

            elif first_player == 3:
                pchooser.remove("3")
                if pchooser[0] == "1":
                    print ("Player #3 has chosen to ask" , user, "for a/an",random_pick ,"!\n")
                    looker = hand1
            
                elif pchooser[0] == "2":
                    print ("Player #3 has chosen to ask Player #2 for a/an",random_pick ,"!\n")
                    looker = hand2
        
                elif pchooser[0] == "4":
                    print ("Player #3 has chosen to ask Player #4 for a/an",random_pick ,"!\n")
                    looker = hand4

            elif first_player == 4:
                pchooser.remove("4")
                if pchooser[0] == "1":
                    print ("Player #4 has chosen to ask" , user, "for a/an",random_pick ,"!\n")
                    looker = hand1
            
                elif pchooser[0] == "2":
                    print ("Player #4 has chosen to ask Player #2 for a/an",random_pick ,"!\n")
                    looker = hand2
        
                elif pchooser[0] == "3":
                    print ("Player #4 has chosen to ask Player #3 for a/an",random_pick ,"!\n")
                    looker = hand3
            


        random_player()	

    while books1 + books2 + books3 + books4 < 13:
        print("Currently,",total_books,"total books are still remaining.\n")
        print(user,"currently has",books1,"books scored.\n")
        print("Player #2 currently has",books2,"books scored.")
        print("Player #3 currently has",books3,"books scored.")
        print("Player #4 currently has",books4,"books scored.\n")
        sleep(3)
        
        first_player = 1 # Remove this after testing.
        
        if first_player == 1:
            print ((user), ", it is now your turn.")
            print ("Okay, your cards include:", (hand1))
            
            asked_card = input("Which card do you want?\n")
            
            if asked_card not in hand1:
                asked_card = input("You do not have that card. Please type your card again.\n")
                sleep(1)
                
            else:
                print ("You asked for a/an:", asked_card,".\n")
                sleep(1)

            first_move = int(input("Who do you want to ask for your card? Please type 2 for Player #2, 3 for Player #3, or 4 for Player #4.\n"))


            
            if first_move == 2:
                print (hand2) # Remove this later for final code.
                if asked_card in hand2:
                    howmany2 = hand2.count(asked_card)
                    if howmany2 == 1:
                        print ("I have one,", asked_card,"!\n")
                        hand1.append(asked_card)
                        hand2.remove(asked_card)
                    elif howmany2 == 2:
                        print ("I have two,", asked_card,"'s !\n")
                        hand1.append(asked_card)
                        hand2.remove(asked_card)
                        hand1.append(asked_card)
                        hand2.remove(asked_card)
                    elif howmany2 == 3:
                        print ("I have three,", asked_card,"'s !\n")
                        hand1.append(asked_card)
                        hand2.remove(asked_card)
                        hand1.append(asked_card)
                        hand2.remove(asked_card)
                        hand1.append(asked_card)
                        hand2.remove(asked_card)
                    elif howmany2 == 4:
                        print ("I have four,", asked_card,"'s !\n")
                        hand1.append(asked_card)
                        hand2.remove(asked_card)
                        hand1.append(asked_card)
                        hand2.remove(asked_card)
                        hand1.append(asked_card)
                        hand2.remove(asked_card)
                        hand1.append(asked_card)
                        hand2.remove(asked_card)

                    

                elif asked_card not in hand2:
                    print ("I do not have the card. Go fish!")
                    drawit()
                
                
                
            elif first_move == 3:
                print (hand3) # Remove this later for final code.
                if asked_card in hand3:
                    howmany3 = hand3.count(asked_card)
                    if howmany3 == 1:
                        print ("I have one,", asked_card,"!\n")
                        hand1.append(asked_card)
                        hand3.remove(asked_card)
                    elif howmany3 == 2:
                        print ("I have two,", asked_card,"'s !\n")
                        hand1.append(asked_card)
                        hand3.remove(asked_card)
                        hand1.append(asked_card)
                        hand3.remove(asked_card)
                    elif howmany3 == 3:
                        print ("I have three,", asked_card,"'s !\n")
                        hand1.append(asked_card)
                        hand3.remove(asked_card)
                        hand1.append(asked_card)
                        hand3.remove(asked_card)
                        hand1.append(asked_card)
                        hand3.remove(asked_card)
                    elif howmany3 == 4:
                        print ("I have four,", asked_card,"'s !\n")
                        hand1.append(asked_card)
                        hand3.remove(asked_card)
                        hand1.append(asked_card)
                        hand3.remove(asked_card)
                        hand1.append(asked_card)
                        hand3.remove(asked_card)
                        hand1.append(asked_card)
                        hand3.remove(asked_card)
                    

                elif asked_card not in hand3:
                    print ("I do not have the card. Go fish!")
                    drawit()
                
                
            elif first_move == 4:
                print (hand4) # Remove this later for final code.
                if asked_card in hand4:
                    howmany4 = hand4.count(asked_card)
                    if howmany4 == 1:
                        print ("I have one,", asked_card,"!\n")
                        hand1.append(asked_card)
                        hand4.remove(asked_card)
                    elif howmany4 == 2:
                        print ("I have two,", asked_card,"'s !\n")
                        hand1.append(asked_card)
                        hand4.remove(asked_card)
                        hand1.append(asked_card)
                        hand4.remove(asked_card)
                    elif howmany4 == 3:
                        print ("I have three,", asked_card,"'s !\n")
                        hand1.append(asked_card)
                        hand4.remove(asked_card)
                        hand1.append(asked_card)
                        hand4.remove(asked_card)
                        hand1.append(asked_card)
                        hand4.remove(asked_card)
                    elif howmany4 == 4:
                        print ("I have four,", asked_card,"'s !\n")
                        hand1.append(asked_card)
                        hand4.remove(asked_card)
                        hand1.append(asked_card)
                        hand4.remove(asked_card)
                        hand1.append(asked_card)
                        hand4.remove(asked_card)
                        hand1.append(asked_card)
                        hand4.remove(asked_card)

                    

                elif asked_card not in hand3:
                    print ("I do not have the card. Go fish!")
                    drawit()
                
                
            else:
                print ("Go read the rules again, and then come try again. You clearly don't know how to play Go Fish!")


                
        elif first_player == 2:
            print ("Player #2, what would you like to do?")   
            playerdeck()
                                    
                    
                    
        elif first_player == 3:
            print ("Player #3, what would you like to do?")
            playerdeck2()
                    
        elif first_player == 4:
            print ("Player #4, what would you like to do?")

            playerdeck3()
                    
        else:
            print ("No clue what happened, but please restart the program.")     
    
    

   
def play_game():
        rules()
        who_goes_first()
        reset_game()
        print ("Now let's shuffle the deck to start!")
        deal_cards_out()
        go_fish()

play_game()
