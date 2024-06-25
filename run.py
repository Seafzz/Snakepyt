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
def print_instructions(stdscr):
    """
    Function to print the instructions of the game.
    """
    stdscr.clear()
    stdscr.addstr(0,0, "Instructions:")
    stdscr.addstr(1,0, "1. The snake will grow in length as it eats the food.")
    stdscr.addstr(2,0, "2. The game will end if the snake runs into the wall or itself.")
    stdscr.addstr(3,0, "3. Use the arrow keys to move the snake.")
    stdscr.addstr(4,0, "4. The snake will go faster if you hold down the key")
    stdscr.refresh()
    stdscr.getch()