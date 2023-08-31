bj = __import__('43018_blackjack')
# score = bj.play_blackjack()
player_names = ["","","","",""]
player_scores = [0,0,0,0,0]


def read_file(filename, player_names, player_scores):
    open_file = open(filename, 'r')
    open_file = open_file.read().splitlines()
    for i in range(len(open_file)):
        open_file[i] = open_file[i].split()
        if open_file[i][1].isdigit() and len(open_file[i]) == 2:
            player_names[i] = open_file[i][0]
            player_scores[i] = int(open_file[i][1])
        else:
            player_names[i] = open_file[i][0] + ' ' + open_file[i][1]
            player_scores[i] = int(open_file[i][2])
    

read_file('high_scores.txt', player_names, player_scores)


def write_to_file(filename, player_names, player_scores):
    
    open_file = open(filename, 'w')
    for i in range(5):
        if player_names[i] != '' and player_scores[i] != 0:
            open_file.write(player_names[i] + ' ' + str(player_scores[i]) + '\n')
    open_file.close()
  


def display_high_scores(player_names, player_scores):
    score_formats = ['','','','','']
    stars = ['','','','','']

    for names in player_names:
        if names == '':
            name_length = 0
            score_format = 32 - 10
            score_formats[player_names.index(names)] = '>' + str(score_format)
            stars[player_names.index(names)] = '>' + str(12 - score_length)
            player_names[player_names.index(names)] = '??????????'
        elif len(names) < 7:
            name_length = len(names)
            score_length = len(str(player_scores[player_names.index(names)]))
            score_format = 32 - name_length + score_length - 1 - (7 - name_length)
            score_formats[player_names.index(names)] = '>' + str(score_format)
            stars[player_names.index(names)] = '>' + str(12 - score_length)
        else:
            name_length = len(names)
            score_length = len(str(player_scores[player_names.index(names)]))
            score_format = 32 - name_length + score_length - 1
            score_formats[player_names.index(names)] = '>' + str(score_format)
            stars[player_names.index(names)] = '>' + str(12 - score_length)
    top1 = player_names[0]
    top2 = player_names[1]
    top3 = player_names[2]
    top4 = player_names[3]
    top5 = player_names[4]
    top1_score = player_scores[0]
    top2_score = player_scores[1]
    top3_score = player_scores[2]
    top4_score = player_scores[3]
    top5_score = player_scores[4]

    print("*****************************************************")
    print("*******************   Blackjack   *******************")
    print("*******************  HIGH SCORES  *******************")
    print("*****************************************************")
    print("*                                                   *")
    print("*       Player Name                     Score       *")
    print("*****************************************************")
    print("*---------------------------------------------------*")
    print(f"*       {format(top1, '7')} {format(top1_score, score_formats[0])} {format('*', stars[0])}")
    print("*---------------------------------------------------*")
    print(f"*       {format(top2, '7')} {format(top2_score, score_formats[1])} {format('*', stars[1])}")
    print("*---------------------------------------------------*")
    print(f"*       {format(top3, '7')} {format(top3_score, score_formats[2])} {format('*', stars[2])}")
    print("*---------------------------------------------------*")
    print(f"*       {format(top4, '7')} {format(top4_score, score_formats[3])} {format('*', stars[3])}")
    print("*---------------------------------------------------*")
    print(f"*       {format(top5, '7')} {format(top5_score, score_formats[4])} {format('*', stars[4])}")
    print("*---------------------------------------------------*")
    print("*****************************************************")
    if '??????????' in player_names:
        player_names[player_names.index('??????????')] = ''

def find_player(player_names, name):
    
    
    if name in player_names:
        print(f'{name} has a high score of {player_scores[player_names.index(name)]}')
        return
    else:
        print(f'{name} does not have a high scores entry.')
        return -1


def is_high_score(player_scores, new_score):
    
    for scores in player_scores:
        if new_score > scores:
            return player_scores.index(scores)  
    return -1


def add_player(player_names, player_scores, new_name, new_score, insert_position):
    
    for i in range(4, insert_position, -1):
        player_names[i] = player_names[i-1]
        player_scores[i] = player_scores[i-1]
    player_names[insert_position] = new_name
    player_scores[insert_position] = new_score
    return player_names, player_scores 

### Define lists to store high scores - player_names and player_scores lists



menu = input('Please enter command [scores, search, play, quit]: ')
while menu != 'quit':
    if menu == 'scores':
        display_high_scores(player_names, player_scores)
    elif menu == 'search':
        name = input('Please enter player name: ')
        find_player(player_names, name)
    elif menu == 'play':
        score = bj.play_blackjack()
        if score > player_scores[4]:
            insert_position = is_high_score(player_scores, score)
            if insert_position != -1:
                print('Congratulations! You have made it into the BlackJack Hall of Fame!')
                name = input('Please enter your name: ')
                add_player(player_names, player_scores, name, score, insert_position)
                write_to_file('high_scores.txt', player_names, player_scores)
        else:
            print('Sorry - you did not make it into the BlackJack Hall of Fame!')
    else:
        print('Not a valid command - please try again.')
    menu = input('Please enter command [scores, search, play, quit]: ')
if menu == 'quit':
    print('Goodbye - thanks for playing!')
    write_to_file('high_scores.txt', player_names, player_scores)
