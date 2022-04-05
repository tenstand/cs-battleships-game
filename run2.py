
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

def create_empty_board(board_x, board_y):
    board = []
    for coord in range(0, board_x):
        columns = []
        for column in range(0, board_y):
            columns.append(empty_space)
        board.append(columns)
    return board

def place_random_ships(ships, board):
    ships_placed = 0
    while ships_placed < ships:
        random_coord_x = randint(0, board_x - 1)
        random_coord_y = randint(0, board_y - 1)
        if board[random_coord_x][random_coord_y] == empty_space:
            board[random_coord_x][random_coord_y] = ship_board
            ships_placed = ships_placed + 1
    return board

def place_ships_manually(ships, board):
    ships_placed = 0
    valid_coordinates_x = [x for x in range(0, board_x)]
    valid_coordinates_y = [x for x in range(0, board_y)]
    while ships_placed < ships:
        coord_x = input("Enter X coordinate for the ship")
        if input_is_valid(coord_x, valid_coordinates_x):
            coord_x = int(coord_x)
            coord_y = input("Enter Y coordinate for the ship")
            if input_is_valid(coord_y, valid_coordinates_y):
                coord_y = int(coord_y)
                if board[coord_x][coord_y] == empty_space:
                    board[coord_x][coord_y] = ship_board
                    ships_placed = ships_placed + 1
                else:
                    print(f"There is already a ship placed in {coord_x} {coord_y}")
    return board

def game_menu():
    print("*******************")
    print("1 - Instructions")
    print("2 - Play game")
    print("3 - Your score")
    print("4 - Quit")
    print("*******************")
    option = input("Please enter your choice:  ")
    valid_values = [1, 2, 3, 4]
    is_valid = input_is_valid(option, valid_values)
    if is_valid:
        if int(option) == 1:
            print("Show instructions")
        if int(option) == 2:
            print("Play game")
        if int(option) == 3:
            print("Your score is: " + str(score))
        if int (option) == "4":
                print("Goodbye!")
    else:
        print("Please select a valid number 1, 2, 3 or 4")

if __name__ == "__main__":
    user_board = create_empty_board(board_x, board_y)
    pc_board = create_empty_board(board_x, board_y)
    pc_board = place_random_ships(ships, pc_board)
    print('Pc board')
    print_board(pc_board)
    user_board = place_ships_manually(ships, user_board)
    print('User board')
    print_board(user_board)
    # print_board(user_board)
