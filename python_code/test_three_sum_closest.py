
from three_sum_closest import *


def test_three_sum_closest_search():
    input_and_expected = [
        ([-1, 2, 1, -4], 1, 2),
        ([0, 0, 0], 1, 0),
        ([i for i in range(-499, 500)], 3000, 1494),
        ([i for i in range(-499, 500)], -3000, -1494),
        ([1, 6, 9, 14, 16, 70], 81, 80),
        ([-100, -91, -91, -89, -83, -82, -81, -79], -275, -274),
        ([87, 6, -100, -19, 10, -8, -58, 56, 14, -1, -42, -45, -17, 10, 20, -4, 13, -17, 0,
          11, -44, 65, 74, -48, 30, -91, 13, -53, 76, -69, -19, -
          69, 16, 78, -56, 27, 41, 67, -79, -2, 30, -13, -60,
          39, 95, 64, -12, 45, -52, 45, -44, 73, 97, 100, -19, -
          16, -26, 58, -61, 53, 70, 1, -83, 11, -35, -7, 61, 30,
          17, 98, 29, 52, 75, -73, -73, -23, -75, 91, 3, -
          57, 91, 50, 42, 74, -7, 62, 17, -91, 55, 94, -21, -36, 73,
          19, -61, -82, 73, 1, -10, -40, 11, 54, -81, 20, 40, -
          29, 96, 89, 57, 10, -16, -34, -56, 69, 76, 49, 76, 82,
          80, 58, -47, 12, 17, 77, -75, -24, 11, -45, 60, 65, 55, -89, 49, -19, 4], -275, -274)
    ]
    for nums, target, expected in input_and_expected:
        closest_found = three_sum_closest_search(nums, target)
        assert closest_found == expected


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
