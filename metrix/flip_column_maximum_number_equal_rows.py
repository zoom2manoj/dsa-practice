from collections import Counter
from typing import List


class Solution:

    def print(self, mat):
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                print(mat[i][j], end=" ")
            print("")

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        self.print(matrix)
        count = Counter()
        for row in matrix:
            if row[0]==0:
                count[tuple(row)]+=1

            else:
                count[tuple([x ^ 1 for x in row])] += 1
        print(count, count.values())


        return max(count.values())



matrix = [[0,0,0],[0,0,1],[1,1,0]]
solution = Solution()
output = solution.maxEqualRowsAfterFlips(matrix)
print(output)