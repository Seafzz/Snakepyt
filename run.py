"""
A simple Python snake game
"""

import random
import curses
import re


def player_name(stdscr):
    """Function to get the player's name."""
    stdscr.clear()
    curses.echo()  # Enable text input
    while True:  # Loop until a valid name is provided
        stdscr.addstr(0, 0, "What's your name? (letters only): ")  # Prompt for name
        stdscr.refresh()
        player = stdscr.getstr().decode(encoding="utf-8").strip()  # Get the input and strip whitespace
        # Validate the name to ensure it consists of letters only
        if re.match("^[A-Za-z]+$", player):  # Check if the input is valid
            break  # Exit the loop if the name is valid
        else:
            stdscr.addstr(
                1, 0, 
                "Invalid name! Please enter letters only. Press any key to try again."
            )  # Error message
            stdscr.refresh()
            stdscr.getch()  # Wait for a key press
            stdscr.clear()  # Clear the screen for a new attempt
    curses.noecho()  # Disable text input
    return player


def ask_played_before(stdscr):
    """Function to ask if the player has played before."""
    stdscr.clear()  # Clear the screen
    stdscr.addstr(0, 0, "Have you played before? (y/n)")
    stdscr.refresh()
    while True:
        played_before = stdscr.getstr().decode(encoding="utf-8").lower()
        if played_before in {"yes", "y", "no", "n"}:
            return played_before
        else:
            stdscr.addstr(1, 0, "Please enter 'yes' or 'no'")
            stdscr.refresh()


def print_instructions(stdscr, player):
    """Function to print the instructions of the game."""
    stdscr.clear()
    stdscr.addstr(0, 0, f"Welcome to Snake, {player}!")
    stdscr.addstr(
        2,
        0,
        "Use the arrow keys to control the snake" +
        "Hold down the key to make the snake go faster.",
    )
    stdscr.addstr(
        3, 0, "Do not let the snake touch the wall or eat itself!"
    )
    stdscr.addstr(4, 0, "The snake will grow longer each time it eats food.")
    stdscr.addstr(
        5, 0,
        "The game will end when the snake runs into a wall or eat itself.",
    )
    stdscr.addstr(7, 0, "If you are ready, press enter to start the game.")
    stdscr.refresh()
    stdscr.getch()  # Wait for user input


def main(stdscr):
    """Main function to run the game."""
    # Initialize curses mode
    try:
        curses.curs_set(0)  # Make cursor invisible
    except curses.error:
        pass  # Handle the error if curs_set fails

    # Get the height and width of the window
    sh, sw = stdscr.getmaxyx()

    # Get player information
    player = player_name(stdscr)
    if ask_played_before(stdscr) in {"no", "n"}:
        print_instructions(stdscr, player)

    # Clear the screen before starting the game loop
    stdscr.clear()

    # Create the game window
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)  # Enable keypad input
    w.timeout(100)  # Refresh the screen every 100ms

    # Create the snake
    snake_x = sw // 4
    snake_y = sh // 2
    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]

    # Create the food
    food = [sh // 2, sw // 2]
    w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

    # Initialize the game state
    key = curses.KEY_RIGHT

    # Initialize the score
    score = 0

    while True:
        # Main game loop for the snake game

        # Clear the game window
        w.clear()

        # Display the snake and food in the game window
        w.addch(int(food[0]), int(food[1]), curses.ACS_PI)
        for segment in snake:
            w.addch(int(segment[0]), int(segment[1]), curses.ACS_CKBOARD)

        # User input for controlling the snake
        next_key = w.getch()
        if next_key in [
            curses.KEY_UP,
            curses.KEY_DOWN,
            curses.KEY_LEFT,
            curses.KEY_RIGHT,
        ]:
            if (
                (next_key == curses.KEY_UP and key != curses.KEY_DOWN)
                or (next_key == curses.KEY_DOWN and key != curses.KEY_UP)
                or (next_key == curses.KEY_LEFT and key != curses.KEY_RIGHT)
                or (next_key == curses.KEY_RIGHT and key != curses.KEY_LEFT)
            ):
                key = next_key

        # Calculate the new head of the snake
        new_head = [snake[0][0], snake[0][1]]

        # Move the snake in the direction of the key
        if key == curses.KEY_DOWN:
            new_head[0] += 1
        elif key == curses.KEY_UP:
            new_head[0] -= 1
        elif key == curses.KEY_LEFT:
            new_head[1] -= 1
        elif key == curses.KEY_RIGHT:
            new_head[1] += 1

        # Insert the new head of the snake
        snake.insert(0, new_head)

        # Check if the snake has eaten the food
        if snake[0] == food:
            score += 1  # Increase the score
            food = None
            while food is None:
                nf = [random.randint(1, sh - 1), random.randint(1, sw - 1)]
                food = nf if nf not in snake else None
            w.addch(food[0], food[1], curses.ACS_PI)
        else:
            # Remove the tail of the snake
            tail = snake.pop()
            w.addch(int(tail[0]), int(tail[1]), " ")

        # Check if the snake has hit itself or the wall
        if (snake[0][0] in [0, sh] or
                snake[0][1] in [0, sw] or
                snake[0] in snake[1:]):
            break

    # End curses window
    curses.endwin()

    # Print final score
    print(f"Congratulations, {player}! Your score is {score}")

    # Wait for user input to close the terminal
    input("Press any key to exit...")


# Initialize the game and start the main game loop
curses.wrapper(main)

