import random
import os
import time

RANK_VALUES = {
    '2': (2,2), 
    '3': (3,3), 
    '4': (4,4), 
    '5': (5,5), 
    '6': (6,6), 
    '7': (7,7), 
    '8': (8,8), 
    '9': (9,9), 
    '10': (10,10), 
    'J': (10,10), 
    'Q': (10,10), 
    'K': (10,10), 
    'A': (11, 1)
}

HIDDEN_CARD = ("Hidden", )
TARGET_VALUE = 21
DEALER_MIN_THRESHOLD = 17

def print_coloured(text, color_code, bold=False):
    if bold:
        prompt(f"{color_code}{text}\033[0m", bold=True)
    else:
        prompt(f"{color_code}{text}\033[0m")

def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def prompt(message, bold=False):
    if bold:
        print(f"---> \033[1m{message}\033[0m")
    else:
        print(f"---> {message}")

def display_welcome_message():
    print_coloured(f"$$$*** Welcome to {TARGET_VALUE}! "
    "***$$$".center(35), "\033[33m", bold=True)
    prompt("")

def display_rules():
    clear_screen()
    prompt("** The Rules **", bold=True)
    prompt("")
    prompt(f"- The goal of {TARGET_VALUE} is to try to "
    "get as close to {TARGET_VALUE} as possible without")
    prompt("  going over. If you go over this value, "
    "it's a bust, and you lose!")
    prompt("")
    prompt("- The player always bets first and then "
    "decides to either hit ")
    prompt("  or stay. A hit means the player wants "
    "to be dealt another card.")
    prompt(f"  Remember, if your total exceeds {TARGET_VALUE}, "
    "you will bust and lose the game.")
    prompt("  The turn is over when the player either busts or stays.")
    prompt("")
    prompt("- When the player stays, it's the dealer's turn. The dealer must ")
    prompt(f"  hit until their total is at least "
    f"{DEALER_MIN_THRESHOLD}. If the dealer busts, ")
    prompt("  then the you win!")
    prompt("")
    prompt("- The game ends when the player runs out of chips.")
    prompt("")
    prompt("")
    prompt("Press 'enter' to continue...")
    input("---> ")

def check_rules():
    prompt("Would you like to know the rules? 'Y/N'")
    choice = input("---> ").strip().lower()

    while invalid_yes_or_no(choice):
        clear_screen()
        display_welcome_message()
        prompt("Would you like to know the rules? 'Y/N'")
        choice = input("---> ").strip().lower()

    if choice.startswith("y"):
        display_rules()

    else:
        clear_screen()
        prompt("Ok! Good luck and get ready to play!")
        time.sleep(1.5)

def deck_init():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = [
        ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7),
        ('8', 8), ('9', 9), ('10', 10), ('J', 10), ('Q', 10), ('K', 10),
        ('A', 1, 11)
        ]

    return {suit: {rank[0]: rank[1:] for rank in ranks} for suit in suits}

def deal_card(deck):
    card_suit = random.choice(list(deck.keys()))
    for _ in deck[card_suit]:
        card_rank = random.choice(list(deck[card_suit].keys()))

    card = (card_suit, card_rank)
    return card

def display_cards(*args, colour=None):
    suit_unicode = {
        'Hearts': "\u2665", 
        'Diamonds': "\u2666", 
        'Clubs': "\u2663", 
        'Spades': "\u2660"
    }

    rank_formatting = []
    cards = [[] for _ in range(1, 8)]


    for i, arg in enumerate(args):

        if arg == HIDDEN_CARD:
            cards[0].extend(["+---------+", " "])
            cards[1].extend(["|| ? * ? ||", " "])
            cards[2].extend(["||* ? ? *||", " "])
            cards[3].extend(["|| ? * ? ||", " "])
            cards[4].extend(["||* ? ? *||", " "])
            cards[5].extend(["|| ? * ? ||", " "])
            cards[6].extend(["+---------+", " "])

        else:
            top_display = [" " for _ in range(1, 10)]
            btm_display = [" " for _ in range(1, 10)]

            top_rank_format(arg, top_display)
            btm_rank_format(arg, btm_display)
            rank_formatting.append((top_display, btm_display))


            cards[0].extend(["+---------+", " "])
            cards[1].extend([f"|{''.join(rank_formatting[i][0])}|", " "])
            cards[2].extend(["|         |", " "])
            cards[3].extend([f"|    {suit_unicode[arg[0]]}    |", " "])
            cards[4].extend(["|         |", " "])
            cards[5].extend([f"|{''.join(rank_formatting[i][1])}|", " "])
            cards[6].extend(["+---------+", " "])

    cards = [
        ''.join(cards[0]), ''.join(cards[1]), ''.join(cards[2]), 
        ''.join(cards[3]), ''.join(cards[4]), ''.join(cards[5]), 
        ''.join(cards[6])
        ]

    if colour == 'player':
        for row in cards:
            print_coloured(''.join(row), "\033[33m")
    if colour == 'dealer':
        for row in cards:
            print_coloured(''.join(row), "\033[91m")

def top_rank_format(card, top):
    if len(card[1]) > 1:
        top[0] = card[1][0]
        top[1] = card[1][1]
    else:
        top[0] = card[1]

def btm_rank_format(card, btm):
    if len(card[1]) > 1:
        btm[-2] = card[1][0]
        btm[-1] = card[1][1]
    else:
        btm[-1] = card[1]

def display_hands(dealer, player, chip_stack, hide_card=False):
    clear_screen()
    if hide_card:
        prompt("Dealer's total: ???", bold=True)
        display_cards(dealer[0], HIDDEN_CARD, colour='dealer')
        display_chip_stack(chip_stack)
        display_cards(*player, colour='player')
        prompt(f"Your total: {get_hand_value(player)}", bold=True)

    else:
        prompt(f"Dealer's total: {get_hand_value(dealer)}", bold=True)
        display_cards(*dealer, colour='dealer')
        display_chip_stack(chip_stack)
        display_cards(*player, colour='player')
        prompt(f"Your total: {get_hand_value(player)}", bold=True)

def update_deck(card, deck):
    deck[card[0]].pop(card[1])

def detect_ace(hand):
    for card in hand:
        if card[1] == 'A':
            return True

    return False

def get_hand_value(hand):
    hand_value = 0
    for card in hand:
        hand_value += RANK_VALUES[card[1]][0]

    if hand_value > TARGET_VALUE and detect_ace(hand):
        hand_value = 0
        for card in hand:
            hand_value += RANK_VALUES[card[1]][1]

    return hand_value

def check_bust(hand_value):
    if get_hand_value(hand_value) > TARGET_VALUE:
        return True

    return False

def resolve_bust(dealer_hand, player_hand, chip_stack, player_has_bet, bet):
    display_hands(dealer_hand, player_hand, chip_stack)
    time.sleep(1)
    prompt("You've bust!")
    time.sleep(1)
    result = check_winner(dealer_hand, player_hand)
    display_winner(result)
    update_chip_stack(chip_stack, player_has_bet, bet, result=result)

def check_winner(dealer, player):
    player_hand_value = get_hand_value(player)
    dealer_hand_value = get_hand_value(dealer)

    if (dealer_hand_value > TARGET_VALUE
    or (player_hand_value > dealer_hand_value
    and not check_bust(player))):
        return 'Player'

    if (player_hand_value > TARGET_VALUE
    or (player_hand_value < dealer_hand_value
    and not check_bust(dealer))):
        return 'Dealer'

    if player_hand_value == dealer_hand_value:
        return 'Tie'

    return None

def display_winner(result):
    if result == 'Player':
        prompt("Congratulations! You Win!")
        time.sleep(1)

    if result == 'Tie':
        prompt("It's a tie!")
        time.sleep(1)

    if result == 'Dealer':
        prompt("Sorry, you lose...")
        time.sleep(1)

def game_setup(player_hand, dealer_hand, deck):
    for i in range(0, 2):
        player_hand[i] = deal_card(deck)
        update_deck(player_hand[i], deck)
        dealer_hand[i] = deal_card(deck)
        update_deck(dealer_hand[i], deck)

def place_bets(dealer_hand, player_hand, chip_stack):
    prompt("")
    prompt("Dealer: 'Place your bets!'")

    while True:
        bet = input("---> Bet: $")

        try:
            bet = int(bet)

        except ValueError:
            clear_screen()
            prompt("Bet must be a whole number: '1', '2', '5', etc.")
            time.sleep(1.5)
            clear_screen()
            display_hands(dealer_hand, player_hand, chip_stack, hide_card=True)
            continue

        if bet <= 0:
            clear_screen()
            prompt("The minimum bet is $1...")
            time.sleep(1.5)
            clear_screen()
            display_hands(dealer_hand, player_hand, chip_stack, hide_card=True)
            continue

        if bet > chip_stack['Player']:
            clear_screen()
            prompt("You don't have enough chips!")
            time.sleep(1.5)
            clear_screen()
            display_hands(dealer_hand, player_hand, chip_stack, hide_card=True)
            continue

        break

    return int(bet)

def update_player_total(dealer_hand,
                        player_hand,
                        deck,
                        player_total,
                        chip_stack
):
    while True:
        prompt("")
        prompt("Enter 'h' to hit or 's' to stay.")
        player_choice = input("---> ").strip().lower()

        if player_choice in ['s', 'stay']:
            clear_screen()
            prompt("Player stays!")
            time.sleep(1.5)
            clear_screen()
            return player_total

        if player_choice in ['h', 'hit']:
            clear_screen()
            prompt("Player hits!")
            time.sleep(1.5)
            clear_screen()

            new_card = deal_card(deck)
            player_hand.append(new_card)
            update_deck(new_card, deck)
            player_total = get_hand_value(player_hand)

            clear_screen()
            display_hands(dealer_hand, player_hand, chip_stack, hide_card=True)

        if check_bust(player_hand):
            clear_screen()
            return player_total

    return player_total

def update_dealer_total(dealer_hand,
                        player_hand,
                        deck,
                        dealer_total,
                        chip_stack
):
    while get_hand_value(dealer_hand) <= DEALER_MIN_THRESHOLD:
        clear_screen()
        prompt("Dealer hits!")
        time.sleep(1.5)
        clear_screen()

        new_card = deal_card(deck)
        dealer_hand.append(new_card)
        update_deck(new_card, deck)

        dealer_total = get_hand_value(dealer_hand)

        clear_screen()
        display_hands(dealer_hand, player_hand, chip_stack)
        time.sleep(1.5)

        if check_bust(dealer_hand):
            prompt("Dealer has bust!")
            time.sleep(1.5)
            return dealer_total

    return dealer_total

def invalid_yes_or_no(answer):
    if answer not in ['n', 'y', 'yes', 'no']:
        return True

    return False

def ask_play_again():
    prompt("")
    prompt("Would you like to play again? 'Y/N'")
    choice = input("---> ").strip().lower()

    while invalid_yes_or_no(choice):
        prompt("Please enter 'Y' or 'N' to continue")
        choice = input("---> ").strip().lower()

    return choice

def update_chip_stack(chip_stack, player_has_bet, bet, result=None):
    if player_has_bet is False:
        chip_stack['Player'] -= bet

    if result == 'Tie':
        chip_stack['Player'] += bet

    if result == 'Player':
        chip_stack['Player'] += (bet * 2)

def display_chip_stack(chip_stack):
    player1 = list(chip_stack.keys())[0]
    prompt("")
    prompt("CHIP STACK:", bold=True)
    prompt(f"{player1}: ${chip_stack[player1]}")

def no_available_chips(chip_stack):
    if chip_stack['Player'] == 0:
        return True

    return False

def chip_stack_init(chip_stack):
    chip_stack['Player'] = 10

def play_twenty_one():
    display_welcome_message()
    time.sleep(1.2)
    check_rules()
    chip_stack = {'Player': 10}

    while True:
        deck = deck_init()
        player_hand, dealer_hand = [None, None], [None, None]
        player_has_bet = False

        game_setup(player_hand, dealer_hand, deck)
        player_total = get_hand_value(player_hand)
        dealer_total = get_hand_value(dealer_hand)

        #PLAYER TURN
        clear_screen()
        display_hands(dealer_hand,
                      player_hand,
                      chip_stack,
                      hide_card=True
        )
        bet = place_bets(dealer_hand, player_hand, chip_stack)
        update_chip_stack(chip_stack, player_has_bet, bet)
        player_has_bet = True
        display_hands(dealer_hand, player_hand, chip_stack, hide_card=True)
        player_total = update_player_total(dealer_hand,
                                           player_hand,
                                           deck,
                                           player_total,
                                           chip_stack
        )

        if player_total > TARGET_VALUE:
            resolve_bust(dealer_hand,
                         player_hand,
                         chip_stack,
                         player_has_bet,
                         bet
            )

        elif (dealer_total >= DEALER_MIN_THRESHOLD
              or dealer_total > player_total):
            display_hands(dealer_hand, player_hand, chip_stack)
            result = check_winner(dealer_hand, player_hand)
            update_chip_stack(chip_stack, player_has_bet, bet, result=result)
            display_winner(result)

        #DEALER TURN
        else:
            clear_screen()
            display_hands(dealer_hand, player_hand, chip_stack)
            dealer_total = update_dealer_total(dealer_hand,
                                               player_hand,
                                               deck,
                                               dealer_total,
                                               chip_stack
            )
            result = check_winner(dealer_hand, player_hand)
            update_chip_stack(chip_stack, player_has_bet, bet, result=result)
            display_winner(result)

        if no_available_chips(chip_stack):
            prompt("")
            prompt("Hmmm...you have no chips left!")
            prompt("Would you like to lose more money? Y/N")
            play_again = input("---> ")
            chip_stack_init(chip_stack)

            if play_again == 'n':
                clear_screen()
                prompt(f"Ok! Thanks for playing {TARGET_VALUE}!", bold=True)
                break

        else:
            play_again = ask_play_again()
            if play_again == 'n':
                clear_screen()
                prompt(f"Ok! Thanks for playing {TARGET_VALUE}!", bold=True)
                break

play_twenty_one()
