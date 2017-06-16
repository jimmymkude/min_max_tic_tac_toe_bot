
########################################################################
#
# Created by: Jimmy Mkude
# Date Created: 6/15/2017
#
########################################################################



import sys

from player import Bot
import library as game



   
def update_board(board, row, col, char, bots):
    board[row][col] = char
    for bot in bots:
        if bot.active:
            bot.update_board(row, col, char)
    
    return board
    
def play(board, mode='2P', difficulty=3):
    game_not_over = True
    turn = 0
    player_char = 'X'
    bot1 = Bot(board)
    bot2 = Bot(board)
    
    while game_not_over:
        # switch turns
        turn = turn ^ 1  
        if turn:
            player_char = 'X'
        else:
            player_char = 'O'
            
        choice_valid = False
        
        row = -1
        col = -1
        
        while not choice_valid:
            if mode == '2P':
                (row, col) = game.get_choice(player_char)
            elif mode == 'CPU':
                #(row, col) = cpu_play(board, player_char)
                pass
            elif mode == '1P':
                bot1.activate(difficulty=difficulty)
                print("jimmy_bot: \"{}\"".format(bot1.msg))
                if turn:
                    (row, col) = game.get_choice(player_char)
                else:
                    (row, col) = bot1.play()
                    print("jimmy_bot: \"{}\"".format(bot1.msg))
                    
                    
            #print("(" + str(row) + ", " + str(col) + ")")
            choice_valid = game.validate_choice(board, row, col)
            
        
        # update and draw board
        update_board(board, row, col, player_char, [bot1, bot2])
        game.draw_board(board)
        
        # evaluate game
        game_not_over = not game.game_over(board)
        
     

def main():
    game.print_guidelines()
    content = []
    for i in range(9):
        content.append(' ')
        
    
    board = game.initialize_board(content) 
    game.draw_board(board)
    mode = 'CPU'
    difficulty = 3
    
    if sys.argv[1] == '1':
        mode = '1P'
    elif sys.argv[1] == '2':
        mode = '2P'
        
    if sys.argv[2] == 'easy':
        difficulty = 1
    elif sys.argv[2] == 'medium':
        difficulty = 2
    
    
    play(board, mode, difficulty)
    
    
    
    
    
    
    
    
    
    
    
    
main()
