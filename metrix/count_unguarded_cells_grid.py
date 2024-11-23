from itertools import pairwise
from typing import List


class Solution:
    def print(self, mat):
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                print(mat[i][j], end=" ")
                if mat[i][j]==0:
                    count+=1
            print("")
        return count

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # mat = [[0 for i in range(n)] for j in range(m)]
        # # print(mat)
        # for i in walls:
        #     mat[i[0]][i[1]] = 1
        # # print(mat)
        #
        # for i in guards:
        #     mat[i[0]][i[1]] = 2
        #     # this is for top to bottom
        #     for x in range(i[0] + 1, m):
        #         # print("x in ", x)
        #
        #         if mat[x][i[1]] != 1:
        #             mat[x][i[1]] = 4
        #         else:
        #             break
        #
        #     # bottom to op
        #     for x in range(i[0]-1, -1, -1):
        #         # print("x in ", x)
        #         if mat[x][i[1]] != 1:
        #             mat[x][i[1]] = 4
        #         else:
        #             break
        #     # left to right
        #     for x in range(i[1]+1, n):
        #         # print("x in ", x)
        #         if mat[i[0]][x] != 1:
        #             mat[i[0]][x] = 4
        #         else:
        #             break
        #     # right to left
        #     for x in range(i[1] -1, -1, -1):
        #         # print("x in ", x)
        #         if mat[i[0]][x] != 1:
        #             mat[i[0]][x] = 4
        #         else:
        #             break
        #
        # count = 0
        # for i in range(len(mat)):
        #     for j in range(len(mat[i])):
        #         # print(mat[i][j], end=" ")
        #         if mat[i][j] == 0:
        #             count += 1
        #     # print("")
        #
        # return count

        g = [[0] * n for _ in range(m)]
        for i, j in guards:
            g[i][j] = 2
        for i, j in walls:
            g[i][j] = 2
        dirs = (-1, 0, 1, 0, -1)

        # for i, j in guards:
        for a, b in pairwise(dirs):
            print(a, b)


        for i, j in guards:
            for a, b in pairwise(dirs):
                x, y = i, j
                while 0 <= x + a < m and 0 <= y + b < n and g[x + a][y + b] < 2:
                    x, y = x + a, y + b
                    g[x][y] = 1
        return sum(v == 0 for row in g for v in row)




m = 4
n = 6
guards = [[0, 0], [1, 1], [2, 3]]
walls = [[0, 1], [2, 2], [1, 4]]

solution = Solution()
output = solution.countUnguarded(m, n, guards, walls)
print(output)
