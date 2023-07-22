from typing import List, Set, Tuple
import numpy as np


# class Game has OmokBoard object instantiated (aggregation)
class OmokBoard:
    def __init__(self, width: int=15, height: int=15):
        self.width: int = width
        self.height: int = height
        self.players: List[int] = [1, 2]

    def reset_board(self, start_player: int=0) -> None:
        self.current_player: int = self.players[start_player]
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
    def make_move(self, coords: Tuple[int, int]) -> bool:
        index = (self.players.index(self.current_player) + 1) % 2
        self.current_player = self.players[index]
        if self.is_appropriate(coords):
            self.board[coords] = self.current_player
            self.available_moves.remove(self.location_to_move(coords))
        return self.check_winner()

    def is_appropriate(self, coords: Tuple[int, int]) -> bool:
        '''
        if move is in self.available_moves
        if move is inside the board
        maybe Renju rule as well?
        '''
        return True

    def check_winner(self) -> bool:
        pass


class OmokGame:
    def __init__(self, board: OmokBoard):
        self.board: OmokBoard = board


o = OmokBoard(3, 3)
o.reset_board()
o.make_move((2, 0))
print(o.board)
print(o.available_moves)
