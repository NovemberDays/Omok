from typing import List, Tuple
from game_board import OmokBoard
from game_rule import RenjuRule


class OmokGame:
    def __init__(self, board: OmokBoard, rule: RenjuRule):
        self.board: OmokBoard = board
        self.rule: RenjuRule = rule
        self.players: List[int] = [1, 2]

    def reset_game(self, start_player: int=0) -> None:
        self.current_player: int = self.players[start_player]
        self.board.reset_board()

    def make_move(self, coords: Tuple[int, int]) -> bool:
        index = (self.players.index(self.current_player) + 1) % 2
        self.current_player = self.players[index]
        if self.rule.is_appropriate():
            self.board.place_stone(coords, index)
        return self.rule.check_winner()


o = OmokBoard(3, 3)
o.reset_board()
o.make_move((2, 0))
print(o.board)
print(o.available_moves)
