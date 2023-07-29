## File : tic tac toe.py
# Author : Andy Jordan
# Student ID : 123456789
# Email ID : joraa001
# This is my own work as defined by the University’s
## Academic Misconduct Policy

import tic_tac_toe_gui
import tkinter

play = input("Whould you like to play Tic Tac Toe? [y/n] ---> ")
while play != 'y' and play != 'n':
    play = input("Whould you like to play Tic Tac Toe? [y/n] ---> ")

# The object of the TicTacToeGUI class that renders the GUI.
# You can use this object to access the methods listed in the specification.

ttt = tic_tac_toe_gui.TicTacToeGUI("<name as input>")

        
# Main game loop.
while play == 'y':
    
    while True:
        # Add your game loop code here.
        print(ttt.player_turn)
        # Updates the GUI. DO NOT REMOVE OR MODIFY!
        try:
            ttt.main_window.update()
        except (tkinter.TclError, KeyboardInterrupt):
            quit(0)
    play = input("Play again? [y/n]")
    while play != 'y' and play != 'n':
        play = input("Play again? [y/n] ---> ")