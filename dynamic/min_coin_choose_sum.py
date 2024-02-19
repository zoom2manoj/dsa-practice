
def help(coin, weight, w, n,  dp):

    if w==0:
        return 0

    if w<0 or n<=0:
        return
    if dp[n][w]!=-1:
        return dp[n][w]





def sum_choice(coin, w):
    n = len(coin)
    weight = [0 for x in range(n)]

    dp =  [[-1 for x in range(w+1)] for i in range(n+1)]
    res = help(coin,weight, w, n , dp)
    print(res)
    # print(dp)

    return 0


coin = [1, 2, 3]
w = 5
sum_choice(coin, w)
