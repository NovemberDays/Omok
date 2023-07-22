from typing import List, Set, Tuple
import numpy as np


# class Game has OmokBoard object instantiated (aggregation)
class OmokBoard:
    def __init__(self, width: int=15, height: int=15):
        self.width: int = width
        self.height: int = height

    def reset_board(self) -> None:
        self.available_moves: Set[int] = set(range(self.width * self.height))
        self.last_move = -1 # indicates new game
        self.board = np.zeros((self.width, self.height))

    def location_to_move(self, coords: Tuple[int, int]) -> int:
        '''
        Moves in 3 x 3 board; move 5 -> (row, col) = (1, 2)
        0 1 2
        3 4 5
        6 7 8
        '''
        return coords[0] * self.width + coords[1]

    def move_to_location(self, move: int) -> Tuple[int, int]:
        row = move // self.height
        width = move % self.width
        return (row, width)

    # move make_move method to OmokGame class?
    # move players and stuff as well?
    def place_stone(self, coords: Tuple[int, int], player: int) -> None:
        self.board[coords] = player
        self.available_moves.remove(self.location_to_move(coords))
        # return self.check_winner()

    def check_winner(self) -> bool:
        pass
