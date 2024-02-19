from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()
        for index in range(0, len(nums) - 2):
            l = index + 1
            r = len(nums) - 1
            while (l < r):
                val = nums[index] + nums[l] + nums[r]

                if val == 0:
                    result.add(tuple(sorted((nums[index], nums[l], nums[r]))))
                    r -= 1
                    l += 1

                if val > 0:
                    r -= 1
                if val < 0:
                    l += 1

        return result