from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        colums_grid = grid[0]

        column = [[] for i in range(len(colums_grid))]
        for row in grid:
            for j, value in enumerate(row):
                column[j].append(value)

        equal_pair = 0
        for row in grid:
            for j, element in enumerate(colums_grid):
                if row[0] == element:
                    if row == column[j]:
                        equal_pair+=1

        return equal_pair





grid = [[3,2,1],[1,7,6],[2,7,7]]

soution = Solution()
res = soution.equalPairs(grid)
print(res)

