from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        output = nums[0]
        left = 0
        right = len(nums)-1
        while left<=right:
            print(left, right)
            mid = (left+right)//2

            if output>nums[mid]:
                output = nums[mid]

            if nums[mid]<nums[left]:
                print('rotated')
                left = mid + 1
            else:
                if output>=nums[left] and output<nums[mid]:
                    right = mid-1
                else:
                    left +=1


        return output


nums = [3,4,5,1,2]
solution = Solution()
result = solution.findMin(nums)
print('result: ', result)

