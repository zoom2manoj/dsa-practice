from collections import deque, defaultdict
from itertools import accumulate
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        currentSum = 0
        maxSum = 0
        n = len(nums)
        left = 0
        i = 0

        while i < k and i < n:
            currentSum += nums[i]
            mp[nums[i]] += 1

            i += 1


        if len(mp) == k:
            maxSum = currentSum

        for i in range(k, n):
            mp[nums[i]] += 1
            mp[nums[left]] -= 1
            if mp[nums[left]] == 0:
                del mp[nums[left]]
            currentSum += nums[i]
            currentSum -= nums[left]
            if len(mp) == k:
                maxSum = max(maxSum, currentSum)
            left += 1


        return maxSum


nums = [1, 5, 4, 2, 9, 9, 9]
k = 3
solution = Solution()
output = solution.maximumSubarraySum(nums, k)
print(output)
