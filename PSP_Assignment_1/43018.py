import tic_tac_toe_gui
import tkinter
    
def draw(slots):
    for i in slots:
        if i not in "X" and i not in "O":
            return False
        return True

def display_game(slots):
        for x in range(3):
            for y in range(3):
                print(slots[x*3 + y], end=' ')
                if y < 2:
                    print('|', end=' ')
            print()
            if x < 2:
                print('-' * 9)


ttt_slots = ['O', 'O', 'O', 
             ' ', 'X', 'X', 
             ' ', ' ', 'X']
            
def end_game():
    play = input("Play again? [y/n] ---> ")
    while play != 'y' and play != 'n':
        play = input("Play again? [y/n] ---> ")
    if play != 'y':
        print(f" ----------------------- END GAME -----------------------")
        feedback = input(f"any feedback? ---> ")
        print(f"Here is your feedback: {feedback}")
    elif play == 'y':
        return True

def move_computer(ttt):
    winning_move_found = False
    block_move_found = False
    slots = list(ttt.slots)
    index = 0
    while index < len(slots):
        if slots[index] == '':
            slots[index] = "O"
            if check_win(slots,"O"):
                winning_move_found = True
                ttt.move_computer(index)
                index +=10
            else:
                slots[index] = ""
        index += 1
        
    index = 0
    while index < len(slots):
        if slots[index] == '':
            slots[index] = "X"
            if check_win(slots,"X"):
                block_move_found = True
                ttt.move_computer(index)
                index +=10
            else:
                slots[index] = ""
        index += 1
        
        if not winning_move_found and not block_move_found:
            if slots[0] == "":
                ttt.move_computer(0)
            if slots[2] == "":
                ttt.move_computer(2)
            if slots[6] == "":
                ttt.move_computer(6)
            if slots[8] == "":
                ttt.move_computer(8)
                
            if slots[4] == "":
                ttt.move_computer(4)
                
            if slots[1] == "":
                ttt.move_computer(1)
            if slots[3] == "":
                ttt.move_computer(3)
            if slots[5] == "":
                ttt.move_computer(5)
            if slots[7] == "":
                ttt.move_computer(7)
            
                
def check_win(slots, letter):
    if slots == letter and slots[1] == letter and slots[2] == letter:
        return True
    elif slots[3] == letter and slots[4] == letter and slots[5] == letter:
        return True
    elif slots[6] == letter and slots[7] == letter and slots[8] == letter:
        return True
    
    elif slots[0] == letter and slots[3] == letter and slots[6] == letter:
        return True
    elif slots[1] == letter and slots[4] == letter and slots[7] == letter:
        return True
    elif slots[2] == letter and slots[5] == letter and slots[8] == letter:
        return True

    elif slots[0] == letter and slots[4] == letter and slots[8] == letter:
        return True
    elif slots[2] == letter and slots[4] == letter and slots[6] == letter:
        return True
    
    return False
#check if the game is draw
def check_draw(slots):
    if "" not in slots:
        return True
    else:
        return False

check_play = False
def display_details():
    print("""
File : 43018.pys
Author : Lua Jin Yuan Alvis
Student ID : 43018
Email ID : Luajy004
This is my own work as defined by the University's
Academic Misconduct Policy
""")

display_details()
play = input("Whould you like to play Tic Tac Toe? [y/n] ---> ")
while play != 'y' and play != 'n':
    
    play = input("Whould you like to play Tic Tac Toe? [y/n] ---> ")

if play =='y':
    check_play = True
    name = input("please input your name ---> ")
    print("--------------- Start Game ---------------")
    # The object of the TicTacToeGUI class that renders the GUI.
    # You can use this object to access the methods listed in the specification.
    ttt = tic_tac_toe_gui.TicTacToeGUI(name)

wins = 0
losses = 0
draws = 0
# set game_over to False first otherwise loop will be fail
game_over = False
# Main game loop.
while play == 'y':
    
    
    
    while True and game_over == False:
        
        # Add your game loop code here.
        if check_win(ttt.slots, "X"):
            print("---- Player wins! ----")
            result = list(ttt.slots)
            ttt.increment_wins()
            
            
            
            display_game(result)
            wins += 1
            game_over = True
            
        if check_win(ttt.slots, "O"):
            print("---- Computer wins! ----")
            result = list(ttt.slots)
            ttt.increment_losses()
            
            
            display_game(result)
            losses += 1 
            game_over = True
        if check_draw(ttt.slots):
            print("---- Draw! ----")
            result = list(ttt.slots)
            ttt.draw()
            
            
            display_game(result)
            draws += 1
            game_over = True

        
        
            
        # Updates the GUI. DO NOT REMOVE OR MODIFY!
        
        try:
            
            ttt.main_window.update()
            if not ttt.player_turn:
                move_computer(ttt)
        except (tkinter.TclError, KeyboardInterrupt):
            quit(0)
        
    again_check = False
    again_check = end_game()
        
    if again_check == True:
        # play = input("Would you like to play Tic Tac Toe? [y/n] ---> ")
        # while play != 'y' and play != 'n':
        #     play = input("Would you like to play Tic Tac Toe? [y/n] ---> ")
        game_over = False
    else:
        play = "n"
if check_play == True:
    print("\nFinal Results:")
    print(f"Wins: {ttt.get_wins()}")
    print(f"Losses: {ttt.get_losses()}")
    print(f"Drawns: {draws}")
