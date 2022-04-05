from random import randint
pc_board = []
user_board = []
board_x = 8
board_y = 8
empty_space = "*"
ship_board = "@"
ships = 5

def print_board(board):
    for row in board:
        print(" ".join(row))
        print("\n")
        
def input_is_valid(input, valid_values):
    try:
        if int(input) in valid_values:
            return True
        else:
            print(f"The value you entered is not valid option, pick one of {valid_values}")
            return False
    except ValueError:
        print("The value you entered is not a number, try again")
        return False
