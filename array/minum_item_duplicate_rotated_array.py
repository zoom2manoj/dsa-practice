from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            print(left, right, mid)

            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return nums[mid]

nums = [1,1]
nums =  [1,3,5]

# nums =  [ 3, 4, 5, 6,7, 8, 9, 9, 1, 2]

solution = Solution()
output = solution.findMin(nums)
print(output)