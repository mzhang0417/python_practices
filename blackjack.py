import random
import os

SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
SUIT_NAME = {'C':'Club', 'S':'Spade', 'H':'Heart', 'D':'Diamond'}


class Card():
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + SUIT_NAME[self.suit]
    
    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

class Deck():
    def __init__(self):
        self.Deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        random.shuffle(self.Deck)
    
    def deal_card(self):
        return self.Deck.pop()

    def __str__(self):
        return str(len(self.Deck)) + " Cards left"


class Hand():
    def __init__(self):
        self.hand = []
        self.hand_value = 0

    def __str__(self):
        return str([str(card) for card in self.hand])

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        temp = []
        self.hand_value = 0
        for card in self.hand:
            r = card.get_rank()
            self.hand_value += VALUES[r]
            temp.append(r)
        if 'A' not in temp:
            return self.hand_value
        elif self.hand_value + 10 <=21:
            return self.hand_value + 10
        else:
            return self.hand_value

def clear():
    if os.name =='nt':
        os.system('CLS')
    if os.name =='posix':
        os.system('clear')

def show_hand():
    global dealer_hand, player_hand
    print("\nYour hand: ")
    print(str(player_hand))
    print("\nYour Score: ")
    print(str(player_hand.get_value()))
    print("\nDealer's hand: ")
    print(str(dealer_hand))
    print("\nDealer's Score: ")
    print(str(dealer_hand.get_value()))

def hit(hand):
    global deck
    hand.add_card(deck.deal_card())

def end():
    choice = ""
    choice = input("\nWould you like to play again? (Y/N)").lower()
    if choice == 'n':
        print('Byebye')
        exit()
    if choice == 'y':
        game()

def game():

    #Initiate Game
    clear()
    global status, deck, dealer_hand, player_hand
    status = ""
    deck = Deck()
    dealer_hand = Hand()
    player_hand= Hand()
    print("Welcome to Black Jack!\n")
    print("Dealing cards...")
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    while status != 'q':
        show_hand()
        status = input('\nDo you want to [H]it, [S]tand, or [Q]uit: ').lower()
        clear()
        while status == 'h':
            hit(player_hand)
            clear()
            show_hand()
            if player_hand.get_value() >21:
                print("\nYou are busted! Game Over!")
                status = 'q'
            else:
                status = input('\nDo you want to [H]it, [S]tand, or [Q]uit: ').lower()
        if status == 's':
            while dealer_hand.get_value() < 17:
                hit(dealer_hand)
            if dealer_hand.get_value() > 21:
                show_hand()
                print("\nYou win! Dealer is busted!")
                status = 'q'
            elif dealer_hand.get_value() >= player_hand.get_value():
                show_hand()
                print("\nYou lost!")
                status = 'q'
            elif player_hand.get_value() == 21:
                show_hand()
                print("\nYou got Black Jack! You win!!!")
                status = 'q'
            else:
                show_hand()
                print("\nYou win!!")
                status = 'q'
    if status == 'q':
    	end()


if __name__ == '__main__':
    game()

