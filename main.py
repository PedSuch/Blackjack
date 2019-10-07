# Author: Pedro Suchite
# Date:   October 6th, 2019
# Main file with just the elements necessary for main Gameplay

from random import shuffle
from blackjack import get_deck, card_value, hand_value, printGameStatus, playersTurn, dealersTurn

player_in = True # boolean variable that keeps track of players bust state

#### blackjack begins with these initial steps ####
deck = get_deck() # get a deck of cards, and randomly shuffle it
shuffle(deck)

# Give the dealer and the player their first two cards
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

# Continously ask the player whether they would like to "hit" or "stay"
playersTurn( player_hand, player_in, deck )

player_score_label, player_score = hand_value(player_hand)
dealer_score_label, dealer_score = hand_value(dealer_hand)

# Check to see if dealer is able to play next
dealersTurn( dealer_hand, player_score, dealer_score_label, deck )
dealer_score_label, dealer_score = hand_value(dealer_hand)

# Final check to see who won this round
printGameStatus(player_score, dealer_score)
