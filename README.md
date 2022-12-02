# Project 3 - Battleships

Here I have created a Battleships game that is ran inside the Python Terminal window,
which is also styled by the Code Institute Terminal Template. 

[!ScreenShot](./readme-images/ami-responsive.png)


## * Game Rules *

The goal of the game is to guess the enemy's battleship position that is dictated by the Game Board, positions of the ships are random and the user has to destroy all the ships to win.
You will be given a set number of missiles to shoot down the ships before the game is over.

Misses will be marked as -X

Ships that were hit will be marked as - O

# UX

 * My goal here as the creator of the terminal based game, was to give the user a simple yet grabbing logic game, where you can take a guess at where the enemies battleship position could be along with a score tracker that will display how you managed to get on at the end of the game. Having played this game in my younger days I felt like this was the best project choice for me. 

    * Give the user the ability to play against a computer
    * Easy to understand instructions / how to play
    * Ability to go again if so desired

# Features

## Current Game Features

1. The player is welcomed with an introductory message that states the games rules , how much missiles the player got and the size of the board with laballed columns and rows.

2. The player is asked to enter his/her name before the game starts.

3. The game board is printer and player will be prompted to take a guess where to fire from the 
    - Columns A - J
    - Rows 0 - 9

4. A counter that counts the ships that were hit during the game and displays them as the score at the end of the game.

5. When the game ends, the player will be prompted a message if he/she would like to play again or not , to see if you can get a better score.


# Future Features

* Having the ship sizes larger than 1 point on the grid, such as the Carrier/Battleship/Cruiser/Submarine/Destroyer
* Give the player the option to set the grid size before the game starts
* Local Multiplayer mode
* Give the ability to position the ships for the player

# Testing Stage

I have tested the game with the following steps : 

    1. I have enabled Pylint in the workspace that has checked all my code is up to standard. I had to fix 120+ errors of whitespaces/indentation/variable names and so on. Which has been adjusted for the most part to meet the PEP8 standards.
    I Have also used the Code Institute's Python Linter as a second check with no issues.

    2. I have done all the input validations tests to best of my knowledge to make sure no special characters can be entered or any inputs that are out of range, wether it was for the user name input or the Row/Column inputs.

    3.I made sure all the columns and rows are corresponding to each other and there is not any out of place information being shown to the user. 

    4. Tested the game by playing a few times myself to record any ongoing / fixed bugs and make sure all features are working as intended.


# Bugs Tracking

## Fixed Bugs :
    1. Fixed a bug where the ships would not count correctly that were hit. Where I had to adjust the ships_hit function to count the correct ship as it was counting the missed ones also.

    2. Fixed a bug where the ships that were hit were not displayed in the correct location. Fix was an incorrect order of rows/columns in the computer board which had to be swapped around as it was displaying the opposite

    3. Fixed a bug where an empty input into the columns / rows input field would crash the game. Problem was with the return statement under the except(ValueError,KeyError) block.

## Remaining Bugs :

    1. If a user writes in a higher value for the row than 11 the game will crash.

# Deployment

* The project was deployed on the Heroku website using Code Institute's terminal template. Here are the steps I have taken to successfully deploy the project: 
    
    1. Create a new repository from the Code Institute template.
    2. Create a new Heroku account / Register
    3. Create a new Heroku App
    4. Set buildpacks to Python and NodeJS in this order.
    5. Link the Heroku App into the repository on GitHub
    6. Deploy the App.


# Credits
* I would like to mention following material that has helped me immensly during this challenging yet engaging project.
    1. Code institute for the material and neccessary knowledge, also the provided template for this project.
    2. YouTube for all the battleship tutorials that have guided me along this project.
    3. Code Institute Slack Community
    4. Stack Overflow for any general queries regarding issues
    5. Google for any other queries.