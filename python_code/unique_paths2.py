
from typing import List
from math import factorial


def unique_paths(m: int, n: int) -> int:
    downward_movements = m - 1
    right_movements = n - 1

    return factorial(downward_movements + right_movements) / (factorial(downward_movements) * factorial(right_movements))


def unique_paths2(obstacleGrid: List[List[int]]) -> int:
    """
    DEPRECATED, DOESN'T WORK FOR SOME BLOCKERS
    A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

    The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

    Now consider if some obstacles are added to the grids. How many unique paths would there be?

    An obstacle and space is marked as 1 and 0 respectively in the grid.

    e.g.:  obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]], Output: 2

    """
    # two possible approaches,
    # Firstly, try to generate all possible paths using a dynamic programming style approach (see unique_paths2_dp)
    # Secondly, calculate all paths, then calculate and add up all paths_to_obstacle * obstacle_to_goal
    # The second option seems easier to implement
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    total_paths = unique_paths(m, n)

    for i, row in enumerate(obstacleGrid):
        for j, square in enumerate(row):
            if square:
                paths_to_obstacle = unique_paths(i + 1, j + 1)
                paths_to_goal = unique_paths(m - i, n - j)
                total_paths -= (paths_to_goal * paths_to_obstacle)

    return total_paths


def unique_paths2_obstacles(obstacleGrid: List[List[int]]) -> int:
    """
    Instead of the above approach,

    """
