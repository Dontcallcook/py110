import pdb

def winner(deck_steve, deck_josh):
    CARD_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    score = {'Steve': 0, 'Josh': 0}
    
    while deck_steve and deck_josh:
        steve = CARD_VALUES[deck_steve.pop()]
        josh = CARD_VALUES[deck_josh.pop()]
        
        if steve > josh:
            score['Steve'] += 1
        elif josh > steve:
            score['Josh'] += 1
        
    if score['Steve'] > score['Josh']:
        return f"Steve wins {score['Steve']} to {score['Josh']}"
    elif score['Josh'] > score['Steve']:
        return f"Josh wins {score['Josh']} to {score['Steve']}"
    else:
        return "Tie"


print(winner(["A", "7", "8"], ["K", "5", "9"]))