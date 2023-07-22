from typing import Tuple
from game_board import OmokBoard


class RenjuRule:
    def __init__(self, board: OmokBoard):
        self.board: OmokBoard = board
        print(self.board.board)

    def is_appropriate(self, coords: Tuple[int, int]):
        '''
        if move is in self.available_moves
        if move is inside the board
        maybe Renju rule as well?
        '''
        print(self.board.board)
        return True
