import collections
from typing import List


class Solution:
    def minSubArrayLen(self, K: int, A: List[int]) -> int:
        d = collections.deque([[0, 0]])
        res, cur = float('inf'), 0
        for i, a in enumerate(A):
            cur += a
            while d and cur - d[0][1] >= K:
                res = min(res, i + 1 - d.popleft()[0])
            while d and cur <= d[-1][1]:
                d.pop()
            d.append([i + 1, cur])
        return res if res < float('inf') else -1

nums = [2,3,1,2,4,3]
nums = [2,-1,2]
nums = [84,-37,32,40,95]


target = 7
target = 3
target = 167


solution = Solution()
output = solution.minSubArrayLen(target, nums)
print(output)




