from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        dp = [False]*(n+1)

        dp[0] = True

        for i in range(n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    print(s[j:i])
                    dp[i] = True
                    dp[i] = True
        return dp[n]



s = 'leetcode'
worddict = ["leet","code"]
s = 'catsandog'
worddict = ["cats","dog","sand","and","cat"]

solution = Solution()
resp = solution.wordBreak(s, worddict)
print(resp)