# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

"""
Battleships Game against a Computer 

- Generate ships at random places on board
- Print a grid sized board
- Validation of inputs 
- Score tracking (Hit ships) / Game over if all ships hit.
- Columns as Letters, Rows as Numbers 

"""

import random # Random for the random placement of the ships on the board


class Board:
    """
    Board Class that contains our print board function
    and the assignment of the Column Letters to Row Numbers.
    """

    def __init__(self, board): 
        self.board = board

    def print_board(self):
        print("  A B C D E F G H I J ")
        number_of_row = 0
        for row in self.board:
            print("%d|%s" % (number_of_row, "|" .join(row)))
            number_of_row += 1

    def columns_to_rows():
        col_to_row = {  "A": 0,
                        "B": 1,
                        "C": 2,
                        "D": 3,
                        "E": 4,
                        "F": 5,
                        "G": 6,
                        "H": 7,
                        "I": 8,
                        "J": 9,
                     }

        return col_to_row

class Ships:
    """
    Ships class that will contain the random placement of ships along the board.
    Get the user input for the row / column
    Validation of inputs by the user
    Ships Hit counter

    """

    def __init__(self, board):
        self.board = board

    def user_input(self):
        try:
            number_of_row = input("Please enter the row number of the ship: ")
            while number_of_row not in "0123456789":
                print("Invalid Input! Please input a number between 0 and 9")
                number_of_row = input("Please enter the row number of the ship: ")
            
            letter_of_column = input("Please enter the column letter of the ship: ")
            while letter_of_column not in "ABCDEFGHIJ":
                print("Invalid Input!, Please enter a letter between A and J ")
                letter_of_column = input("Please enter the column letter of the ship: ")
            return int(number_of_row), Board.columns_to_rows()[letter_of_column]
        except ValueError and KeyError:
            print("Invalid Input!")
            return self.user_input()

    def ships_shot_counter(self):
        ships_shot = 0

        for row in self.board:
            for column in row:
                if column == "X":
                    ships_shot += 1
        return ships_shot

    def random_ships(self):
        for i in range(6):
            self.number_of_row = random.randint(0, 6)
            self.letter_of_column = random.randint(0, 6)

            while self.board[self.number_of_row][self.letter_of_column] == "X":
                self.number_of_row = random.randint(0,6)
                self.letter_of_column = random.randint(0, 6)
            self.board[self.number_of_row][self.letter_of_column] = "X"
        return self.board


def Game():
    """
    This is the game run function, where we call our Board object to create the
    board for the computer and player
    We set the guesses for the ships shot
    and Run the game.
    """
    player_board = Board([[" "] * 11 for i in range(10)]) 
    computer_board = Board([[" "] * 11 for i in range(10)])
    Ships.random_ships(computer_board)
    guesses = 5 # Set number of guesses of 5

    while guesses > 0:
        Board.print_board(player_board)
      
        player_number_of_row, player_letter_of_column = Ships.user_input(object) # Getting the user input here

        """
        Checking for guesses that have already been hit in a certain area
        """
        while player_board.board[player_number_of_row][player_letter_of_column] == "*" or player_board.board[player_number_of_row][player_letter_of_column] == "X":
            print("You've already guessed this area, try again!")
            player_number_of_row, player_letter_of_column = Board.user_input(object)
        
        if computer_board.board[player_number_of_row][player_letter_of_column] == "X":
            print("YOU HIT MY BATTLESHIP!")
            player_board.board[player_letter_of_column][player_number_of_row] = "O"
        
        else:
            print("YOU MISSED")
            player_board.board[player_number_of_row][player_letter_of_column] = "*"

        """
        Now checking for the number of guesses that have been made
        and deciding if you have won or lost the game
        """

        if Ships.ships_shot_counter(player_board) == 5:
            print("YOU'VE DESTROYED ALL THE SHIPS")
            break
        else:
            guesses -= 1
            print(f'You have {guesses} guesses left')

            if guesses == 0:
                print("You have lost the game, Better luck next time !")
                Board.print_board(player_board)
                break

if __name__ == '__main__':
    Game()


            