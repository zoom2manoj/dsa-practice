from typing import List

"""
Core concept for this problem
height is having 0 value by default and update value for row item iteration if row item is not 0. and in future for another row iteration, if row item is coming 0 then hieght value is update from 0.
based on height, we can calculate, weight of height item and update max value in answer and if it's coming zero then skip

"""
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or len(matrix) == 0:
            return 0
        print(matrix)
        m = len(matrix)
        n = len(matrix[0])
        print(m, n)
        height = [0] * n
        # print(height)
        ans = 0
        for i in range(m):
            for j in range(n):
                # print(i, j, matrix[i][j], matrix[m-1-i][n-1-j], matrix[i][n-j-1], matrix[m-i-1][j])
                height[j] = 0 if matrix[i][j] == '0' else height[j] + 1
            print(i, height)
            ans = max(ans, self.calculate_area(height))

        return ans

    def calculate_area(self, height):

        ans = 0
        stack = []
        for i in range(len(height) + 1):
            while stack and (i == len(height) or height[stack[-1]] > height[i]):
                h = height[stack.pop()]
                w = i - stack[-1] - 1 if stack else i

                ans = max(ans, h * w)
                print(i, h, w, height, ans)
            stack.append(i)
        print('========')
        return ans


matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]

solution = Solution()
resp = solution.maximalRectangle(matrix)
print(resp)




