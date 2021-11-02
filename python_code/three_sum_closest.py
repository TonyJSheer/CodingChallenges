from typing import List


class Node(object):
    def __init__(self, indexes: List[int]) -> None:
        self.indexes = tuple(sorted(indexes))
        self._total = None

    def total(self, numbers: List[int]) -> int:
        return sum(numbers[i] for i in self.indexes)

    def neighbouring_nodes(self, tick: int, max_index: int, searched: set, near_solution: bool):
        nodes = []
        i, j, k = self.indexes
        if 0 <= i + tick < max_index and i + tick != j and i + tick != k:
            node = Node([i + tick, j, k])
            if node not in searched:
                nodes.append(node)
        if 0 <= j + tick < max_index and i != j + tick and j + tick != k:
            node = Node([i, j + tick, k])
            if node not in searched:
                nodes.append(node)
        if 0 <= k + tick < max_index and i != k + tick and j != k + tick:
            node = Node([i, j, k + tick])
            if node not in searched:
                nodes.append(node)

        if not near_solution:
            return nodes[:1]
        return nodes

    def __eq__(self, o: object) -> bool:
        return self.indexes == o.indexes

    def __hash__(self) -> int:
        return self.indexes.__hash__()

    def __str__(self) -> str:
        return self.indexes.__str__()

    def __repr__(self) -> str:
        return self.indexes.__repr__()


def three_sum_closest_search(nums: List[int], target: int) -> int:
    nums = sorted(nums)
    max_index = len(nums)
    current = Node([0, 1, 2])
    searched = {current}
    near_solution = False
    to_search = set(current.neighbouring_nodes(
        1, max_index, searched, near_solution))

    closest_sum = current.total(nums)
    closest_distance = abs(closest_sum - target)
    # need to use greedy heuristic to get 'near' solution (distance changes from - to +)

    # Search method below will search one step up to increase total, or one step down to decrease
    while to_search:
        current = to_search.pop()
        searched.add(current)

        current_sum = current.total(nums)

        if not near_solution and current_sum > target:
            near_solution = True
            searched = set()

        if current_sum == target:
            return current_sum
        elif current_sum < target:
            to_search.update(current.neighbouring_nodes(
                1, max_index, searched, near_solution))
            # search up
        elif current_sum > target:
            # search down
            to_search.update(current.neighbouring_nodes(
                -1, max_index, searched, near_solution))

        current_distance = abs(current_sum - target)
        if current_distance < closest_distance:
            closest_distance, closest_sum = current_distance, current_sum

    return closest_sum


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
