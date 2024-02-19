from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        def searching(nums, target, left, right):

            while left <= right:

                mid = (left + right) // 2
                if nums[mid] == target:
                    return True
                if nums[left] == nums[mid] and nums[mid] == nums[right]:
                    left += 1
                    right -= 1
                    return searching(nums, target, left, right)

                if nums[left] <= nums[mid]:
                    if target >= nums[left] and target < nums[mid]:
                        right = mid - 1
                        return searching(nums, target, left, right)
                    left = mid + 1
                    return searching(nums, target, left, right)

                if nums[mid] <= target and nums[right] >= target:
                    left = mid + 1
                    return searching(nums, target, left, right)
                return searching(nums, target, left, mid - 1)

        n = len(nums)
        left = 0
        right = n - 1
        output = searching(nums, target, left, right)
        print('output', output)
        return output

nums = [1,0,1,1,1]
target = 0
solution = Solution()
solution.search(nums, target)