
from three_sum_closest import *


def test_three_sum_closest():
    input_and_expected = [
        ([-1, 2, 1, -4], 1, 2),
        ([0, 0, 0], 1, 0),
        ([i for i in range(-499, 500)], 3000, 1494),
        ([i for i in range(-499, 500)], -3000, -1494)
    ]
    for nums, target, expected in input_and_expected:
        closest_found = three_sum_closest(nums, target)
        assert closest_found == expected


def test_binary_search_closest():
    input_and_expected = [
        ([1], 500, 1),
        ([1], 2, 1),
        ([1, 2, 3, 4, 5], 1, 1),
        ([i for i in range(-499, 500)], 0, 0),
        ([i for i in range(-499, 500)], -1000, -499),
        ([i for i in range(-499, 500)], 1000, 499),
    ]
    for nums, target, expected in input_and_expected:
        closest_found = binary_search_closest(nums, target)
        assert closest_found == expected
