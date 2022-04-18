import random

def game():
    playerIn = True
    dealerIn = True

#------------------------------------------------

# deck of cards / player and dealer hand
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            'Q', 'J', 'K', 'A', 'Q', 'J', 'K', 'A', 'Q', 'J', 'K', 'A', 'Q', 'J', 'K', 'A']
    playerHand = []
    dealerHand = []

#------------------------------------------------

# deal the cards
    def dealCard(turn):
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
                if total > 11:
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

# game loop
    for i in range(2):
        dealCard(dealerHand)
        dealCard(playerHand)

    while playerIn or dealerIn:
        print()
        print("-------------------------------")
        print(f"Dealer has {revealDealerHand()} and...")
        print(f"You have {playerHand} for a total of {total(playerHand)}")
        print("-------------------------------")

        if total(dealerHand) == 21:
            break

        elif playerIn:
            stayOrHit = input("1: Stay \n2: Hit\n")

#------------------------------------------------

# deals cards to the dealer, case the player chooses to stay
        if total(dealerHand) > 16:
            dealerIn = False
    
        else:
            if stayOrHit == '1':
                dealCard(dealerHand)

            else:
                pass

#------------------------------------------------

# if wants stay it ends the loop, else it deal the card
        if stayOrHit == '1':
            playerIn = False

        else:
            dealCard(playerHand)

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

#------------------------------------------------

# starts the game
game()

#------------------------------------------------



#------------------------------------------------

# checks if the player wants to play again
def rePlay():
    print()
    replay = input("Do you want to play again? (Y/N)").upper()
    if replay == "Y":
        return True

    else:
        return False

#------------------------------------------------

# case the player wants to play again it executes the game()
while rePlay():
    game()

#------------------------------------------------

print()
print("Byeeeee")
print()

#------------------------------------------------