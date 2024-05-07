import cards as c
import functions as f


def game():
    game_deck = c.deck.copy()

    player_hand = [f.draw(game_deck), f.draw(game_deck)]
    ace_number = f.search_ace(player_hand)
    score = f.score_calc(player_hand)

    dealer_hand = [f.draw(game_deck), f.draw(game_deck)]
    ace_number_dealer = f.search_ace(dealer_hand)
    score_dealer = f.score_calc(dealer_hand)
    result = "0"
    while True:
        f.scoreboard(player_hand, dealer_hand, score)

        if score == 21 and score_dealer == 21:
            result = "Draw"
            break
        elif score == 21:
            result = "Win"
            break

        print("[A] Exit", ' ' * 5, "[S] Hit", ' ' * 5, "[D] Stay")
        move = str.lower(input())
        f.clear()
        if move == "a":
            return 0
        elif move == "s":
            player_hand.append(f.draw(game_deck))
            ace_number = f.search_ace(player_hand)
            f.clear()
            print("You drew:", player_hand[len(player_hand) - 1].name)
        elif move == "d":
            break

        score = f.score_calc(player_hand)
        if score == 21:
            result = "Win"
            break
        else:
            for y in range(ace_number):
                temp_score = score
                temp_score -= 10 * y
                if temp_score == 21:
                    result = "Win"
                    break

        if score > 21:
            score -= 10 * ace_number
            if score > 21:
                result = "Loss"
                break

    if result != "Loss":
        f.clear()
        while True:
            if result != "Win" and score_dealer < 17:
                dealer_hand.append(f.draw(game_deck))
                print("Dealer drew:", dealer_hand[len(dealer_hand) - 1].name)
                score_dealer = f.score_calc(dealer_hand)
                ace_number_dealer = f.search_ace(dealer_hand)
            elif score_dealer > 21:
                score_dealer -= 10 * ace_number_dealer
                if score_dealer > 21:
                    result = "Win"
                    break
            else:
                break

        if score == score_dealer:
            result = "Draw"
        if score > score_dealer and result != "Win":
            result = "Win"
        if score < score_dealer and result != "Win":
            result = "Loss"

    f.scoreboard(player_hand, dealer_hand, score, score_dealer, True)
    if result == "Draw":
        print("Draw!")
    elif result == "Win":
        print("You won!")
    elif result == "Loss":
        if score - 10 * ace_number > 21:
            print("Bust!")
        else:
            print("You lost!")


playing = True
while playing:
    f.clear()
    x = game()
    if x == 0:
        break
    else:
        while True:
            cont = str.lower(input("Continue playing? [Y/N]"))
            if cont == "y":
                break
            elif cont == "n":
                playing = False
                break
