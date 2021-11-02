from typing import List


def three_sum_closest(nums: List[int], target: int) -> int:
    """
    Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

    Return the sum of the three integers.

    You may assume that each input would have exactly one solution.
    """
    # possible approach: for each pair, find third such that sum is closest (third can basically be binary search)
    # possible approach: greedy algo? find closest match for first number, then find closest match for pair.
    sorted_nums = sorted(nums)

    closest_sum = sum(sorted_nums[:3])
    for i, num1 in enumerate(sorted_nums):
        for j, num2 in enumerate(sorted_nums[i + 1:]):
            num3 = binary_search_closest(
                sorted_nums[i + j + 2:], target - num1 - num2)
            if num3 is None:
                continue
            if abs(num1 + num2 + num3 - target) < abs(closest_sum - target):
                closest_sum = num1 + num2 + num3
            if 3 * num1 > target:
                return closest_sum
            if num1 + 2 * num2 > target:
                break

    return closest_sum


def binary_search_closest(nums: List[int], target: int) -> int:
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return nums[0]

    i = int(len(nums)/2)
    num = nums[i]
    if num == target:
        return num

    # if
    if num < target:
        closer_candidate = binary_search_closest(nums[i + 1:], target)

    if num > target:
        closer_candidate = binary_search_closest(nums[:i], target)

    if closer_candidate is not None and abs(closer_candidate - target) < abs(num - target):
        return closer_candidate
    else:
        return num
