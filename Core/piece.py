""" Piece class """


class Piece:

    def __init__(self, key, sideA, sideB, sideC, sideD):
        self.key = key
        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC
        self.sideD = sideD

    def rotate(self):
        """
        Rotate the piece to make easy to look for restrictions
        @return: none
        """
        pass
