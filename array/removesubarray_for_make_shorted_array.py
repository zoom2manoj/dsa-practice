from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        length = len(arr)

        # Initialize two pointers for the beginning and end of the array
        left = 0
        right = length - 1

        # Move the left pointer to the right as long as the subarray is non-decreasing
        while left + 1 < length and arr[left] <= arr[left + 1]:
            left += 1

        # Move the right pointer to the left as long as the subarray is non-decreasing
        while right - 1 >= 0 and arr[right - 1] <= arr[right]:
            right -= 1

        # If the whole array is already non-decreasing, return 0
        if left >= right:
            return 0

        # Calculate the length of the remaining array to be removed
        min_length_to_remove = min(length - left - 1, right)

        # Reinitialize the right pointer for the next loop
        new_right = right

        # Check for the shortest subarray from the left side to the midpoint
        for new_left in range(left + 1):
            # Increment the right pointer until the elements on both sides are non-decreasing
            while new_right < length and arr[new_right] < arr[new_left]:
                new_right += 1
            # Update the minimum length if a shorter subarray is found
            min_length_to_remove = min(min_length_to_remove, new_right - new_left - 1)

        # Return the minimum length of the subarray to remove to make array non-decreasing
        return min_length_to_remove


arr = [1, 2, 3, 10, 4, 2, 3, 5]
arr = [5,4,3,2,1]

solution = Solution()
resp = solution.findLengthOfShortestSubarray(arr)
print(resp)

"""
Example 1:

Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].
Example 2:

Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
Example 3:

Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.
 
"""
