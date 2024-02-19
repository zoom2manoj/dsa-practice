from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        def possible(mid, n):
            ans = 0
            for x in range(n):

                if matrix[x][0] > mid:
                    return ans >= k

                if matrix[x][n - 1] <= mid:
                    ans += n
                    continue

                greaterthan = 0
                jump = n // 2

                while jump >= 1:
                    while greaterthan + jump < n and matrix[x][greaterthan + jump] <= mid:
                        greaterthan += jump
                    jump //= 2
                ans += greaterthan + 1

            return ans >= k

        n = len(matrix[0])

        low = matrix[0][0]
        hi = matrix[n - 1][n - 1]
        # print(low, hi)
        while low <= hi:
            mid = (low + hi) // 2
            # print(mid)

            # if mid
            if not possible(mid, n):
                low = mid + 1
            else:
                hi = mid - 1

        return low


matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8

solution = Solution()
resp = solution.kthSmallest(matrix, k)
print(resp)