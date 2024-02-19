class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, ans = [-1], 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif len(stack) == 1:
                stack[0] = i
            else:
                stack.pop()
                ans = max(ans, i - stack[-1])
        return ans




solution = Solution()
s = '(()'
output  = solution.longestValidParentheses(s)
print(output)