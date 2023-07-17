import tic_tac_toe_gui
import tkinter

# The object of the TicTacToeGUI class that renders the GUI.
# You can use this object to access the methods listed in the specification.


ttt = tic_tac_toe_gui.TicTacToeGUI("")

    
# Main game loop.
while True:
    # Add your game loop code here.

    # Updates the GUI. DO NOT REMOVE OR MODIFY!
    try:
        ttt.main_window.update()
    except (tkinter.TclError, KeyboardInterrupt):
        quit(0)
