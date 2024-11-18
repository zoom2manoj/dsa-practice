from collections import deque
from itertools import accumulate
from typing import List
from math import inf

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        if len(nums) == 1 and k == nums[0]:
            return 1
        d = deque([[0, 0]])
        sum = 0
        res = float('inf')
        for i, x in enumerate(nums):
            sum += x
            while d and (sum - d[0][1]) >= k:
                res = min(res, i + 1 - d.popleft()[0])

            while d and sum <= d[-1][1]:
                d.pop()

            d.append([i + 1, sum])

        return res if res < float('inf') else -1


solution = Solution()
nums = [2, -1, 2]
k = 3


nums = [48,99,37,4,-31]
k = 140

nums = [17,85,93,-45,-21]
k = 150

output = solution.shortestSubarray(nums, k)
print(output)


"""
Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3

"""