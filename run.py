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
    stdscr.addstr(1,0, "1. The player has to guess the number between 1 and 100.")
    stdscr.addstr(2,0, "2. The player has 10 attempts to guess the number.")
    stdscr.addstr(3,0, "3. After each guess, the player will be told if the number is higher or lower.")
    stdscr.addstr(4,0, "4. If the player guesses the number, the game will end.")
    stdscr.addstr(5,0, "5. If the player runs out of attempts, the game will end.")
    stdscr.addstr(6,0, "6. Good luck!")
    stdscr.addstr(7,0, "Press any key to continue...")
    stdscr.refresh()
    stdscr.getch()
        