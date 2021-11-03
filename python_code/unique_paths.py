

def unique_paths(m: int, n: int) -> int:
    """
    A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

    The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

    How many possible unique paths are there?
    """
    # required downward movements are always = m-1
    # required rightward movements are always = n-1
