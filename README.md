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
| **Test ID** | **Functionality Tested**                        | **Input/Actions**                           | **Expected Outcome**                                                                                     | **Actual Outcome**                                       | **Pass/Fail** |
|-------------|--------------------------------------------------|---------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------|---------------|
| T01 | Snake movement in all directions | Press **UP**, **DOWN**, **LEFT**, **RIGHT** keys | Snake should move in the respective direction with each key press | Snake moves as expected in all directions | Pass |
| T02 | Snake consumes food and grows | Move the snake to collide with the food | Snake grows in length by 1 and score increases by 1 |Snake grows and increments correctly| Pass |
| T03 | Snake dies when colliding with the wall | Move the snake to the game boundary | Game should end with a "Game Over" message when the snake collides with the wall | Game over message appears after snake hits the wall | Pass |
| T04 | Snake dies when colliding with itself | Make the snake collide with its own body | Game should end with a "Game Over" message when the snake collides with itself | Game Over message appears after snake collides with itself | Pass |
| T05 | Random food spawn after consumption | Consume food and wait for the next food item to appear | A new food item should spawn randomly on the board without overlapping the snake's body | Food spawns at a random location, not overlapping the snake | Pass |
| T06 | Score updates correctly after consumption | Eat multiple food items | Score should increase by 1 for each food item consumed | Score incremented correctly for each food item eaten | Pass |
| T07 | Snake cannot move in the opposite direction | While moving right, press the **LEFT** key | Snake should not be able to move in the opposite direction (e.g., can't move left while moving right) | Snake does not turn in the opposite direction | Pass |
| T08 | Game asks for player's name and previous play status | Start the game and enter a name. The game asks if the player has played before (yes/no) | The game asks for the player's name and whether they have played before with a yes/no input | Game asked for the name and previous play status | Pass          |
| T09 | Game displays instructions if user hasn't played before | Answer "no" when asked if you have played before | Controls and instructions should be displayed on the screen | Instructions were shown on the screen | Pass |
| T10 | Game handles invalid input for the yes/no question | Enter an invalid input (e.g., "abc") when asked if you've played before | The game should ask the question again until a valid "yes" or "no" input is given | Game asked the question again until a valid input was given | Pass |


## Screenshots
This section provides visual documentation of the Snake game, highlighting its key functionalities.

### Game Start Screen
The game starts by asking for the player's name and whether they have played before:

#### View 1: Name Input
![Game Start Screen - Name Input](https://private-user-images.githubusercontent.com/163156309/376820056-9a552605-a7e8-42d9-b476-bd97a2ded27d.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjkwMzExMjksIm5iZiI6MTcyOTAzMDgyOSwicGF0aCI6Ii8xNjMxNTYzMDkvMzc2ODIwMDU2LTlhNTUyNjA1LWE3ZTgtNDJkOS1iNDc2LWJkOTdhMmRlZDI3ZC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMDE1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTAxNVQyMjIwMjlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04MDkyYmU5ZjhlMGZjMzcyOGI0NGZlZTVhNzcwMjFhMGY5YWJkY2NjODE1ZmIwYjE2NWQ2ZWMxODczMWQ3YmY2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.vLeCqL74ZACgLDx2GYI2WS9Dfb4NYASpj2D0Ia5wKbg)

#### View 2: Previous Play Status
![Game Start Screen - Previous Play](https://private-user-images.githubusercontent.com/163156309/376820070-6d7b7280-8819-4113-9e24-f6164f01ac62.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjkwMzE4OTYsIm5iZiI6MTcyOTAzMTU5NiwicGF0aCI6Ii8xNjMxNTYzMDkvMzc2ODIwMDcwLTZkN2I3MjgwLTg4MTktNDExMy05ZTI0LWY2MTY0ZjAxYWM2Mi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMDE1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTAxNVQyMjMzMTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jODUwYWFjYWIwZjBhODZmYTA4YThlYzA1OGNlM2NhYTllYWNmYTU4ZWQyYWJjZjIwN2ExZGIxZTZkOGNmMzQ3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.ZtPC2BrAJbTu70Tsc3G8lxRfQ1oeF0PtIW95cmKRCuc)


### 2. Instructions Screen
The game explains the controls and rules for players who are new to the game.
![Instructions Screen](https://private-user-images.githubusercontent.com/163156309/376821831-db7d5969-1e0c-4319-8f2d-032cbee0e209.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjkwMzE2ODUsIm5iZiI6MTcyOTAzMTM4NSwicGF0aCI6Ii8xNjMxNTYzMDkvMzc2ODIxODMxLWRiN2Q1OTY5LTFlMGMtNDMxOS04ZjJkLTAzMmNiZWUwZTIwOS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMDE1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTAxNVQyMjI5NDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mNWNhN2FlOTAzMjgyMjY4NGM2MGI3MTZhYzRiMGE0MzY3OTRkODg3ODFjNGM1Yjg5OTVkYTI5NTBjODIxOTE3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.DcB8fuzFKYPpoXpswwKrJGeCbArknWeKiae-rBaFGFE)

### 3. Gameplay Screen
This screenshot captures the snake in action as it moves and interacts with food.
![Gameplay Screenshot](https://private-user-images.githubusercontent.com/163156309/376822940-723fd16c-401d-49c4-baba-a6ba25b9f0aa.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjkwMzIwODAsIm5iZiI6MTcyOTAzMTc4MCwicGF0aCI6Ii8xNjMxNTYzMDkvMzc2ODIyOTQwLTcyM2ZkMTZjLTQwMWQtNDljNC1iYWJhLWE2YmEyNWI5ZjBhYS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMDE1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTAxNVQyMjM2MjBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0wMGIxZjIxZjZhYWFkYTBjMDE5ZTU2NTc3YTg3ODVlYzUyNDg1N2JiN2U4ZDA3ZWI5ZTc4MGQ1Yzg3NzNiYzBjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.e6w1rL09hAkJAvGUm66mRIEIcxdUnj-dXyry6RCieBs)

### 4. Game Over Screen
Displayed when the game ends, showing the player’s score.
![Game Over Screen](https://private-user-images.githubusercontent.com/163156309/376822950-d873ee0b-da23-47c9-8c48-bc7adbb97756.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjkwMzIwODAsIm5iZiI6MTcyOTAzMTc4MCwicGF0aCI6Ii8xNjMxNTYzMDkvMzc2ODIyOTUwLWQ4NzNlZTBiLWRhMjMtNDdjOS04YzQ4LWJjN2FkYmI5Nzc1Ni5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMDE1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTAxNVQyMjM2MjBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mYjQ4MzI4OTMwNjU3MzJhNzM4ZWQ3YmY4NjliYTJjZjI5NzgzNGNkOWNkOTMzM2UxOTJjNzJmNDRlNzljYjI4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9._CUcctY8t3rIa2nQyp8AL7gTxyyhPbjAiPkJIO_dNCk)


## Known Issues
 - **Issue**: Holding down the arrow key may cause the snake to continue moving in the same direction for too long.
- **Fix**: This was caused by a blank space in the movement function. This has been removed, and no further issues have been encountered. If the problem persists, try resetting the game by restarting the application.

## Code Validation:
- The code has been validated using [pep8ci](https://pep8ci.herokuapp.com/).
- Evidence of PEP 8 compliance: ![PEP 8 Validator Results](https://private-user-images.githubusercontent.com/163156309/376796603-27c1adb0-37f5-457d-a473-d1525acfea56.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjkwMjU4ODksIm5iZiI6MTcyOTAyNTU4OSwicGF0aCI6Ii8xNjMxNTYzMDkvMzc2Nzk2NjAzLTI3YzFhZGIwLTM3ZjUtNDU3ZC1hNDczLWQxNTI1YWNmZWE1Ni5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMDE1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTAxNVQyMDUzMDlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kOTEyNzZjZDY3Y2VlYTg1M2Q5Y2MxNzk3OTVlN2FmYmJlNDZmZTllMzFiMjEyMzM2YjQzN2FmZTQ5ODJkZjliJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.E6pgebHlJz2OB9aWqroYFSTxWg8T9-0eyoUKn1AeSeY)


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
- **Python**: For providing a powerful programming environment.
- **Curses Library**: For enabling terminal handling in a user-friendly manner.
- **GitHub Copilot**: For assistance in code formatting and suggestions.
- **Special Thanks to**:
  - Sean (classmate) Pointers, discussion and suggestions
  - Christian Thompson for code inspiration. (https://gist.github.com/wynand1004)
  - Jaded Tuna for guidance on project structure. https://github.com/JadedTuna 
