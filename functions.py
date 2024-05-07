from os import system, name
import random
import time


random.seed(time)


def clear():
    if name == 'nt':
        x = system('cls')
    else:
        x = system('clear')


def draw(deck):
    x = random.randint(0, len(deck) - 1)
    card = deck[x]
    del deck[x]
    return card


def search_ace(hand):
    aces = 0
    for card in hand:
        if card.value == 11:
            aces += 1
    return aces


def score_calc(hand):
    count = 0
    for x in hand:
        count += x.value
    return count


def scoreboard(hand, pc_hand, score, pc_score=0, reveal=False):
    if not reveal:
        print("Dealer's cards:", pc_hand[0].s_name, "?")
    if reveal:
        print("Dealer's cards:", end=" ")
        for card in pc_hand:
            print(card.s_name, end=" ")
        print("\nDealer's score:", pc_score)

    print("Your cards:", end=" ")
    for card in hand:
        print(card.s_name, end=" ")
    print("\nScore:", score, "\n")
