# Legend
# '1' to place the ship
# '2' if it's hit
# '3' for a missed shot
# '0' an empty space

from random import randint

#Function to create board for computer and player

board = []

for x in range(0, 5):
    board.append([0] * 5)

def print_board(board):
    for row in board:
        s=str(row)
        print(" ".join(s))

#Create rows and columns

def random_row(board):
    return randint(0,len(board)-1)
def random_column(board):
    return randint(0,len(board)-1)

#Create ships
def create_ships(grid):
    for ship in range(4):
        ship_row, ship_column = randint(0,4), randint(0,4)
        while grid[ship_row][ship_column] == 1:
            #ship_row, ship_column = get_ship_location()
            print("X")
        grid[ship_row][ship_column] = 1

#Ship location
# def get_ship_location():
#     ship_location = []
#     print('Please place your ship')
#     while len(ship_location) < 5:
#         row = input()
#         if row not in board.keys():
#             print('Please enter a valid row')
#         if row in ship_location:
#             print('This space is occupied')
#         else: 
#             ship_location.append(row)
#     for row in ship_location:
#         board[row] = 'O'
#     return board

#check if all ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 2:
                count += 1
    return count


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
    print("2 - Play game")
    print("3 - Your score")
    print("*******************")
    option = input("Please enter your choice:  ")
    valid_values = [1, 2, 3]
    is_valid = input_is_valid(option, valid_values)
    if is_valid:
        if int(option) == 1:
            print("show instructions")
        if int(option) == 2:
            print_board(board)
        if int(option) == 3:
            print("show score")
    else:
        print("Please select a valid number 1, 2 or 3")


if __name__ == "__main__":
    # print("Running")
    # pc_board = create_computer_board()
    # print(pc_board)
    #game_menu()

    create_ships(board)
    print_board(board)


