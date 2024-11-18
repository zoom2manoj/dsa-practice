from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return nums
        current_item = nums[0]
        count = 0
        n = len(nums)
        for i in range(1, len(nums)):
            item = nums[i]
            if item>current_item:
                current_item = item
                count+=1
                nums[count], nums[i] = nums[i], nums[count]
        print(nums)
        print(count)
        nums = nums[:count+1]
        print(nums)





nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums = [1,1,2]
solution = Solution()
solution.removeDuplicates(nums)