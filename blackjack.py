from modules import *

def game_on():

    print('Welcome to blackjack!')
    print('Get as close to 21 without going over!\nDealer hits until she 17 or more\nAce count as 1 or 11')

    deck = Deck()
    deck.shuffle()

    player_chips = Chip()

    game_on = True
    while game_on:

        if player_chips.total == 0:
            player_chips.total = 100

        while True:
            bet = int(input('Take your bet (your current chips are {}): '.format(player_chips.total)))
            check_chips = player_chips.make_bet(bet)
            if check_chips == False:
                print('Not enough chips')
            else:
                break
        
        dealer_hand = []
        player_hand = []

        dealer_hand.append(deck.hit())
        dealer_hand.append(deck.hit())

        player_hand.append(deck.hit())
        player_hand.append(deck.hit())

        dealer_total = 0
        dealer_bust = False

        player_total = 0
        player_bust = False

        player_win = False

        draw = False

        print("Dealer's hand:\n{} of {}\n<hidden>".format(dealer_hand[0].rank, dealer_hand[0].suit))
        print()
        print("Your hand:\n{} of {}".format(player_hand[0].rank, player_hand[0].suit))
        print("{} of {}\n".format(player_hand[1].rank, player_hand[1].suit))

        for card in player_hand:
            player_total += get_card_value(player_total, card.rank)
        
        print("Your total score is {}\n".format(player_total))

        while True:
            hit_or_stand = input("Do you want to hit or stand?\nEnter h/s:\n")

            if hit_or_stand.lower() == 'h':
                hit = deck.hit()
                player_hand.append(hit)
                print('{} of {}\n'.format(hit.rank, hit.suit))
                player_total += get_card_value(player_total, hit.rank)
                print("Your total score is {}\n".format(player_total))

                player_bust = bust(player_total)
                if player_bust:
                    print('YOU BUST!')
                    player_chips.result(not player_bust) 
                    break
            else:
                break
        
        if not player_bust:
            while dealer_total <= 17:
                hit = deck.hit()
                dealer_hand.append(hit)
                dealer_total += get_card_value(dealer_total, hit.rank)  

            print('Dealer hand:\n')
            for card in dealer_hand:
                print("{} of {}".format(card.rank, card.suit))

            print()
            print("Dealer's total score is {}\n".format(dealer_total))
            
            dealer_bust = bust(dealer_total)
            player_win = win(player_total, dealer_total)
            draw = player_total == dealer_total
            
            if dealer_bust:
                print("Dealer bust! YOU WIN!!\n")
                player_chips.result(dealer_bust)
            
            elif draw:
                print("It's a draw!\n")
            
            else:
                if player_win:
                    print('YOU WIN!!\n')
                else:
                    print('DEALER WINS!\n')
                player_chips.result(player_win)

        play_again = input('Do you want to play again?\nEnter y/n:\n')
        if play_again.lower() == 'y':
            game_on = True
        else:
            game_on = False        
             
                
game_on()
                

