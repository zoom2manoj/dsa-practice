
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        depth = [[None for x in range(m)] for y in range(n)]
        for x in range(n):
            for y in range(m):
                if x==0 or y==0:
                    depth[x][y]=1
                else:
                    depth[x][y] = depth[x-1][y]+depth[x][y-1]
        return depth[n-1][m-1]


solution = Solution()
output = solution.uniquePaths(3, 7)

print(output)