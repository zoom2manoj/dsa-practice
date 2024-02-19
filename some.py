from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        output = []
        # Loop for all the elements in the array
        for i in range(len(nums)):
            # If the current element is equal to the next element, we skip
            if i < len(nums) - 2 and nums[i] == nums[i + 1]:
                continue
            # We will update the array in place
            output.append( nums[i])
            count += 1

        print(count)
        return count, output


nums = [1,1,2]

solution = Solution()
print(nums)
count, out = solution.removeDuplicates(nums);
print(nums)
print(out)
