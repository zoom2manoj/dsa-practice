from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # start, end = -1, -1
        # for index in range(len(nums)):
        #     if target == nums[index]:
        #         if start==-1:
        #             start = index
        #         if start >-1:
        #             end = index

        # return [start, end]

        f = self.first(nums, target)
        s  = self.last(nums, target)
        return [f, s]

    def first(self, nums, target):
        left = 0
        right = len(nums) - 1
        starting_index = -1
        while left <= right:
            print('left right', left, right)
            mid = left + (right - left) // 2
            if nums[mid] == target:
                starting_index = mid
                right = mid-1
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid + 1

        print('first start', starting_index)
        return starting_index



    def last(self, nums, target):
        left = 0
        right = len(nums) - 1
        starting_index = -1
        ending_index = -1
        while left <= right:
            print('left right', left, right)
            mid = left + (right - left) // 2
            if nums[mid] == target:
                ending_index = mid
                left =mid+1
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid + 1

        print('end ',  ending_index)
        return ending_index


nums = [5,7,7,8,8,10]
target = 8

# nums = [1]
# target = 1

solution = Solution()
res = solution.searchRange(nums, target)
print(res)
