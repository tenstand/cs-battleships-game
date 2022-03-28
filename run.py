# Legend
# 'X' to place the ship or if it's hit
# 'O' for a missed shot
# '.' an empty space

from random import randint

#Function to create board for computer
def create_computer_board():
    board = {'a': 0, 'b': 1, 'c':2, 'd: 3,'e': 4, 'f': 5, 'g': 6, 'h':7}

    ship_locs = random.sample(board.keys(), 8)
    for loc in ship_locs:
        board[loc] = 'O'
    return board

#Function to create board for player
def create_player_board():
    board = {'a': 0, 'b': 1, 'c':2, 'd: 3,'e': 4, 'f': 5, 'g': 6, 'h':7}

#Create ships
def create_ships(board):
    for ship in range (5):
        ship_row, ship_column = randint (0,7), randint(0,7)
        while board [ship_row][ship_column] == 'X':
            ship_row, ship_column = randint (0,7), randint(0,7)
        board [ship_row][ship_column] = 'X'





    
