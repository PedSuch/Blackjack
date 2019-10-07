# Author: Pedro Suchite
# Date:   October 6th, 2019
# External file with helper functions necessary for the main game.

# define the card ranks, and suits
ranks = [_ for _ in range(2, 11)] + ['JACK', 'QUEEN', 'KING', 'ACE']
suits = ['SPADE', 'HEART ', 'DIAMOND', 'CLUB']

def playersTurn( player_hand, player_in, deck ):
    while player_in:
        # Display the player's current hand and its value.
        currentScore = '''\nYou are currently at {} \nwith the hand {}\n'''
        print ( currentScore.format( hand_value(player_hand)[0], player_hand )
        )
        # If the player's hand is bust end the round and player looses.
        if hand_value(player_hand)[1] == 100:
            break

        if player_in:
            response = int(input('Hit or stay? (Hit = 1, Stay = 0)'))
            # If the player asks to be hit, take the first card from the top of
            # deck and add it to their hand. If they ask to stay, change
            # player_in to false, and move on to the dealer's hand.
            if response:
                player_in = True
                new_player_card = deck.pop()
                player_hand.append(new_player_card)
                print( 'You draw {}'.format(new_player_card) )

            else:
                player_in = False


def dealersTurn( dealer_hand, player_score, dealer_score_label, deck ):
    if player_score <= 21:
        dealerHandString = '''\nDealer is at {}\nwith the hand {}\n'''
        print( dealerHandString.format(dealer_score_label, dealer_hand) )

    # Loops until the dealer's hand is less than 17
    while hand_value(dealer_hand)[1] < 17:
        new_dealer_card = deck.pop()
        dealer_hand.append(new_dealer_card)
        print( 'Dealer draws {}'.format(new_dealer_card) )


def printGameStatus( player_score, dealer_score ):
    if player_score < 100 and dealer_score == 100:
        print( 'You beat the dealer!' )

    elif player_score > dealer_score:
        print( 'You beat the dealer!' )

    elif player_score == dealer_score:
        print( 'You tied the dealer, nobody wins.' )

    elif player_score < dealer_score:
        print( "Dealer wins!" )

def get_deck():
    """Return a new deck of cards."""

    return [[rank, suit] for rank in ranks for suit in suits]

def card_value(card):
    """Returns the integer value of a single card."""

    rank = card[0]
    if rank in ranks[0:-4]:
        return int(rank)
    elif rank is 'ACE':
        return 11
    else:
        return 10

def hand_value(hand):
    """Returns the integer value of a set of cards."""

    # Naively sum up the cards in the deck.
    tmp_value = sum(card_value(_) for _ in hand)
    # Count the number of Aces in the hand.
    num_aces = len([_ for _ in hand if _[0] is 'ACE'])

    # Aces can count for 1, or 11. If it is possible to bring the value of
    #the hand under 21 by making 11 -> 1 substitutions, do so.
    while num_aces > 0:

        if tmp_value > 21 and 'ACE' in ranks:
            tmp_value -= 10
            num_aces -= 1
        else:
            break

    # Return a string and an integer representing the value of the hand. If
    # the hand is bust, return 100.
    if tmp_value < 21:
        return [str(tmp_value), tmp_value]
    elif tmp_value == 21:
        return ['Blackjack!', 21]
    else:
        return ['Bust!', 100]
