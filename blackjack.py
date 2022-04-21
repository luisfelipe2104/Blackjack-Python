import random

#------------------------------------------------
# deck of cards
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        'Q', 'J', 'K', 'A', 'Q', 'J', 'K', 'A', 'Q', 'J', 'K', 'A', 'Q', 'J', 'K', 'A']

#------------------------------------------------

# in case there's no card
def no_cards(deck):
    print("---------------------------------------")
    print("The deck ran out of cards")
    print("We're gonna take a new deck")
    print("---------------------------------------")
    deck2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            'Q', 'J', 'K', 'A', 'Q', 'J', 'K', 'A', 'Q', 'J', 'K', 'A', 'Q', 'J', 'K', 'A']

    deck.extend(deck2)
#------------------------------------------------

while True:
    playerIn = True
    dealerIn = True

#------------------------------------------------

# player and dealer hand
    playerHand = []
    dealerHand = []

#------------------------------------------------

# deal the cards
    def dealCard(turn, deck):

 #------------------------------------------------       
        # in case there's no card
        if deck == []:
            no_cards(deck)
#------------------------------------------------

        # deals the cards randomly
        card = random.choice(deck)
        turn.append(card)
        deck.remove(card)

#------------------------------------------------

# calculate the total of each hand
    def total(turn):
        total = 0
        face = ['Q', 'J', 'K']

        for card in turn:
            if card in range(1, 11):
                total += card
        
            elif card in face:
                total += 10

            else:
                if total >= 11:
                    total += 1
                else:
                    total += 11

        return total

#------------------------------------------------

# reveals the dealer hand
    def revealDealerHand():
        if len(dealerHand) == 2:
            return dealerHand[0]

        elif len(dealerHand) > 2:
            return dealerHand

#------------------------------------------------

# shows the total of each hand
    def turn():
        print()
        print("-------------------------------")
        if len(dealerHand) == 2:
            print(f"Dealer has {revealDealerHand()} and...")
        else:
            print(f"Dealer has {dealerHand} for a total of {total(dealerHand)}")

        print(f"You have {playerHand} for a total of {total(playerHand)}")
        print("-------------------------------")

#------------------------------------------------

# game loop
    for i in range(2):
        dealCard(dealerHand, deck)
        dealCard(playerHand, deck)

    while playerIn or dealerIn:

        if total(dealerHand) == 21:
            break

        if total(playerHand) == 21:
            break

        elif playerIn:
            responses = ['1', '2']
            stayOrHit = None

            while stayOrHit not in responses:
                turn()

                stayOrHit = input("1: Stay \n2: Hit\n")


        elif not playerIn:
            turn()


#------------------------------------------------

# deals cards to the dealer, case the player chooses to stay
        if total(dealerHand) > 16:
            dealerIn = False        
    
        else:
            if stayOrHit == '1':
                dealCard(dealerHand, deck)

            else:
                pass

#------------------------------------------------

# if wants stay it ends the loop, else it deal the card
        if stayOrHit == '1':
            playerIn = False

        else:
            dealCard(playerHand, deck)

#------------------------------------------------

# ends the loop
        if total(playerHand) >= 21:
            break

#------------------------------------------------

# check if there's a blackjack
    if total(playerHand) == 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Blackjack! You win!")

    elif total(dealerHand) == 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Blackjack! Dealer wins!")

#------------------------------------------------

# case the hand is greater than 21
    elif total(playerHand) > 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("You bust! Dealer wins!")

    elif total(dealerHand) > 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Dealer busts! You win!")


#------------------------------------------------

# checks the winner
    elif 21 - total(dealerHand) < 21 - total(playerHand):
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Dealer wins!")

        
    elif 21 - total(dealerHand) > 21 - total(playerHand):
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("You win!")

    # in case of tie
    elif total(playerHand) == total(dealerHand):
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Tie!")

#------------------------------------------------

# checks if the player wants to play again
    print()
    print("-------------------------------")
    playAgain = ['Y', 'N']
    replay = None
    while replay not in playAgain:
        replay = input("Do you want to play again? (Y/N) ").upper()
    
    if replay == 'N':
        break

    else:
        pass

#------------------------------------------------

print()
print("Byeeeee")
print()

#------------------------------------------------