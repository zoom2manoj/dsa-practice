import sys


def knapsnap_helper(cost, weight, w, n , dp):

    if(w==0):
        return 0

    if w<0 or n<=0:
        return sys.maxsize

    if dp[n][w]!=-1:
        return dp[n][w]

    if (cost[n-1]<0):
        dp[n][w] = min(sys.maxsize, knapsnap_helper(cost, weight, w, n-1, dp))
        return dp[n][w]


    if weight[n-1]<=w:
        dp[n][w] = min(cost[n-1]+knapsnap_helper(cost, weight, w-weight[n-1], n, dp), knapsnap_helper(cost, weight, w, n-1, dp))
        return dp[n][w]

    dp[n][w] = knapsnap_helper(cost, weight, w, n-1, dp)
    return dp[n][w]





    # return dp[n][w]
def minCost(cost, w):

    n = len(cost)
    weight = [0 for i in range(w)]
    for x in range(1, w+1):
        weight[x-1] = x


    dp = [[-1 for i in range(w+1)] for j in range(n+1)]
    print(dp)
    print(weight)

    res = knapsnap_helper(cost, weight, w, n, dp)

    print(res)






W = 5
cost = [20, 10, 4, 50, 100]

minCost(cost, W)
