"""
Example 1:

Input: nums = [-2,5,-1], lower = -2, upper = 2
Output: 3
Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.



Example 2:

Input: nums = [0], lower = 0, upper = 0
Output: 1

"""
from bisect import bisect_left
from itertools import accumulate
from typing import List

class BinaryIndexedTree:
    # Initialize the Binary Indexed Tree with `size` elements.
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    # Update the tree by adding a value `val` to the element at index `index`.
    def update(self, index, val):
        # Propagate the update up the tree.
        while index <= self.size:
            self.tree[index] += val
            index += index & -index

    # Query the cumulative sum from index 1 to `index`.
    def query(self, index):
        sum_ = 0
        # Aggregate the sums.
        while index > 0:
            sum_ += self.tree[index]
            index -= index & -index
        return sum_

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # Compute the prefix sums of the input array `nums`.
        prefix_sums = list(accumulate(nums, initial=0))
        # Flatten and sort the unique sums for tree construction.
        sorted_arr = sorted(set(x for sum_ in prefix_sums for x in (sum_, sum_ - lower, sum_ - upper)))
        # Initialize the Binary Indexed Tree with the length of the sorted unique sums.
        tree = BinaryIndexedTree(len(sorted_arr))
        count = 0  # Initialize the count of ranges.

        # Iterate over the prefix sums.
        for sum_ in prefix_sums:
            # Find the indices for the current sum minus the upper and lower bounds.
            # +1 because our BIT is 1-indexed.
            left = bisect_left(sorted_arr, sum_ - upper) + 1
            right = bisect_left(sorted_arr, sum_ - lower) + 1
            # Calculate the number of sums in the range [lower, upper].
            count += tree.query(right) - tree.query(left - 1)
            # Update the BIT for the current prefix sum.
            tree.update(bisect_left(sorted_arr, sum_) + 1, 1)

        # Return the total count of sums in the range.
        return count



nums = [-2,5,-1]
lower = -2
upper = 2

solution = Solution()
res = solution.countRangeSum(nums, lower, upper)
print(res)


