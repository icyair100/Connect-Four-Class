#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below

class Player:

    def __init__(self, checker):
        """a constructor for Player objects"""
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """returns a string representing a Player object."""
        
        return 'Player ' + self.checker

    def opponent_checker(self):
        """returns a one-character string representing the
        checker of the Player object’s opponent."""
        if self.checker == 'X':
            return 'O'
        if self.checker == 'O':
            return 'X'
    def next_move(self, board):
        """accepts a Board object as a parameter and returns
        the column where the player wants to make the next move"""
        self.num_moves += 1

        while True:
            col_input = input('Enter a column: ')
            if col_input in '0123456':
                num = int(col_input)
                if board.can_add_to(num):
                    return num
            print('Try again')






        
        
