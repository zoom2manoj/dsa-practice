"""
Example 1:

Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
Example 2:

Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).

"""
from typing import List

from bisect import bisect_left
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        print(nums)
        count = 0
        for index, item in enumerate(nums):
            left = bisect_left(nums, lower-item, lo=index+1)
            right = bisect_left(nums, upper-item+1, lo=index + 1)
            count+=right-left
        return count


# nums = [0, 1, 7, 4, 4, 5]
# lower = 3
# upper = 6


nums = [1,7,9,2,5]
lower = 11
upper = 11

s = Solution()
resp = s.countFairPairs(nums, lower, upper)
print(resp)
