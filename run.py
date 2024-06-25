import random
import curses

def player_name(stdscr):
    """
    Function to get the player's name.
    """
    stdscr.clear()
    curses.echo() #Enable text input
    stdscr.addstr(0,0 "What's your name?")
    stdscr.refresh()
    player = stdscr.getstr().decode(encoding="Utf-8")
    curses.noecho() #Disable text input
    return player

 def ask_played_before(stdscr):
        """
        Function to ask if the player has played before.
        """
        stdscr.clear() #Clear the screen
        stdscr.addstr(0,0, "Have you played before? (y/n)")
        stdscr.refresh()
        while True:
            played before == stdscr.getstr().decode(encoding="utf-8").lower()
            if played_before in {'yes', 'y', 'no', 'n'}:
                return played_before
            else:
                stdscr.addstr(1,0, "Please enter 'yes' or 'no'")
                stdscr.refresh()
                
        