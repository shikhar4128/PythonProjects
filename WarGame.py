import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values={'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        # Here we need to create a deck which contains all 52 card objects
        # SO we create an empty list with no user input
        self.all_cards = []

        # To store each card use this loop:
        for suit in suits:
            for rank in ranks:
                # Create ard objects
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    # Now we need to shuffle this deck
    def shuffle(self):
        random.shuffle(self.all_cards)  # We dont need to return anything as shuffle return type is None
                                        # Also we dont need to store this anywhere as the only purpose is to know if deck is shuffled

    # Now we need to create a method that can remove cards (one deal card or two deal)
    def dealOne(self):
        return self.all_cards.pop()  # Returning one card from list.

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def removeOne(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            return self.all_cards.extend(new_cards)
        else:
            return self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'

#GAME SETUP

player1=Player("ONE")
player2=Player("TWO")

new_deck=Deck()

new_deck.shuffle()

for deal in range(26):
    player1.add_cards(new_deck.dealOne())
    player2.add_cards(new_deck.dealOne())


game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f'Round number: {round_num}')

    # Check if any player have zero cards after every round(First round that wont be the case still need oto check)
    # IF anyone has zero then other player wins and game ends
    if len(player1.all_cards) == 0:
        print('Player 1 is out of cards!! Player 2 wins!!')
        game_on = False
        break

    if len(player2.all_cards) == 0:
        print('Player 2 is out of cards!! Player 1 wins!!')
        game_on = False
        break

    # Start of new round
    player1_cards = []  # This variable we can think of is cards player will leave on table. LIke currenct cards in play.
    # This is not similar to player1.all_cards defined above. That is something player holds close to them in hand,face down

    # SO to start a new round we need to remove cards from player1.all_cards(all card list for p1) and append to player1_cards(current card in play)
    player1_cards.append(player1.removeOne())

    player2_cards = []
    player2_cards.append(player2.removeOne())

    # COMPARING CARDS
    compare_Cards = True

    while compare_Cards:
        if player1_cards[-1].value > player2_cards[-1].value:
            player1.add_cards(player1_cards)
            player1.add_cards(player2_cards)
            compare_Cards = False

        elif player1_cards[-1].value < player2_cards[-1].value:
            player2.add_cards(player1_cards)
            player2.add_cards(player2_cards)
            compare_Cards = False

        else:
            print('WAR!!')  # both cards are equal
            if len(player1.all_cards) < 5:
                print('Player 1 is unable to play war! Game over at War')
                print('Player 2 Wins!!')
                compare_Cards = False
                break

            elif len(player2.all_cards) < 5:
                print('Player 2 is unable to play war! Game over at War')
                print('Player 1 Wins!!')
                compare_Cards = False
                break

            else:
                for num in range(5):
                    player1_cards.append(player1.removeOne())
                    player2_cards.append(player2.removeOne())