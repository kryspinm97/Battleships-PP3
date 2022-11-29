"""
Battleships Game against a Computer 

- Generate ships at random places on board
- Print a grid sized board
- Validation of inputs 
- Score tracking (Hit ships) / Game over if all ships hit.
- Columns as Letters, Rows as Numbers 

"""

import random # Random for the random placement of the ships on the board

def intro_message():
  """
  This is an introductory message that will show when the game is first initiated.

  """

  print('\nWELCOME TO THE GAME OF BATTLESHIPS!\n')
  print('*' * 60)
  print('THE GAME BOARD AREA IS THE SIZE OF 10x10')
  print('COLUMNS ARE A - J, ROWS ARE 0 TO 9')
  print('BATTLE IT OUT AND SEE IF YOU CAN DESTROY ALL COMPUTER WARSHIPS!')
  print('YOU HAVE 20 MISSILES SO CHOOSE WISELY!')
  print('\nGOOD LUCK!\n')
  print('*' * 60)

  
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
        """
        Here we ask the user to input the column letter and the row 
        number, along with the validation of such inputs incase of
        any other character or number that is not in range being input.
        """
        try:
            letter_of_column = input("Please enter the column letter: ")
            while letter_of_column not in "ABCDEFGHIJ":
                print("Invalid Input!, Please enter a letter between A and J ")
                letter_of_column = input("Please enter the column letter: ")

            number_of_row = input("Please enter the row number: ")
            while number_of_row not in "0123456789":
                print("Invalid Input! Please input a number between 0 and 9")
                number_of_row = input("Please enter the row number: ")     

            return int(number_of_row), Board.columns_to_rows()[letter_of_column]

        except ValueError and KeyError:
            print("Invalid Input!")
            return self.user_input()

    def ships_shot_counter(self):
        """
        Here we count the ships shot. Ships are marked as an O.
        """
        ships_shot = 0

        for row in self.board:
            for column in row:
                if column == "O":
                    ships_shot += 1
        return ships_shot

    def random_ships(self):
        """
        Here we randomly place 5 ships around the board
        Between the rows and columns of 0 and 9.
        """
        for i in range(5): 
            self.number_of_row = random.randint(0, 9)
            self.letter_of_column = random.randint(0, 9)

            while self.board[self.number_of_row][self.letter_of_column] == "O":
                self.number_of_row = random.randint(0,9)
                self.letter_of_column = random.randint(0, 9)
            self.board[self.number_of_row][self.letter_of_column] = "O"
        return self.board


def Game():
    """
    This is the game run function, where we call our Board object to create the
    board for the computer and player
    We set the missiles for the ships shot
    and Run the game.
    """
    intro_message() # Here we print out our welcome message on the start of a new game
    
    player_name = input('Please enter your name: ')
 
    while True:
        if  player_name.isalpha():
            print(f'Welcome {player_name}!')
            break
        else:
            print("Invalid input!, Name must be in letters")

    print("-" * 40)

    player_board = Board([[" "] * 11 for i in range(10)]) 
    computer_board = Board([[" "] * 11 for i in range(10)])
    Ships.random_ships(computer_board)
    missiles = 20 # Set number of missiles of 20

    while missiles > 0:
        Board.print_board(player_board)

        print("_" * 40)

        player_number_of_row, player_letter_of_column = Ships.user_input(object) # Getting the user input here
        
        print("_" * 40)

        """
        Checking for missiles that have already been hit in a certain area
        """
        while player_board.board[player_number_of_row][player_letter_of_column] == "O" or player_board.board[player_number_of_row][player_letter_of_column] == "X":
            print("You've already guessed this area, try again!")
            player_letter_of_column, player_number_of_row = Ships.user_input(object)
        
        if computer_board.board[player_number_of_row][player_letter_of_column] == "O":
            print("You have sunk my battleship!")
            player_board.board[player_letter_of_column][player_number_of_row] = "O"
        
        else:
            print("You have missed!")
            player_board.board[player_number_of_row][player_letter_of_column] = "X"

        """
        Now checking for the number of missiles that have been made
        and deciding if you have won or lost the game
        """

        if Ships.ships_shot_counter(player_board) == 5:
            print("You have destroyed all the ships on the battlefield!")
            break
        else:
            missiles -= 1
            print(f'You have {missiles} missiles left')

            if missiles == 0:
                print("*" * 40)
                print(f'{player_name}, you have lost the game!')
                print(f'You have hit {Ships.ships_shot_counter(player_board)} of the ships this game')
                Board.print_board(player_board)
                print("*" * 40)
                restart_the_game()
                
def restart_the_game():
    """ 
    Here user will get asked if he would like to play the game again
    if he lost / won.
    """

    play_again = input("Would you like to play the game again? Y/N?")

    while True:
        
        if play_again == "N":
            print("Thank you for playing battleships!")
            exit()
        elif play_again == "Y":
            Game()
            
            
if __name__ == '__main__':
    Game()


            