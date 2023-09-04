#
#  PSP Assignment 2 - Provided file (highscores.py).
#  Remove this and place appropriate file comments here.
#
#  Modify this file to include your code solution.
#
# import the 43018 blackjack assignment to this assignment
bj = __import__('43018_blackjack')

# build an array with str and an empty int for their score and name
player_names = ["","","","",""]
player_scores = [0,0,0,0,0]
# This function takes a file name and reads the contents of that file into
# the player_name and player_scores lists passed as a parameter into the
# function.
#
# The function returns the number of players read in from the file.
# You should make sure that you do not exceed the size of the lists (i.e. size
# of 5).  The player_names and player_scores lists should not exceed 5 elements.

def read_file(filename, player_names, player_scores):
    # open and read the file in line
    open_file = open(filename, 'r')
    # re-use `open_file` to build an array when text in file will go to next line ("hello\nI am Alvis") ['hello','I am ALvis']
    open_file = open_file.read().splitlines()
    # read every line in in high_score.txt
    for i in range(len(open_file)):
        open_file[i] = open_file[i].split()
        # to check if the are in string or digit and it have two varibale which is their name and theirs so = 2 
        if open_file[i][1].isdigit() and len(open_file[i]) == 2:
            # the name is 0 and the score will be 1
            player_names[i] = open_file[i][0]
            player_scores[i] = int(open_file[i][1])

# call the function
read_file('high_scores.txt', player_names, player_scores)


def write_to_file(filename, player_names, player_scores):
    # write high score to the file
    open_file = open(filename, 'w')
    
    # read every line and knows who is the highest score 
    for i in range(5):
        # if the player is not an empty string and their score is not 0
        if player_names[i] != '' and player_scores[i] != 0:
            # rewrite their names and score
            open_file.write(player_names[i] + ' ' + str(player_scores[i]) + '\n')
    # close the file
    open_file.close()
  


def display_high_scores(player_names, player_scores):
    # list two array which is score format and stars
    score_formats = ['','','','','']
    stars = ['','','','','']
    # scan all player's name
    for names in player_names:
        # if names is = to an empty string
        if names == '':
            name_length = 0
            # to build it not 22 bcause this value will be change for another people, like var and let in js 
            score_format = 32 - 10
            score_formats[player_names.index(names)] = '>' + str(score_format)
            # calculate stars base on what is the length does the player have
            stars[player_names.index(names)] = '>' + str(12 - score_length)
            # name the empty player to 'not an value name'
            player_names[player_names.index(names)] = 'not an value name'
            # if their name is less than 7 character
        elif len(names) < 7:
            name_length = len(names)
            # calculate the score format base on their name and score length
            score_length = len(str(player_scores[player_names.index(names)]))
            score_format = 32 - name_length + score_length - 1 - (7 - name_length)
            # set the score format for the player
            score_formats[player_names.index(names)] = '>' + str(score_format)
            stars[player_names.index(names)] = '>' + str(12 - score_length)
        else:
            name_length = len(names)
            score_length = len(str(player_scores[player_names.index(names)]))
            score_format = 32 - name_length + score_length - 1
            score_formats[player_names.index(names)] = '>' + str(score_format)
            stars[player_names.index(names)] = '>' + str(12 - score_length)
            
    # count who is the best and whats their score
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

    # the template
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
    
    # if player name is exist it will display the name 
    if name in player_names:
        print(f'{name} has a high score of {player_scores[player_names.index(name)]}')
    else:
        print(f'{name} does not have a high scores entry.')
        return -1


def is_high_score(player_scores, new_score):
    
    for scores in player_scores:
        # if the new score appear return the player score
        if new_score > scores:
            return player_scores.index(scores)  
    return -1 

def add_player(player_names, player_scores, new_name, new_score, insert_position):
    
    for i in range(4, insert_position, -1): #1 
        # shift existing name to let new player get in 
        player_names[i] = player_names[i-1]
        player_scores[i] = player_scores[i-1]
    # insert new player name and score
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
        # run back the black jack file
        score = bj.play_blackjack()
        # check if the score is higher or lower 
        if score > player_scores[4]:
            
            insert_position = is_high_score(player_scores, score)
            # if the player has found....
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
    
    # if the player enter quit it shows below outputs
if menu == 'quit':
    print('Goodbye - thanks for playing!')
    write_to_file('high_scores.txt', player_names, player_scores)
