from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:


        left = 0
        right = len(nums)-1

        while left <=right:
            mid = (left+right)//2
            if nums[mid]<nums[right]:
                left = mid+1
            elif nums[mid]>nums[right]:
                right -= 1
            else:
                left+=1





        return mid


nums = [1,2,3,1]
nums = [1,2,1,3,5,6,4]

solution = Solution()
output = solution.findPeakElement(nums)
print(output)