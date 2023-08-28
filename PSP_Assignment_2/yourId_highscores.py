import yourId_blackjack as bj
import os
import sys
# score = bj.play_blackjack()
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
    open_file = open(os.path.join(sys.path[0], filename), 'r')
    open_file = open_file.read().splitlines()
    for i in range(4):
        open_file[i] = open_file[i].split()
        player_names[i] = open_file[i][0] + ' ' + open_file[i][1]
        player_scores[i] = int(open_file[i][2])
    print(player_names)
    print(player_scores)

read_file('./high_scores.txt', player_names, player_scores)




# This function will output the contents of the player_names and player_scores
# lists to a file in the same format as the input file.
#
# The file will need to be opened for writing in this function (and of course
# closed once all writing has been done).
#
# The function accepts the filename of the file to write to, the player_names
# and player_scores lists.
def write_to_file(filename, player_names, player_scores):
    
    # This line will eventually be removed - used for development purposes only.
    print("In function write_to_file()")

    # Place your code here
    


# This function will take the player_names list and the player_scores list
# as parameters and will output the contents of the lists to the screen.
#
# This function displays the information to the screen in the format
# specified in the assignment specifications under the section - 'Screen Format'.
def display_high_scores(player_names, player_scores):
    
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
    # format(top1_score, '>20d')
    # format(top2_score, '>20d')
    # format(top3_score, '>20d')
    # format(top4_score, '>20d')
    # format(top5_score, '>20d')

    print("*****************************************************")
    print("*******************   Blackjack   *******************")
    print("*******************  HIGH SCORES  *******************")
    print("*****************************************************")
    print("*                                                   *")
    print("*       Player Name                     Score       *")
    print("*****************************************************")
    print("*---------------------------------------------------*")
    print(f"*       {top1} {format(top1_score, '>20')}           *")
    print("*---------------------------------------------------*")
    print(f"*       {top2} {format(top2_score, '>20')}           *")
    print("*---------------------------------------------------*")
    print(f"*       {top3} {format(top3_score, '>20')}           *")
    print("*---------------------------------------------------*")
    print(f"*       {top4} {format(top4_score, '>20')}           *")
    print("*---------------------------------------------------*")
    print(f"*       {top5} {format(top5_score, '>20')}           *")
    print("*---------------------------------------------------*")
    print("*****************************************************")

display_high_scores(player_names, player_scores)

# This function will take the player's name as input along with the player_names
# list and will return the 
# position (index) of the player found in the player_names list.  You must not
# use list methods in your solution.
#
# If more than one player exists with the same name, return the position
# of the player who has the highest score (i.e. first match found).
#
# If the player is not found, the function returns -1.
def find_player(player_names, name):
    
    # This line will eventually be removed - used for development purposes only.
    print("In function find_player()")

    



# This function takes a player's score, and the player_scores list
# as input and determines whether the player is to be added to the
# high scores lists (player_names and player_scores).
#	
# If the player is to be added, the insertion position is returned from this function.
#
# If the player does not qualify to have their name recorded in the high scores lists,
# the function returns -1.  
def is_high_score(player_scores, new_score):
    
    # This line will eventually be removed - used for development purposes only.
    print("In function is_high_Score()")

    # Place your code here



# This function takes the high scores lists (player_names and player_scores),
# the player's name and score and the position to insert the player into the lists.
#
# The player is added to the high scores lists at the insert position.
# The high scores lists (player_names and player_scores) must be maintained in
# descending order of total score.  Where two players have the same total score, 
# the new player being added should appear first.
#
# (Hint: when inserting a player, simply shift all elements one position down the lists.
# You must make sure you are not exceeding list bounds and that your lists do not contain
# more than five elements).  You must not use list methods in your solution.
#
# The function returns the number of high scores stored in the lists.    
def add_player(player_names, player_scores, new_name, new_score, insert_position):
    
    # This line will eventually be removed - used for development purposes only.
    print("In function add_player()")

    # Place your code here

    



### Define lists to store high scores - player_names and player_scores lists



### Place your code here...  : )

