""" Create restrictions for the pieces in determinate places"""

from Core.piece import Piece


class Restrictions(Piece):

    def __init__(self, neighs):
        Piece.__init__(self, 0, 0, 0, 0, 0)
        self.neighs = neighs

    def create_restrictions(self):
        pass
