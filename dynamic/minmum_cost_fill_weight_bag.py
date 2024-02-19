
# Create matrix min_cost[n+1][W+1], where n is number of distinct weighted packets of orange and W is the maximum capacity of the bag.
# Initialize the 0th row with INF (infinity) and 0th Column with 0.
# Now fill the matrix
# if wt[i-1] > j then min_cost[i][j] = min_cost[i-1][j] ;
# if wt[i-1] <= j then min_cost[i][j] = min(min_cost[i-1][j], val[i-1] + min_cost[i][j-wt[i-1]]);
# If min_cost[n][W]==INF then output will be -1 because this means that we cant not make weight W by using these weights else output will be min_cost[n][W].




def MinimumCost():
    return 0






cost = [1, 2, 3, 4, 5]
W = 5
n = len(cost)

print(MinimumCost(cost, n, W))















