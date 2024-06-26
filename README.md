# Snake Game

## Introduction
Welcome to the Snake Game implemented in Python using the `curses` library. This classic arcade game allows you to control a snake that grows in length as it eats food, while avoiding collisions with walls and itself.

## Features
- **Snake Movement:** Use arrow keys to control the direction of the snake.
- **Scoring:** The score increases each time the snake eats food.
- **Game Over:** The game ends if the snake collides with the walls or itself.
- **Instructions:** Clear instructions provided at the start of the game.

## Requirements
- python 3.x or newer
- curses library (standard in Python)

## How to play
1. **Installation:**
- Ensure Python 3.x is installed on your system.
- No additional libraries is required as "Curses" is a part of the python standard library.

2. ***Running the Game***
- Clone the repository
- Open a terminal or command prompt
- Navigate to the directory containing "snakepyt"
- Run the game using the command: "python snakepyt.game.py

3. ***Game Controls:***
- Use the arrow keys ("Up", "Down", "Left", "Right") to controll the snake's direction.
- Hold down the arrow key to speed up the snake.

4. ***Objectives***
- Guide the snake to eat the food that appears randomly on the screen.
- Avoid Collisions with the walls and the snake's own body.

5. ***Ending the Game:***
- The game will end when the snake collides with the walls or itself.
- Your final score will be displayed.

6. ***Restarting the Game:***
- After the game ends, press any key to exist the game.

### Manual testing
I tested it, and my friends tested the game.


## Known Issues
 - Holding down the key would sometimes cause the snake to keep moving the same direction for a prolonged period of time and would not stop going that same direction until an unspecified amount of time had gone by.
    Fix: This was caused by an blank space being present in the movement function this is now removed and there hasnt been an issue after.

## Validation:
I used flake and black to validate my code to meet pep8 standard
It passed with minor problems some of the issues I had was:
- blank lines contains whitespace
- Line to long

     All errors was fixed.

### Technologies Used
- Python library curses
- Gitpod and github
- Github co-pilot
- Heroku
- Black and Flake8 

### Deployment
1. 
2. Log into Heroku
3. On Heroku click the menu and navigate to "New" and select "Create new app"
4. Chose a name for your app, choose the region you are deploying from and then click "Create app"
5. After you have clicked "Create app" Check "Deployment Method" and make sure you mark "Github"
6. Once that is checked, go to "Search for repository to connect to: 
- Choose the correct github account
- Insert the name of the repository in this case: Snakepyt and click search.
7. In deploy from Github make sure the branch is main, Then press Deploy Branch.



## Credits

- Github co-pilot (Formating code to meet pep8 standard, code suggestions and to awnser code related questions)
- Sean (classmate) Brainstorming, suggestions and pointers!
- Python and curses library
- Christian Thompson (https://gist.github.com/wynand1004)
- Jaded Tuna https://github.com/JadedTuna 
