"""
Battleships Game against a Computer

- Generate ships at random places on board
- Print a grid sized board
- Validation of inputs
- Score tracking (Hit ships) / Game over if all ships hit.
- Columns as Letters, Rows as Numbers

"""
import random


def intro_message():
    """
    This is an introductory message that will show when the game is first
    initiated.
    """

    print("\nWELCOME TO THE GAME OF BATTLESHIPS!\n")
    print("*" * 60)
    print("THE GAME BOARD AREA IS THE SIZE OF 10x10")
    print("COLUMNS ARE A - J, ROWS ARE 0 TO 9")
    print("BATTLE IT OUT AND SEE IF YOU CAN DESTROY ALL COMPUTER WARSHIPS!")
    print("THE COMPUTER HAS 5 SHIPS HIDDEN ON THE BOARD")
    print("YOU HAVE 20 MISSILES SO CHOOSE WISELY!")
    print("\nGOOD LUCK!\n")
    print("*" * 60)


class Board:
    """
    Board Class that contains our print board function
    """

    def __init__(self, board):
        self.board = board

    def print_board(self):
        print("  A B C D E F G H I J ")
        number_row = 0
        for row in self.board:
            print("%d|%s" % (number_row, "|".join(row)))
            number_row += 1


class Ships:
    """
    Ships class that will contain the random placement of ships along the
    board.
    Get the user input for the row / column
    Validation of inputs by the user
    Ships Hit counter

    """

    def __init__(self, board):
        self.board = board
        self.number_row = None
        self.letter_column = None

    def user_input(self):
        """
        Here we ask the user to input the column letter and the row
        number, along with the validation of such inputs incase of
        any other character or number that is not in range being input.
        """
        try:
            letter_column = input("Please enter a column letter: ").upper()
            while letter_column not in "ABCDEFGHIJ":
                print("Invalid Input!, Please enter a letter between A and J ")
                letter_column = input("Please enter a column letter: ").upper()

            number_row = input("Please enter a row number: ")
            while number_row not in '0123456789':
                print("Invalid Input! Please input a number between 0 and 9")
                number_row = input("Please enter a row number: ")

            return int(number_row), columns_to_rows()[letter_column]

        except (ValueError, KeyError):
            print("Invalid Input!")
            return Ships.user_input(self)

    def ships_hit(self):
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
        Here we randomly place a set amount of ships around the computer board
        Between the rows and columns of 0 and 9.
        """
        for i in range(10):
            self.number_row = random.randint(0, 9)
            self.letter_column = random.randint(0, 9)

            while self.board[self.number_row][self.letter_column] == "O":
                self.number_row = random.randint(0, 9)
                self.letter_column = random.randint(0, 9)
            self.board[self.number_row][self.letter_column] = "O"
        return self.board


def columns_to_rows():  # Assigning the columns to rows
    col_to_row = {
        "A": 0,
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


def run_game():
    """
    This is the game run function, where we call our Board object to create the
    board for the computer and player
    We set the missiles for the ships shot
    and Run the game.
    """
    intro_message()  # Run the welcoming message at start of game

    player_name = input("Please enter your name: ")

    while True:
        if player_name.isalpha():   # only input letters (a-z)
            print(f"Welcome {player_name}!")
            break
        else:
            print("Invalid input!, Name must be in letters")
            player_name = input("Please enter your name: ")

    print("-" * 40)

    user_board = Board([[" "] * 11 for i in range(10)])
    computer_board = Board([[" "] * 11 for i in range(10)])
    Ships.random_ships(computer_board)
    missiles = 20  # Set number of missiles of 20

    while missiles > 0:
        Board.print_board(user_board)
        print("_" * 40)

        user_number_row, user_letter_column = Ships.user_input(object)

        print("-" * 40)
        """
        Here we get the validation and also checking for duplicate guesses.
        If the ship has been hit already, If it hasn't or if it was a miss.
        """

        while (
            user_board.board[user_number_row][user_letter_column] == "O"
            or user_board.board[user_number_row][user_letter_column] == "X"
        ):
            print("You've already guessed this area, try again!")
            user_number_row, user_letter_column = Ships.user_input(object)

        if computer_board.board[user_number_row][user_letter_column] == "O":
            print("You have sunk my battleship!")
            user_board.board[user_number_row][user_letter_column] = "O"

        else:
            print("You have missed!")
            user_board.board[user_number_row][user_letter_column] = "X"

        """
        Now checking for the number of missiles that have been made
        and deciding if you have won or lost the game
        """

        if Ships.ships_hit(user_board) == 5:
            print(f" *** CONGRATULATIONS {player_name} !!")
            print("-" * 40)
            print("You have destroyed all the ships on the battlefield!")
            print("-" * 40)
            print("Here is a display of the ships you have hit")
            Board.print_board(user_board)
            print("-" * 40)
            restart_the_game()
        else:
            missiles -= 1
            print(f"You have {missiles} missiles left")
            print("-" * 40)

            if missiles == 0:
                print("*" * 40)
                print(f"{player_name}, you have lost the game!")
                print("-" * 40)
                print(
                    f"You have hit {Ships.ships_hit(user_board)} ships")
                print("Better Luck next time!")
                print("-" * 40)
                Board.print_board(user_board)
                print("-" * 40)
                restart_the_game()


def restart_the_game():
    """
    Here user will get asked if he would like to play the game again
    if he lost / won.
    """

    play_again = input("Would you like to play the game again? Y/N?")

    while True:
        if play_again == "N":
            print("*" * 40)
            print("Thank you for playing Battleships!")
            print("*" * 40)
            exit()
        elif play_again == "Y":
            run_game()


if __name__ == "__main__":
    run_game()
