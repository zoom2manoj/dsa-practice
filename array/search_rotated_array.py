from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if nums is None or len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        print(nums)

        left = 0
        right = len(nums)-1



        while left<right:
            mid = left +(right - left) // 2
            if nums[mid]>nums[right]:
                left = mid+1
            else:
                right = mid

        print('left right', left, right)

        pivot = left
        left =0
        right = len(nums)-1
        print(left, right, '=====')

        if nums[pivot]<=target<=nums[right]:
            left =pivot
        else:
            right = pivot

        print(left, right, '=====')

        while left<=right:

            mid = left + (right-left)//2

            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                left = mid+1
            elif target<nums[mid]:
                right = mid-1

        return -1




nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

nums = [1,3]
target = 2

solution = Solution()
data = solution.search(nums, target)
print('result ', data)