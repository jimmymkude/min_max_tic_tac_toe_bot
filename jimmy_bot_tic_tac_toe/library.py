
########################################################################
#
# Created by: Jimmy Mkude
# Date Created: 6/15/2017
#
########################################################################


def initialize_board(content_list):
    board = []
    index = 0
    for i in range(3):
        row = []
        for j in range(3):
            row.append(content_list[index])
            index += 1
        board.append(row)
            
    return board
    
    
def print_guidelines():
    print()
    print("######################################################")
    print("Jimmy's Tic Tac Toe Board")
    print()
    print("Coordinate Guideline:")
    content = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    board = initialize_board(content)
    draw_board(board)
    
    print("######################################################")
    print()
    print("Modes: ['1': 1 Player, '2': 2 Player, '3': CPU v CPU]")
    print()
    print("######################################################")
    print()
    print("Diffuculty: ['easy', 'medium', 'hard']")
    print()
    print("######################################################")
    print()
    print("Syntax: python3 tic_tac_toe.py <mode> <difficulty>")
    print("e.g. To play CPU on 'hard' difficulty you would run: ")
    print("     python3 tic_tac_toe.py 1 hard")
    print()

def draw_board(board):
    
    print()
    print("  __  __  __")
    for row in board:
        row_str = ""
        for cell in row:
             row_str += " " + cell + " |"
        print(" |" + row_str)
        print("  __  __  __")
        print()
        

def is_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        print("Error. Please select an integer from 1 to 9.\n")
        return False
        

def get_choice(player_char):
    choice = ''
    valid = False  
    while not valid:
        choice = input("Player {}'s turn:    ".format(player_char))
        valid = is_integer(choice)
        
    choice = int(choice) - 1
    
    row = 2
    col = -1
    while(row >= 0):
        col = choice - 3 * row
        if col >= 0 and col <= 2:
           break 
        
        row -= 1
        
    return (row, col)

def board_full(board):
    for row in board:
        for char in row:
            if char == ' ':
                return False
    return True
    
    
def validate_cood(x, y):
    return x >= 0 and x <= 2 and y >=0 and y <=2
    
    
def validate_choice(board, x, y, mode='verbose'):
    if validate_cood(x,y) and board[x][y] == ' ':
        return True
    
    if mode == 'verbose':    
        print("Invalid Choice. Please select an integer from 1 to 9 for an open spot on the grid.")
    return False   
    
    
    
"""
    Recursive Depth first, goes in /(direction) until it steps out of bounds
    Tries to find a sequence of 3 similar characters in the path
"""
def try_path(board, x, y, player_char, direction, curr_length):
    if board[x][y] != ' ' and board[x][y] == player_char:
        curr_length += 1
        if curr_length >= 3:
            return True
        next_x = x + direction[0]
        next_y = y + direction[1]
        
        if validate_cood(next_x, next_y):
            return try_path(board, next_x, next_y, player_char, direction, curr_length)
            
    return False
        
        
"""
    Iterates through each valid neighbours and tries the path
    recursively using try_path()
"""
def try_paths(board, row, col):
    neighbour_x = [1, 1, 0, -1]
    neighbour_y = [0, 1, 1, 1]
    player_char = board[row][col]
    
    # for the 4 adjacent (right, down-right, down, down-left) neighbours
    for i in range(4):
        x = row + neighbour_x[i]
        y = col + neighbour_y[i]
        
        # if it is a valid neighbour
        if validate_cood(x, y):
            direction = (neighbour_x[i], neighbour_y[i])
            found = try_path(board, x, y, player_char, direction, 1)
            if found:
                return True
    
    return False
        
        

"""
    Iterates through each box in the grid and tries its paths using try_paths
    Skips empty boxes
"""
def find_win(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            player_char = board[row][col]
            if player_char == ' ':
                continue
            found = try_paths(board, row, col)
            if found:
                return (True, player_char)
    
    return (False, '')
    

def game_over(board):
    (won, player_char) = find_win(board)
    
    if won:
        print("Player {} won.".format(player_char))
        return True
        
    if board_full(board):
        print("Tie.")
        return True
    
    return False 
    

    
