import copy
import random
from board import Board

class Ai:

    def __init__(self, level=1, player=2):
        self.level = level
        self.player = player

    def rnd(self, board:Board):
        empty_squares = board.get_empty_squares()
        idx = random.randrange(0, len(empty_squares))
        return empty_squares[idx] # (row, col)
    
    def minimax(self, board:Board, maximising):
        # terminal case
        case = board.final_state(None)

        # case 1: player 1 wins
        if case == 1:
            return 1, None
        
        # case 2: player 2 wins
        if case == 2:
            return -1, None
        
        # case 3: draw
        if board.is_full():
            return 0, None
        
        if maximising:
            max_eval = -100
            best_move = None
            empty_squares = board.get_empty_squares()
            for (row, col) in empty_squares:
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, 1)
                eval = self.minimax(temp_board, False)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)
                    
            return max_eval, best_move

        elif not maximising:
            min_eval = 100
            best_move = None
            empty_squares = board.get_empty_squares()
            for (row, col) in empty_squares:
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, self.player)
                eval = self.minimax(temp_board, True)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)

            return min_eval, best_move

    
    def eval(self, main_board):
        if self.level == 0:
            # random choice
            eval = 'random'
            move = self.rnd(main_board)
        else:
            # minimax algo choice
            eval, move = self.minimax(main_board, False)
        return move # (row, col)