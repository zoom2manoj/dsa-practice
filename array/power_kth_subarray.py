from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return []
        app = [-1] * (len(nums) - k + 1)
        count = 0
        for i in range(1, k):
            if nums[i] == nums[i - 1] + 1:
                count += 1
        # print(count)
        app[0] = nums[k - 1] if (count == k - 1) else -1
        # print(app)
        for i in range(1, len(nums) - k+1):
            if nums[i] == nums[i - 1] + 1:
                count -= 1
            if nums[i + k - 1] == nums[i + k - 2] + 1:
                count += 1
            app[i] = nums[i + k - 1] if (count == k - 1) else -1

        return app


nums = [1, 2, 3, 4, 3, 2, 5]
k = 3

# nums = [1, 4]
# k = 1
solution = Solution()
output = solution.resultsArray(nums, k)
print(output)

"""
Example 1:

Input: nums = [1,2,3,4,3,2,5], k = 3

Output: [3,4,-1,-1,-1]

Explanation:

There are 5 subarrays of nums of size 3:

[1, 2, 3] with the maximum element 3.
[2, 3, 4] with the maximum element 4.
[3, 4, 3] whose elements are not consecutive.
[4, 3, 2] whose elements are not sorted.
[3, 2, 5] whose elements are not consecutive.
Example 2:

Input: nums = [2,2,2,2,2], k = 4

Output: [-1,-1]

Example 3:

Input: nums = [3,2,3,2,3,2], k = 2

Output: [-1,3,-1,3,-1]
"""
