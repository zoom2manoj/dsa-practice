# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index in range(1, len(nums)):
            current = nums[index]
            if target - current in nums and index != nums.index(target - current):
                return [nums.index(target - current), index]

nums = [2,7,11,15]
target = 9
solution = Solution()
result = solution.twoSum(nums, target)

print(result)
