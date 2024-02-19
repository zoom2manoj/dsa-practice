from typing import List


class Solution:
    def searchMatrix(self, M: List[List[int]], T: int) -> bool:
        # y, i, j = len(M), 0, len(M[0]) - 1
        # while i < y and ~j:
        #     cell = M[i][j]
        #     if cell == T:
        #         return True
        #     elif cell > T:
        #         j -= 1
        #     else:
        #         i += 1
        # return False


        row = len(M)
        column = len(M[0])
        i =0
        j = column-1
        while i>=0 and j<row:
            item = M[i][j]
            print(item)

            if T == item:
                return True
            elif T>item:
                i+=1
            elif T<item:
                j-=1
        return False


m = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
t = 5
# m = [[1,1]]
# t = 0
solution = Solution()
output = solution.searchMatrix(m, t)
print(output)
