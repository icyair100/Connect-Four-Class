#
# ps9pr4.py  (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps9pr3 import *

class AIPlayer(Player):

    def __init__(self, checker, tiebreak, lookahead):
        """ Constructs a new AIPlayer object"""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self): 
        """ returns a string representing an AIPlayer"""
        return('Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')')

    def max_score_column(self, scores):

        max_scores = []
        for i in range(len(scores)):
            if scores[i] == max(scores):
                max_scores += [i]

        if self.tiebreak == 'LEFT':
            return max_scores[0]
        elif self.tiebreak == 'RIGHT':
            return max_scores[-1]
        else:
            return random.choice(max_scores)

    def scores_for(self, board):
        scores = [0]*len(range(board.width))

        for col in range(board.width):
            if board.can_add_to(col) == False:
                scores[col] = -1
            elif board.is_win_for(self.checker) == True:
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                otherscore = opponent.scores_for(board)
                if max(otherscore) == 0:
                    scores[col] = 100
                elif max(otherscore) == 100:
                    scores[col] = 0
                elif max(otherscore) == 50:
                    scores[col] = 50

                board.remove_checker(col)
        return scores
    
    def next_move(self, board):

        self.num_moves += 1

        scores = self.scores_for(board)
        return self.max_score_column(scores)


        








        
    
