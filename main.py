import functions as f


def game():
    player_cards = []
    dealer_cards = []
    player_cards.append(f.draw(player_cards, dealer_cards))
    player_cards.append(f.draw(player_cards, dealer_cards))
    dealer_cards.append(f.draw(player_cards, dealer_cards))
    dealer_cards.append(f.draw(player_cards, dealer_cards))

    ace_number = f.search_ace(player_cards)
    score = f.score_calc(player_cards)

    ace_number_dealer = f.search_ace(player_cards)
    score_dealer = f.score_calc(dealer_cards)
    result = "0"
    while True:
        f.scoreboard(player_cards, dealer_cards, score)

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
            player_cards.append(f.draw(player_cards, dealer_cards))
            ace_number = f.search_ace(player_cards)
            f.clear()
            print("You drew:", f.get_name(player_cards[len(player_cards)-1]))
        elif move == "d":
            break

        score = f.score_calc(player_cards)
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
                dealer_cards.append(f.draw(player_cards, dealer_cards))
                print("Dealer drew:", f.get_name(dealer_cards[len(dealer_cards)-1]))
                score_dealer = f.score_calc(dealer_cards)
                ace_number_dealer = f.search_ace(dealer_cards)
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

    f.scoreboard(player_cards, dealer_cards, score, score_dealer, True)
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
