# Legend
# 'X' to place the ship or if it's hit
# 'O' for a missed shot
# '.' an empty space

from random import randint

#Function to create board for computer
def create_computer_board():
    board = {'a': 0, 'b': 1, 'c':2, 'd: 3,'e': 4, 'f': 5, 'g': 6, 'h':7}

#Function to create board for player
def create_player_board():
    board = {'a': 0, 'b': 1, 'c':2, 'd: 3,'e': 4, 'f': 5, 'g': 6, 'h':7}

#Create ships
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint (0,7), randint(0,7)
        while board [ship_row][ship_column] == 'X':
            ship_row, ship_column = randint (0,7), randint(0,7)
        board [ship_row][ship_column] = 'X'

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






    
