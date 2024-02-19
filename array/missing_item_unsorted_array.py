from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        missing = n
        for x in range(n):
            # print(x)
            print(missing, x, nums[x], x ^ nums[x])
            missing^=x^nums[x]
            print(missing, x, nums[x],  x^nums[x])
            print('============================')
        return missing



nums  = [3, 0 , 2]
solution = Solution()
output = solution.missingNumber(nums)
print(output)



