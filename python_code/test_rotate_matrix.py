
from rotate_matrix import *


def test_rotate_matrix():
    matrices_to_test_and_result = (
        # 2 x 2 input
        ([[1, 2],
         [3, 4]],
         # 2 x 2 output
         [[3, 1],
          [4, 2]]),

        # 3 x 3 input
        ([[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]],
         # 3 x 3 output
         [[7, 4, 1],
          [8, 5, 2],
          [9, 6, 3]]),

        # 4 x 4 input
        ([[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]],
         # 4 x 4 output
         [[13, 9, 5, 1],
          [14, 10, 6, 2],
          [15, 11, 7, 3],
          [16, 12, 8, 4]]
         ),
    )
    for matrix, expected in matrices_to_test_and_result:
        assert rotate_matrix(matrix) == expected


def test_check_rotations():
    matrices_to_test_and_result = (
        (
            [[0, 1], [1, 0]],
            [[1, 0], [0, 1]],
            True
        ),
        (
            [[0, 1], [1, 1]],
            [[1, 0], [0, 1]],
            False
        ),
        (
            [[0, 0, 0], [0, 1, 0], [1, 1, 1]],
            [[1, 1, 1], [0, 1, 0], [0, 0, 0]],
            True
        ),
    )

    for matrix, target, expected in matrices_to_test_and_result:
        result = check_rotations(matrix, target)
        assert result == expected
