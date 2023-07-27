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
    # Updates the GUI. DO NOT REMOVE OR MODIFY!
    try:
        ttt.main_window.update()
    except (tkinter.TclError, KeyboardInterrupt):
        quit(0)
