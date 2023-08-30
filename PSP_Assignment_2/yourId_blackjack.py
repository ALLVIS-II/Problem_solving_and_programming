import random

def get_choice():
    choice = input('Would you like to hit or stand? [h/s] ---> ')
    while choice != 'h' and choice != 's':
        choice = input('Would you like to hit or stand? [h/s] ---> ')
    return choice

def deal_players_hand():
    player_first_die, player_second_die = random.randint(1, 10), random.randint(1, 10)
    player_total_score = player_first_die + player_second_die
    print('\nPlayer hand: {} + {} = {}'.format(player_first_die, player_second_die, player_total_score))
    choice = get_choice()
    while choice == 's' and player_total_score < 15:
        print('\nCannot stand on value less than 15!\n')
        choice = 'h'
    while choice == 'h':
        
        dice = random.randint(1, 10)
        if dice == 1:
            if player_total_score + dice > 21:
                dice = 1
            else:
                dice = 11

        player_old_total_score = player_total_score
        player_total_score += dice
        if player_total_score > 21:
            print('Player hand: {} + {} = {}'.format(player_old_total_score, dice, player_total_score))
            print('PLAYER BUSTS!')
            choice = 's'
        else:
            print('Player hand: {} + {} = {}'.format(player_old_total_score, dice, player_total_score))
            choice = get_choice()
            if choice == 's' and player_total_score < 15:
                print('\nCannot stand on value less than 15!\n')
                choice = 'h'
        
            
    return player_total_score
    
def deal_dealers_hand(dealer_hand):
    dealer_die = random.randint(1, 10)
    dealer_total_score = dealer_hand + dealer_die
    print('\nDealer hand: {} + {} = {}'.format(dealer_hand, dealer_die, dealer_total_score))
    while dealer_total_score < 17:
        dice = random.randint(1, 10)
        if dice == 1:
            if dealer_total_score + dice > 21:
                dice = 1
            else:
                dice = 11
        dealer_old_total_score = dealer_total_score
        dealer_total_score += dice
        if dealer_total_score > 21:
            print('Dealer hand: {} + {} = {}'.format(dealer_old_total_score, dice, dealer_total_score))
            print('DEALER BUSTS!')
        else:
            print('Dealer hand: {} + {} = {}'.format(dealer_old_total_score, dice, dealer_total_score))
    return dealer_total_score

def determine_winner(player_total_score, dealer_total_score):
    if player_total_score > 21:
        return 0
    elif dealer_total_score > 21:
        return 1
    elif player_total_score > dealer_total_score:
        return 1
    elif dealer_total_score > player_total_score:
        return 0
    else:
        return 3


def play_blackjack():
    total_score = 0
    again = 'y'
    while again == 'y':
        dealer_hand = random.randint(1, 10)
        print('Dealer hand:', dealer_hand)
        player_total_score = deal_players_hand()
        dealer_total_score = deal_dealers_hand(dealer_hand)
        check = determine_winner(player_total_score, dealer_total_score)
        if check == 3:
            print(f'Dealer = {dealer_total_score} Player = {player_total_score} *** Push - no winners. ***')
            total_score += 1
        if check == 1:
            print(f'Dealer = {dealer_total_score} Player = {player_total_score} *** Player wins! ***')
            total_score += 3
        if check == 0:
            print(f'Dealer = {dealer_total_score} Player = {player_total_score} *** Dealer wins! ***')
        again = input(f'Your score: {total_score} - Play again [y|n]? ')
        while again != 'y' and again != 'n':
            again = input(f'Please enter y or n. Play again [y|n]? ')
        

    return total_score

# # Call function play_blackjack() - plays blackJack against the computer
# score = play_blackjack()
# # Display score to the screen
# print('\n\nYour score is:', score)