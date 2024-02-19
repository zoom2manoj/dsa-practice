class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = 'aeiou'
        ans = 0
        maxc = 0
        for i, c in enumerate(s):

            if c in vowel:
                maxc+=1
            if i>=k and s[i-k] in vowel:
                maxc-=1
            ans = max(maxc, ans)

        return ans


s = 'abciiidef'
# s = 'zpuerktejfp'
s  = 'ibpbhixfiouhdljnjfflpapptrxgcomvnb'
vowel  = ['a', 'e', 'o', 'u', 'i']
k = 3
k = 33
solution = Solution()
aa = solution.maxVowels(s, k)
print('res', aa)