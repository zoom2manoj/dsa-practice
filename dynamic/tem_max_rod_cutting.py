class Solution:

    # Function to find the maximum obtainable value by cutting the rod
    def cutRod(self, price, n):
        dp = [0 for i in range(n+1)]
        for i in range(1, n+1):
            max_val = -1
            for j in range(i):
                max_val = max(max_val, dp[j]+price[i-j-1])
            dp[i] = max_val
        return dp[n]



price = [1, 5, 8, 9, 10, 17, 17, 20]
N = 8

solution = Solution()
output = solution.cutRod(price, N)
print(output)
