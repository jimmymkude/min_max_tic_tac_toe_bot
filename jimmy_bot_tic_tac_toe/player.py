
########################################################################
#
# Created by: Jimmy Mkude
# Date Created: 6/15/2017
#
########################################################################


import library as game
import copy


class Bot:
    
    def __init__(self, board):
        self.board = copy.deepcopy(board)
        self.active = False
        self.msg = "My name is Jimmy Bot. Goodluck mate."
        self.score_msg = {
            -1 : "That was sloppy game for me. Try playing me in hard mode.",
            0 : "This is a tie mate.",
            1 : "Anyone's game.",
            2 : "This win is mine."
        }
        self.difficulty_depth = {
            1 : 3,
            2 : 4,
            3 : 8
        }
        
    def activate(self, char='O', difficulty=3):
        self.active = True
        self.char = char
        self.opponent_char = self.inverse_char(char)
        self.difficulty = difficulty
        self.max_depth = self.difficulty_depth[self.difficulty]
        #print("jimmy_bot difficulty: {}".format(self.max_depth))
             
        
        
    def draw_board(self):
    
        print()
        print("Bot board.")
        print("  __  __  __")
        for row in self.board:
            row_str = ""
            for cell in row:
                 row_str += " " + cell + " |"
            print(" |" + row_str)
            print("  __  __  __")
            print()
      
      
    def update_board(self, x, y, char):
        self.board[x][y] = char
        #self.draw_board()
        
    
    def get_possible_moves(self, board):
        moves = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                char = board[i][j]
                if char == ' ':
                    #print((i,j))
                    moves.append((i,j))
        #print()
        return moves
        
    def inverse_char(self, char):
        inverse = 'X'
        if char == 'X':
            inverse = 'O'
        return inverse
        
        
    def explore(self, board, box, char, our_char, depth, max_depth):
        b = copy.deepcopy(board)
        b[box[0]][box[1]] = char
        
        
        (won, winning_char) = game.find_win(b)

        if won:
            # win
            if winning_char == our_char:
                return 2
            # loss
            #print(box)
            #game.draw_board(b)
            return -1
        
        if game.board_full(b):
            # draw  
            return 0
        
        if depth >= max_depth:
            # not determined
            #print("Depth is 3")
            return 1
        
        #print("Depth: " + str(depth))
        #print("Chose: {}".format(box))
        #print("Next Moves: ")
        next_moves = self.get_possible_moves(b)
        # if no more moves then its a draw
        #if not next_moves:
            #return 0
        
        new_depth = depth + 1
        scores = []
        for move in next_moves:
            scores.append(self.explore(b, move, self.inverse_char(char), our_char, new_depth, max_depth))
        
        if char == our_char:
            #print("Max: {}".format(max(scores)))
            return min(scores)
        
        #print("Min: {}".format(min(scores)))
        return max(scores) 
        
        
        
    def select_move(self, moves):
        scores = {}
        options = {}
        b = copy.deepcopy(self.board)
        for move in moves:
            #game.draw_board(b)
            score = self.explore(b, move, self.char, self.char, 1, max_depth=self.max_depth)
            scores[score] = move
            options[move] = score
        
        #print(options)
        selected_score = max(scores)
        selected_move = scores[selected_score]
        
        #print("selected: {}".format(selected_move))
        
        self.msg = self.score_msg[selected_score]
        
        return selected_move
            


    def play(self):
        row = -1
        col = -1
        possible_moves = self.get_possible_moves(self.board)
          
        #print(possible_moves)
        if possible_moves:
            row = possible_moves[0][0]
            col = possible_moves[0][1]
            
            (row, col) = self.select_move(possible_moves)
            
            
        #print(validate_choice(board, row, col))
        
        return (row, col)
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
    
