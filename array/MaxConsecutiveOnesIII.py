from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1

        return r - l + 1
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 2
k = 3

solution = Solution()
res = solution.longestOnes(nums, k)

print(res)
