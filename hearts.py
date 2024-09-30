import pdb

def score_a_hand(cards):
    CARD_VALUES = {
        '2': 1,
        '3': 2,
        '4': 3,
        '5': 4,
        '6': 5,
        '7': 6,
        '8': 7,
        '9': 8,
        '1': 9,
        'J': 10,
        'Q': 11,
        'K': 12,
        'A': 13,
    }
    winning_hand = None
    for hand in cards:
        if not winning_hand:
            winning_hand = hand
        else:
            if hand[-1] == winning_hand[-1] and CARD_VALUES[hand[0]] > CARD_VALUES[winning_hand[0]]:
                winning_hand = hand
                print(f'winning_hand is {winning_hand}')
            
    return winning_hand

print(score_a_hand(['10C', 'JC','AC', 'QC']))