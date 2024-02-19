from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        n = len(nums)
        output  = n+ 1
        left = 0
        sum = 0
        for i in range(n):
            sum += nums[i]

            while sum >= target or (sum<target and nums[left]<0):
                output = min(output, i + 1 - left)
                sum -= nums[left]
                left += 1

        return output if output != n + 1 else 0


nums = [2,3,1,2,4,3]
nums = [2,-1,2]
# nums = [84,-37,32,40,95]


target = 7
target = 3
# target = 167


solution = Solution()
output = solution.minSubArrayLen(target, nums)
print(output)




