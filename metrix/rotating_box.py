from collections import deque
from typing import List


class Solution:
    def print(self, box):

        for i in range(len(box)):
            for j in range(len(box[0])):
                print(box[i][j], end=" ")
            print("")
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        self.print(box)
        m, n = len(box), len(box[0])
        ans = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                ans[j][m - i - 1] = box[i][j]
        for j in range(m):
            q = deque()
            for i in range(n - 1, -1, -1):
                if ans[i][j] == '*':
                    q.clear()
                elif ans[i][j] == '.':
                    q.append(i)
                elif q:
                    ans[q.popleft()][j] = '#'
                    ans[i][j] = '.'
                    q.append(i)
        self.print(ans)
        return ans



box = [["#", "#", "*", ".", "*", "."],
       ["#", "#", "#", "*", ".", "."],
       ["#", "#", "#", ".", "#", "."]]

# box = [["#", "#", "#", "#", ".", "."]]

solution = Solution()
output = solution.rotateTheBox(box)
print(output)
