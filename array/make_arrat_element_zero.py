from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        n = len(nums)
        valid_count = 0

        # Function to simulate the process starting at a given position `curr` and direction
        def simulate(curr, direction):
            nums_copy = nums[:]
            position = curr
            move = direction

            while 0 <= position < n:
                if nums_copy[position] == 0:
                    # If the value is zero, just move in the current direction
                    position += move
                else:
                    # If the value is greater than zero, decrement it and reverse direction
                    nums_copy[position] -= 1
                    move = -move  # Reverse direction
                    position += move

            # Check if all elements have become 0
            return all(x == 0 for x in nums_copy)

        # Try all positions where nums[curr] == 0
        for curr in range(n):
            if nums[curr] == 0:
                # Try both directions (left: -1, right: 1)
                if simulate(curr, 1):
                    valid_count += 1
                if simulate(curr, -1):
                    valid_count+=1

        return valid_count







nums = [1, 0, 2, 0, 3]
# nums = [2,3,4,0,4,1,0]
# nums = [16,13,10,0,0,0,10,6,7,8,7]
solution = Solution()
ouput = solution.countValidSelections(nums)
print(ouput)
