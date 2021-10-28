
from three_sum import *


def test_three_sum():
    string_and_expected = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([], []),
        ([0], []),
    ]
    for nums, triples in string_and_expected:
        found_triples = three_sum(nums)
        assert sorted(found_triples) == sorted(triples)
