from unique_paths import *


def test_unique_paths():
    size_and_paths = [
        (3, 2, 3),
        (7, 3, 28),
        (3, 3, 6),
        (3, 7, 28),
    ]

    for m, n, expected_paths in size_and_paths:
        total_paths = unique_paths(m, n)
        assert expected_paths == total_paths
