# Legend
# 'X' to place the ship or if it's hit
# 'O' for a missed shot
# '.' an empty space

from random import randint

#Function to create board for computer and player

hidden_board = []

for x in range(0, 5):
    hidden_board.append([0] * 5)

def print_hidden_board(hidden_board):
    for row in board:
        print(" ".join(row))

player_board = []

for x in range (0, 5):
    player_board.append([0] * 5)

def print_player_board(player_board):
    for row in board:
        print(" ".join(row))

#Create ships
def create_ships(grid):
    for ship in range(5):
        ship_row, ship_column = randint(0,5), randint(0,5)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"

#Ship location
def get_ship_location():
    ship_location = []
    print('Please place your ship')
    while len(ship_location) < 7:
        row = input()
        if row not in board.keys():
            print('Please enter a valid row')
        if row in ship_location:
            print('This space is occupied')
        else: 
            ship_location.append(row)
    for row in ship_location:
        board[row] = 'O'
    return board


def input_is_valid(input, valid_values):
    try:
        if int(input) in valid_values:
            return True
        else:
            return False
    except ValueError:
        print("The value you entered is not a number, try again")
        return False


def game_menu():
    print("*******************")
    print("1 - Instructions")
    print("2 - Play Game")
    print("3 - High Scores")
    print("*******************")
    option = input("Please enter your choice:  ")
    valid_values = [1, 2, 3]
    is_valid = input_is_valid(option, valid_values)
    if is_valid:
        if int(option) == 1:
            print("show instructions")
        if int(option) == 2:
            print("show play game")
        if int(option) == 3:
            print("show score")
    else:
        print("Please select a valid number 1, 2 or 3")


if __name__ == "__main__":
    # print("Running")
    # pc_board = create_computer_board()
    # print(pc_board)
    game_menu()


