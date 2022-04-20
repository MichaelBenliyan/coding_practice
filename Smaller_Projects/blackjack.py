from random import randint
from sys import exit

def add_card(hand, deck, num = 1): 
    i = 0 
    while i < num: 
        hand.append(deck.pop(randint(0, (len(deck)-1))))
        i += 1

def check_hand_total(hand):
    count = 0
    ace_counter = 0
    for card in hand:
        if type(card) == int: 
            count += card
        elif card == "J" or card == "Q" or card == "K":
            count += 10
        else: 
            ace_counter += 1
    if ace_counter != 0:
        i = 0
        while i < ace_counter:  
            if count + 11 > 21: 
                count += 1
                i += 1
            else: 
                count += 11
                i += 1
    if count > 21: 
        return "burn"
    else:
        return count      

def dealer(player_hand, dealer_hand, deck):
    if len(dealer_hand) < 2: 
        add_card(dealer_hand, deck)
    if len(dealer_hand) == 2 and check_hand_total(dealer_hand) == 21:
        print("Dealer Blackjack :( ")
        return lose()
    if check_hand_total(dealer_hand) == "burn": 
        print(f"Dealer's cards: {dealer_hand}\n") 
        print(f"Your cards: {player_hand}\n")
        print("Dealer Burns!")
        return win()
    elif check_hand_total(dealer_hand) >= 17: 
        print(f"Dealer's cards: {dealer_hand}\n") 
        print(f"Your cards: {player_hand}\n")
    else: 
        add_card(dealer_hand, deck)
        print(f"Dealer's cards: {dealer_hand}\n") 
        print(f"Your cards: {player_hand}\n")
        dealer(player_hand, dealer_hand, deck)

def player(player_hand, dealer_hand, deck): 
    if check_hand_total(player_hand) == 21 and len(player_hand) == 2:
        print("BLACKJACK!")
        return win()
    if check_hand_total(player_hand) == 21: 
        pass
    elif check_hand_total(player_hand) == "burn": 
        print("You Burn.")
        return lose()
    else: 
        choice = input("Type 'h' to hit or 's' to stay:").lower().rstrip()
        print()
        if choice == 'h': 
            add_card(player_hand, deck)
            print(f"Dealer's cards: {dealer_hand}\n") 
            print(f"Your cards: {player_hand}\n")
            player(player_hand, dealer_hand, deck)

        
def check_winner(player_count, dealer_count):
    if player_count > dealer_count:
        return win()
    elif dealer_count > player_count: 
        return lose()
    else: 
        push()

def win(): 
    print('*******************\n')
    print("You Win!\n")
    print('*******************\n')
    play_again()

def lose(): 
    print('*******************\n')
    print("You Lose!\n")
    print('*******************\n')
    play_again()

def push(): 
    print('*******************\n')
    print("Push! (Draw)\n")
    print('*******************\n')
    play_again()

def play_again(): 
    choice = input("Type 'y' to play again or 'n' to stop playing: ").lower().rstrip()
    if choice == 'y': 
        blackjack()
    else: 
        exit()

def blackjack(): 
    J, Q, K = 10, 10, 10
    suit_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    deck = suit_list * 4
    player_cards = []
    dealer_cards = []
    add_card(player_cards, deck, 2)
    add_card(dealer_cards, deck, 1)
    print(f"Dealer's cards: {dealer_cards}\n") 
    print(f"Your cards: {player_cards}\n")
    player(player_cards, dealer_cards, deck)
    dealer(player_cards, dealer_cards, deck)
    check_winner(check_hand_total(player_cards),check_hand_total(dealer_cards))

blackjack()