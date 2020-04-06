""" Start and end of the puzzle maker """

from Core import file_manager as fm
from Core.solutions import Solutions
from Core.piece import Piece


class Front:

    def __init__(self, pieces_file):
        self.pieces_from_file = fm.get_puzzle_file(pieces_file)
        self.puzzle_pieces = {}
        self.solutions = [0][0]
        self.puzzle_pieces_from_file()
        self.get_solutions()
        self.write_solutions()

    def puzzle_pieces_from_file(self):
        key = 1
        for piece in self.pieces_from_file:
            self.puzzle_pieces[key] = Piece(key, *tuple(map(int, piece.split(' '))))
            key += 1

    def get_solutions(self):
        solution=Solutions(self.puzzle_pieces)
        solution.resolve()

    def write_solutions(self):
        pass


if __name__ == "__main__":
    main = Front("../Pieces/4x4.txt")
