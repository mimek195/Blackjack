from os import system, name
import random
import time

random.seed(time)


def draw(player_cards, dealer_cards):
    cards_drew = player_cards + dealer_cards
    return random.choice([i for i in range(0, 51) if i not in cards_drew])


def get_name(card_id):
    card_names = ["♥ Two", "♥ Three", "♥ Four", "♥ Five", "♥ Six", "♥ Seven", "♥ Eight", "♥ Nine", "♥ Ten",
                  "Valet of Hearts", "Queen of Hearts", "King of Hearts", "Ace of Hearts",
                  "♠ Two", "♠ Three", "♠ Four", "♠ Five", "♠ Six", "♠ Seven", "♠ Eight", "♠ Nine", "♠ Ten",
                  "Valet of Spades", "Queen of Spades", "King of Spades", "Ace of Spades",
                  "♦ Two", "♦ Three", "♦ Four", "♦ Five", "♦ Six", "♦ Seven", "♦ Eight", "♦ Nine", "♦ Ten",
                  "Valet of Diamonds", "Queen of Diamonds", "King of Diamonds", "Ace of Diamonds",
                  "♣ Two", "♣ Three", "♣ Four", "♣ Five", "♣ Six", "♣ Seven", "♣ Eight", "♣ Nine", "♣ Ten",
                  "Valet of Clubs", "Queen of Clubs", "King of Clubs", "Ace of Clubs"]
    return card_names[card_id]


def get_short_name(card_id):
    card_short_name = ["♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥V", "♥Q", "♥K", "♥A",
                       "♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠V", "♠Q", "♠K", "♠A",
                       "♦2", "♦3", "♦4", "♦5", "♦6", "♦7", "♦8", "♦9", "♦10", "♦V", "♦Q", "♦K", "♦A",
                       "♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣V", "♣Q", "♣K", "♣A"]
    return card_short_name[card_id]


def get_value(card_id):
    card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                   2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                   2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                   2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return card_values[card_id]


def search_ace(hand):
    ace_list = [12, 25, 38, 51]
    ace_count = 0
    for a in hand:
        for aces in ace_list:
            if a == aces:
                ace_count += 1
    return ace_count


def clear():
    if name == 'nt':
        x = system('cls')
    else:
        x = system('clear')


def score_calc(hand):
    count = 0
    for x in hand:
        count += get_value(x)
    return count


def scoreboard(hand, pc_hand, score, pc_score=0, reveal=False):
    if not reveal:
        print("Dealer's cards:", get_short_name(pc_hand[0]), "?")
    if reveal:
        print("Dealer's cards:", end=" ")
        for card in pc_hand:
            print(get_short_name(card), end=" ")
        print("\nDealer's score:", pc_score)

    print("Your cards:", end=" ")
    for card in hand:
        print(get_short_name(card), end=" ")
    print("\nScore:", score, "\n")

