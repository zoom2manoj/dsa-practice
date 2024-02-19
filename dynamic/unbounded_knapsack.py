





W = 100
val = [10, 30, 20]
wt = [5, 10, 15]
n = len(val)



def unboundedknapsacked(w, n, val, wt):

    dp = [0 for x in range(w+1)]


    for i in range(w+1):
        for j in range(n):

            if wt[j]<=i:
                dp[i] = max(dp[i], (dp[i-wt[j]]+val[j]))



    return dp[w]





output = unboundedknapsacked(W, n, val, wt)
print(output)