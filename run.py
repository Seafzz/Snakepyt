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
   stdscr.addstr(0, 0, f"Welcome to Snake, {player}!")
   stdscr.addstr(2, 0, "Use the arrow keys to control the snake. You can hold down the arrows to make the snake go faster.")
   stdscr.addstr(3, 0, "Do not let the snake touch the sides of the game area or eat itself!")
   stdscr.addstr(4, 0, "The snake will grow longer each time it eats food.")
   stdscr.addstr(5, 0, "The game will end when the snake runs into the sides of the game area or eats itself.")
   stdscr.addstr(7, 0, "If you are ready, press enter to start the game.")
   stdscr.refresh()
   stdscr.getch() #wait for user input

def main(stdscr):
    # Initialize curses mode
    curses.curs_set(0) #Make cursor invisble

    # Get the height and width of the window
    sh, sw = stdscr.getmaxyx()

    #Get player information
    player = player_name(stdscr)
    if ask_played_before(stdscr) in {'no', 'n'}:
        print_instructions(stdscr)

    #Clear the screen before starting the game loop
    stdscr.clear()

    #Create the game window
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1) #Enable keypad input
    w.timeout(100) #Refresh the screen every 100ms

    #Create the snake
    snake_x = sw//4
    snake_y = sh//2
    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x-1],
        [snake_y, snake_x-2]
    ]

    #Create the food
    food = [sh//2, sw//2]
    w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

    #Initialize the game state
    key = curses.KEY_RIGHT

    #Initialize the score
    score = 0

    while True:
        """
        Main game loop for the snake game
        """
        #clear the game window
        w.clear()
        
        #display the snake and food in the game window
        w.addch(int(food[0]), int(food[1]), curses.ACS_PI)
        for segement in snake:
            w.addch(int(segement[0]), int(segement[1]), curses.ACS_CKBOARD)

         #User input for controlling the snake
        next key = w.getch()
        if next_key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
        if (next_key == curses.KEY_UP and key != curses.KEY_DOWN) or \
            (next_key == curses.KEY_DOWN and key != curses.KEY_UP) or \
            (next_key == curses.KEY_LEFT and key != curses.KEY_RIGHT) or \
            (next_key == curses.KEY_RIGHT and key != curses.KEY_LEFT):
            key = next_key
        
        #Calculate the new head of the snake
        new_head = [snake[0][0], snake[0][1]]

                
