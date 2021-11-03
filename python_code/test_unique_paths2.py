from unique_paths2 import *


# def test_unique_paths2():
#     grid_and_paths = [
#         ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2),
#         ([[0, 0, 0], [0, 1, 0], [0, 1, 0]], 1),
#         ([[0, 0, 0], [0, 1, 1], [1, 1, 0]], 0),
#         ([[0, 1], [0, 0]], 1),
#     ]

#     for grid, expected_paths in grid_and_paths:
#         total_paths = unique_paths2(grid)
#         assert expected_paths == total_paths

def test_unique_paths2_obstacles():
    grid_and_paths = [
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2),
        ([[0, 0, 0], [0, 1, 0], [0, 1, 0]], 1),
        ([[0, 0, 0], [0, 1, 1], [1, 1, 0]], 0),
        ([[0, 1], [0, 0]], 1),
    ]

    for grid, expected_paths in grid_and_paths:
        total_paths = unique_paths2_obstacles(grid)
        assert expected_paths == total_paths
