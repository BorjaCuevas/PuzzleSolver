""" Read and Write files """


def get_puzzle_file(pieces_file):
    """
    Get the pieces array from a file
    @param pieces_file: path file
    @return: array of pieces
    """
    try:
        f = open(pieces_file, "r")
        data = f.read().splitlines()
        data = data[1:]
        return data
    except IndexError:
        print(f"[FILE ERROR] There is a problem with {pieces_file}.")


def write_solution_file():
    """
    Write the solution in txt
    @return:
    """
    pass
