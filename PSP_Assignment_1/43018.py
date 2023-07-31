import tic_tac_toe_gui
import tkinter

def display_game():
    pass
def end_game():
    play = input("Play again? [y/n]")
    while play != 'y' and play != 'n':
        play = input("Play again? [y/n] ---> ")
    if play != 'y':
        print(f" ----------------------- END GAME -----------------------")
        feedback = input(f"any feedback? ---> ")
        print(f"Here is your feedback: {feedback}")
        play = input("Play again? [y/n]")

def move_computer(ttt):
    slots = list(ttt.slots)
    index = 0
    while index < len(slots):
        if slots[index] == '':
            slots[index] = "O"
            if check_win(slots,"O"):
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
                ttt.move_computer(index)
                index +=10
            else:
                slots[index] = ""
        index += 1
def check_win(slots, letter):
    if slots == letter and slots [1] == letter and slots[2] == letter:
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

test_slots = [' ', ' ', 'X', ' ', 'O', 'X', ' ', 'O', 'X']
print(check_win(test_slots, 'X'))

def display_details():
    print("""
File : 43018.py
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
    name = input("please input your name ---> ")
    print("--------------- Start Game ---------------")
    # The object of the TicTacToeGUI class that renders the GUI.
    # You can use this object to access the methods listed in the specification.
    ttt = tic_tac_toe_gui.TicTacToeGUI(name)


        
# Main game loop.
while play == 'y':
    
    while True:
        # Add your game loop code here.
        if not ttt.player_turn:
            print("It's the computer's turn ---> ")
        while not ttt.check_win and not ttt.blocking_move_found:
            ttt.display_game(ttt.slots)
        if not ttt.player_turn:
            ttt.move_computer(0)
        else:
            ttt.player_turn()
            
        # Updates the GUI. DO NOT REMOVE OR MODIFY!
        try:
            ttt.main_window.update()
        except (tkinter.TclError, KeyboardInterrupt):
            quit(0)
        end_game()