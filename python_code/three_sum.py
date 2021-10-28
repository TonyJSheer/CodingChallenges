
from collections import defaultdict
from typing import List, Set


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
    for first_num, indexes in numbers_to_indexes.items():
        # Check for triples, i.e. three zeros
        if 3 * first_num == 0 and len(indexes) > 2:
            triples.add(
                tuple(sorted((first_num, first_num, first_num))))

        # Check for solutions involving this number as a double
        if len(indexes) > 1:
            required_number = 0 - first_num - first_num
            if required_number in numbers_to_indexes and required_number != first_num:
                triples.add(
                    tuple(sorted((first_num, first_num, required_number))))

        # Go through pairs
        for second_num in numbers_to_indexes.keys():
            if first_num != second_num:  # already handled case of 2 or 3 copies of num
                required_number = 0 - first_num - second_num

                # already handled 2x num case so will exclude here
                if required_number in numbers_to_indexes and required_number not in (first_num, second_num):
                    triples.add(
                        tuple(sorted((first_num, second_num, required_number))))

    return [list(triple) for triple in triples]
