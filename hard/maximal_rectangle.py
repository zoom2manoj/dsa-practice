from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        print(matrix)
        m = len(matrix)
        n = len(matrix[0])
        print(m, n)
        for i in range(m):
            for j in range(n):
                print(i, j, matrix[i][j], matrix[m-1-i][n-1-j], matrix[i][n-j-1], matrix[m-i-1][j])


        return 'yes'


matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]

solution = Solution()
resp = solution.maximalRectangle(matrix)
print(resp)
