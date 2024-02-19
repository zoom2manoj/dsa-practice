

def helper(profit, weight, w, n, dp):


    if w==0 or n==0:
        return 0
    if dp[n][w]!=-1:
        return dp[n][w]

    if weight[n-1]<=w:
        dp[n][w] = max(profit[n-1]+helper(profit, weight, w-weight[n-1], n , dp), helper(profit, weight, w, n-1 , dp))
        return dp[n][w]

    elif weight[n-1]>w:
        dp[n][w] = helper(profit, weight, w, n-1, dp)

    return dp[n][w]





profit = [60, 100, 120]
weight = [10, 20, 30]
W = 50
n = len(profit)

dp  =[ [-1 for x in range(W+1)] for i in range(n+1)]

res = helper(profit, weight, W, n, dp)
print(res)


