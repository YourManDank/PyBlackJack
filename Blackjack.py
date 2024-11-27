"""Blackjack"""

import random
import sys
# importing the random module allows us to build random number generators for the card pulling function
# importing the system module gives us basic system functionality such as input/output/error, exiting the programme or listing the python version for the purpose of debugging

HEARTS = chr(9829) # Character 9829 is '♥'
DIAMONDS = chr(9830) # Character 9830 is '♦'
SPADES = chr(9824) # Character 9824 is '♠'
CLUBS = chr(9827) # Character 9827 is '♣'
BACKSIDE = 'backside'

def main():
    print('''Blackjack
          Rules:
          >Try to get a total number of points as close to 21 as possible
          >Jacks, Queens and Kings are worth 10 points
          >Aces are worth either 1 or 11 points
          >All other cards are worth their face value
          >Jokers are not in use
          >(H) to draw another card
          >(S) to stand
          >(D) to double down on your first play, but you must draw one more card before standing
          >All bets are returned in the event of a tie
          >The Dealer must stand on 17''')

    money = 5000
    while True:
        if money <= 0:
            print("The House always wins")
            print("Thanks for playing!")
            sys.exit()

        # Player enters their bet for this round:
        print('Money:', money)

        #Draw two cards for both the Dealer and Player
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        #Handles the Player's actions:
        print('Bet:', bet)
        while True: #Keeps looping until the Player busts
            displayHands(playerHand, dealerHand, False)
            print()

        #Check if the Player has bust:
        if getHandValue(playerHand) > 21:
            break