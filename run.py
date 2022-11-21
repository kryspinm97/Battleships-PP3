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

    def __init__(self, board):
        self.board = board

    def print_board(self):
        print(" A B C D E F G H I J ")
        number_of_row = 1
        for row in self.board:
            print("%d|%s" % (number_of_row, " | " .join(row)))
            number_of_row += 1

    def columns_to_rows():
        col_to_row = {  "A" : 0,
                        "B" : 1,
                        "C" : 2,
                        "D" : 3,
                        "E" : 4,
                        "F" : 5,
                        "G" : 6,
                        "H" : 7,
                        "I" : 8,
                        "J" : 9,
        }

        return col_to_row
    