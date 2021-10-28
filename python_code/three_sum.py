
from typing import List


from collections import defaultdict


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]],
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.
    """
    numbers_to_indexes = defaultdict(lambda: [])
    for i, num in enumerate(nums):
        numbers_to_indexes[num].append(i)

    # A basic strategy, for every pair check for the third unique number to make them add to 0
    triples = set()
    for i, first_num in enumerate(nums):
        for j, second_num in enumerate(nums[i + 1:]):
            j = j + i + 1
            required_number = 0 - first_num - second_num
            if required_number in nums[j + 1:]:  # Only look for required num

                triples.add(
                    tuple(sorted((first_num, second_num, required_number))))

    return [list(triple) for triple in triples]
