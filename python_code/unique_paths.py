
from math import factorial


def unique_paths(m: int, n: int) -> int:
    """
    A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

    The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

    How many possible unique paths are there?
    """
    # required downward movements are always = m-1
    # required rightward movements are always = n-1
    downward_movements = m - 1
    right_movements = n - 1

    # total paths is simply the number of permutations of right and down movements,
    # e.g. RRDD, RDRD, RDDR, DRDR, DDRR, DRRD
    # permutations without worrying about repetition (i.e. all characters unique) is ((m + n - 2))!
    # but since we can't permute D with another D to make a unique path, divide by (m-1)! * (n-1)!

    return factorial(downward_movements + right_movements) / (factorial(downward_movements) * factorial(right_movements))
