## File : tic tac toe.py
# Author : Andy Jordan
# Student ID : 123456789
# Email ID : joraa001
# This is my own work as defined by the University’s
## Academic Misconduct Policy

import tic_tac_toe_gui
import tkinter

# The object of the TicTacToeGUI class that renders the GUI.
# You can use this object to access the methods listed in the specification.


ttt = tic_tac_toe_gui.TicTacToeGUI("<name as input>")

    
# Main game loop.
while True:
    # Add your game loop code here.
    def move_computer(solt):
        return print("move_computer")
    def increment_wins():
        return print("increment_wins")
    def draw():
        return print("move computer")
    def get_wins():
        return print("get_wins")
    def get_losses():
        return print("get losses")
    
    print(input(ttt))
    def check_win(slots, letter):
    # Check horizontal rows
        for i in range(0, 9, 3):
            if slots[i] == slots[i+1] == slots[i+2] == letter:
                return True

    # Check vertical rows
        for i in range(3):
            if slots[i] == slots[i+3] == slots[i+6] == letter:
                return True

    # Check diagonals
            if slots[0] == slots[4] == slots[8] == letter:
                return True
            elif slots[2] == slots[4] == slots[6] == letter:
                return True

            return False

# Test with dummy list
test_slots = [' ', ' ', 'X', ' ', 'O', 'X', ' ', 'O', 'X']
print(check_win(test_slots, 'X'))  # Output: True

    # Updates the GUI. DO NOT REMOVE OR MODIFY!
    try:
        ttt.main_window.update()
    except (tkinter.TclError, KeyboardInterrupt):
        quit(0)
