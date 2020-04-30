'''
create deck
create player bank
player bets
player 2 cards show, dealer 1 of 2 cards shows
GOAL: get closer to 21 than dealer
PLAYER TURN:
player can hit or stay.
hit: take another card
stay: stop getting cards

DEALER TURN:
hits if player under 21 and until player busts or beats player
bust=over 21

'''

import random

suits=('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}
playing=True

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.deck =[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        l1=''
        for card in self.deck:
            l1+='\n'+card.__str__()
        return l1
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        onecard=self.deck.pop()
        return onecard

class Chips:
    
    def __init__(self,balance=100):
        self.balance=balance
        self.bet=0
    
    def __str__(self):
        return 'Account balance:'+str(self.balance)

    def win_bet(self):
        self.balance+=self.bet

    def lost_bet(self):
        self.balance-=self.bet

class Hand:

    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0

    def __str__(self):
        l1=''
        for card in self.cards:
            l1+=' '+card.__str__()
        return l1 

    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
        if card.rank=='Ace':
            self.aces+=1

    def adjust_ace(self):
        while self.value>21 and self.aces:
            self.value-=10
            self.aces-=1

def disp_fullhands(player,dealer):
    print('Dealer hand: '+ str(dealer))
    print('Player hand: '+ str(player))

def disp_hiddenhands(player,dealer):
    print('Dealer hand: '+ str(dealer.cards[1]))
    print('Player hand: '+ str(player))
    
def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("How many chips to bet: "))
        except:
            print("Sorry, invalid response")
        else:
            if chips.bet > chips.balance:
                print(f"Sorry! Insufficient balance. Your balance is {chips.balance}")
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_ace()

def hit_stay(deck,hand):
    global playing

    while True:
        x=input("Hit or Stay? Enter h or s:")
        if x[0].lower()=="h":
            hit(deck,hand)
        elif x[0].lower()=="s":
            print("Player stays, Dealer's Turn")
            playing=False
        else:
            print("Error:hit_stay. Please provide valid input")
            continue

        break

def player_busts(player,dealer,chips):
    print("PLAYER BUSTS! Dealer wins!")
    chips.lost_bet()

def player_wins(player,dealer,chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("DEALER BUSTS! Player wins!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("DEALER WINS!")
    chips.lost_bet()

def push(player,dealer,chips):
    print("Player and Dealer Tie!")

def main():
    print("Welcome to the Blackjack table")
    global playing
    while True:
        deck_in_play=Deck()
        deck_in_play.shuffle()
        
        player_hand=Hand()
        player_hand.add_card(deck_in_play.deal())
        player_hand.add_card(deck_in_play.deal())

        dealer_hand=Hand()
        dealer_hand.add_card(deck_in_play.deal())
        dealer_hand.add_card(deck_in_play.deal())

        try:
            player_bal=int(input("How many chips: "))
        except:
            print("Sorry, invalid response")
        
        player_bank=Chips(player_bal)
        take_bet(player_bank)
        
        disp_hiddenhands(player_hand,dealer_hand)

        while playing:
            hit_stay(deck_in_play,player_hand)
            disp_hiddenhands(player_hand,dealer_hand)
            if player_hand.value>21:
                player_busts(player_hand,dealer_hand,player_bank)
                break
            
        if player_hand.value<=21:
            while dealer_hand.value<=17:
                hit(deck_in_play,dealer_hand)
            disp_fullhands(player_hand,dealer_hand)

            if dealer_hand.value>=21:
                dealer_busts(player_hand,dealer_hand,player_bank)
            elif dealer_hand.value>player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_bank)
            elif dealer_hand.value<player_hand.value:
                player_wins(player_hand,dealer_hand,player_bank)
            else:
                push(player_hand,dealer_hand,player_bank)
        print(player_bank)
            
        restart=input("Play again? Enter y/n: ")
        if restart[0].lower()=="y":
            playing=True
            continue
        else:
            print("Thanks for playing!")
            break

main()