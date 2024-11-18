from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        delta = [0] * (n + 1)  # One extra for handling the right boundary

        for li, ri in queries:
            delta[li] -= 1  # Decrement starting at li
            if ri + 1 < n:
                delta[ri + 1] += 1  # Increment stopping at ri + 1

        current_decrement = 0
        for i in range(n):
            current_decrement += delta[i]
            if nums[i] != 0:
                if nums[i]+current_decrement<0:
                    nums[i] = 0
                else:
                    nums[i] += current_decrement

        return all(x == 0 for x in nums)


nums = [1, 0, 1]
queries = [[0, 2]]


nums = [4,3,2,1]
queries = [[1,3],[0,2]]

# nums = [2]
# queries = [[0,0],[0,0]]

# nums = [1, 0, 1]
# queries = [[0, 2]]



# nums = [2]
# queries = [[0,0],[0,0], [0,0]]
# queries = [[0,0],[0,0]]




solution = Solution()
output = solution.isZeroArray(nums, queries)
print(output)