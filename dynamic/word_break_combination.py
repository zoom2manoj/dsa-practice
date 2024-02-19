from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}

        def solve(s, wordDict):
            if not s:
                return ['']
            if s in memo:
                return memo[s]
            ret = []
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    for j in solve(s[i:], wordDict):
                        ret.append((s[:i] + " " + j).strip())
            memo[s] = ret
            return memo[s]
        d = solve(s, set(wordDict))
        return d


solution = Solution()
# s = "catsanddog",
# wordDict = ["cat","cats","and","sand","dog"]

s = 'pineapplepenapple'
wordDict = ["apple","pen","applepen","pine","pineapple"]
res = solution.wordBreak(s, wordDict)
print(res)