

def rotate_matrix(matrix: list):
    matrix_size = len(matrix)

    # make matrix of zeros
    new_matrix = [[0 for _ in range(matrix_size)]
                  for _ in range(matrix_size)]

    for i, row in enumerate(matrix):
        for j, entry in enumerate(row):
            new_matrix[j][matrix_size - 1 - i] = entry
    return new_matrix


def check_rotations(matrix: list, target: list):
    if matrix == target:
        return True
    for _ in range(3):
        matrix = rotate_matrix(matrix)
        if matrix == target:
            return True
    return False
