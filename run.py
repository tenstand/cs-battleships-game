# Legend
# 'X' to place the ship / or a hit
# '0' for a missed shot
# '_' an empty space

from random import randint

pc_board = []
user_board = []

#Function to create pc board 

def generate_computer_board():
    ships_counter = 5
    board= []
    for row in range(0, 5):
        columns = []
        ship_added = 0
        for column in range(0, 5):
            if ships_counter > 0 and ship_added == 0:
                value = randint(0, 1)
                if value == 1:
                    ships_counter = ships_counter - 1
                    ship_added = 1
                columns.append(value)
            else:        
                columns.append(0)
        board.append(columns) 
    return board

#Function to create user board 

def generate_user_board():
    ships_counter = 5
    board= []
    for row in range(0, 5):
        columns = []
        ship_added = 0
        for column in range(0, 5):
            board.append(columns) 
    return board

#Create ships
def create_ships(grid):
    for ship in range(8):
        ship_row, ship_column = randint(0,8), randint(0,8)
        while grid[ship_row][ship_column] == 1:
            #ship_row, ship_column = get_ship_location()
            print("X")
        grid[ship_row][ship_column] = 1

#Ship location
def get_ship_location():
    ship_location = []
    print('Please place your ship')
    while len(ship_location) < 8:
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

#check if all ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
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
    create_ships(pc_board)
    turns = 10
    while turns > 0:
        print("Take a guess")
        print_board(user_board)
        row, column = get_ship_location()
        if user_board[row][column] == "-":
            print("That space is empty.")
        elif pc_board[row][column] == "X":
            print("Hit")
            user_board[row][column] = "X" 
            turns -= 1  
        else:
            print("Miss!")
            user_board[row][column] = "-"   
            turns -= 1     
        if count_hit_ships(user_board) == 8:
            print("You win!")
            break
        print("You have " + str(turns) + " turns left")
        if turns == 0:
            print("Game ends")
            
    pc_board = generate_computer_board()
    print_board(pc_board)

