from collections import deque
from typing import List

#
# class Solution:
#     def removeInvalidParentheses(self, s: str) -> List[str]:
#
#         # def isParentheses(c):
#         #     return  (c==')') or (c=='(')
#         #
#         # def isValid(s):
#         #     # print('validation ', s)
#         #     counter = 0
#         #     for i in range(len(s)):
#         #         if s[i] =='(':
#         #             counter +=1
#         #         elif s[i]==')':
#         #             counter -=1
#         #         if counter<0:
#         #             return False
#         #     return (counter==0)
#         #
#         # if len(s)==0:
#         #     return
#         #
#         # visited = set()
#         # q = []
#         # level = 0
#         # temp = 0
#         # q.append(s)
#         # visited.add(s)
#         # result = []
#         # # print(q)
#         # # print(visited)
#         # while len(q):
#         #     str = q[-1]
#         #     q.pop()
#         #     # print('q', q)
#         #     if isValid(str):
#         #         # print('valid ', str)
#         #         result.append(str)
#         #         level = True
#         #     if level:
#         #         continue
#         #
#         #     for i in range(len(str)):
#         #         if (not  isParentheses(str[i])):
#         #             continue
#         #
#         #         temp = str[0: i]+str[i+1:]
#         #         # print('temp ',i, ', ', temp)
#         #         if temp not in visited:
#         #             # print('temp value added in q', temp)
#         #             q.append(temp)
#         #             visited.add(temp)
#         #
#         # # print('====================')
#         # # print(q)
#         # return result
#
#         def getLeftRightCount(s):
#             l, r =0, 0
#             for c in s:
#                 if c=='(':
#                     l+=1
#                 elif c==')':
#                     if l==0:
#                         r+=1
#                     else:
#                         l-=1
#             return l, r
#
#         def isValid(s):
#             # print('validation ', s)
#             counter = 0
#             for i in range(len(s)):
#                 if s[i] =='(':
#                     counter +=1
#                 elif s[i]==')':
#                     counter -=1
#                 if counter<0:
#                     return False
#             return (counter==0)
#
#         result = []
#         def dfs(str, start, l, r):
#             if l==0 and r==0 and isValid(str):
#                 result.append(str)
#                 return
#             for i in range(start, len(str)):
#                 if i>start and s[i]==s[i-1]:
#                     continue
#                 if r>0 and str[i]==')':
#                     dfs(str[:i]+str[i+1:], i, l, r-1)
#                 if l>0 and str[i]=='(':
#                     dfs(str[:i]+str[i+1:], i, l-1, r)
#
#
#         l, r = getLeftRightCount(s)
#         dfs(s, 0, l, r )
#         print(result)
#         return result
#




class Solution:
    # def removeInvalidParentheses(self, s):
    #     """
    #     :type s: str
    #     :rtype: List[str]
    #     """
    #
    #     left = 0
    #     right = 0
    #
    #     # First, we find out the number of misplaced left and right parentheses.
    #     for char in s:
    #
    #         # Simply record the left one.
    #         if char == '(':
    #             left += 1
    #         elif char == ')':
    #             # If we don't have a matching left, then this is a misplaced right, record it.
    #             right = right + 1 if left == 0 else right
    #
    #             # Decrement count of left parentheses because we have found a right
    #             # which CAN be a matching one for a left.
    #             left = left - 1 if left > 0 else left
    #
    #     result = {}
    #     def recurse(s, index, left_count, right_count, left_rem, right_rem, expr):
    #         # If we reached the end of the string, just check if the resulting expression is
    #         # valid or not and also if we have removed the total number of left and right
    #         # parentheses that we should have removed.
    #         if index == len(s):
    #             if left_rem == 0 and right_rem == 0:
    #                 ans = "".join(expr)
    #                 result[ans] = 1
    #         else:
    #
    #             # The discard case. Note that here we have our pruning condition.
    #             # We don't recurse if the remaining count for that parenthesis is == 0.
    #             if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
    #                 recurse(s, index + 1,
    #                         left_count,
    #                         right_count,
    #                         left_rem - (s[index] == '('),
    #                         right_rem - (s[index] == ')'), expr)
    #
    #             expr.append(s[index])
    #
    #             # Simply recurse one step further if the current character is not a parenthesis.
    #             if s[index] != '(' and s[index] != ')':
    #                 recurse(s, index + 1,
    #                         left_count,
    #                         right_count,
    #                         left_rem,
    #                         right_rem, expr)
    #             elif s[index] == '(':
    #                 # Consider an opening bracket.
    #                 recurse(s, index + 1,
    #                         left_count + 1,
    #                         right_count,
    #                         left_rem,
    #                         right_rem, expr)
    #             elif s[index] == ')' and left_count > right_count:
    #                 # Consider a closing bracket.
    #                 recurse(s, index + 1,
    #                         left_count,
    #                         right_count + 1,
    #                         left_rem,
    #                         right_rem, expr)
    #
    #             # Pop for backtracking.
    #             expr.pop()
    #
    #     # Now, the left and right variables tell us the number of misplaced left and
    #     # right parentheses and that greatly helps pruning the recursion.
    #     recurse(s, 0, 0, 0, left, right, [])
    #     return list(result.keys())
    def removeInvalidParentheses(self, s):
        def getLeftAndRightCounts(s: str) -> tuple:
            l = 0
            r = 0

            for c in s:
                if c == '(':
                    l += 1
                elif c == ')':
                    if l == 0:
                        r += 1
                    else:
                        l -= 1

            return l, r

        def isValid(s: str):
            count = 0  # Number of '(' - # Of ')'
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                if count < 0:
                    return False
            return True  # Count == 0

        ans = []

        def dfs(s: str, start: int, l: int, r: int) -> None:
            if l == 0 and r == 0 and isValid(s):
                ans.append(s)
                return

            for i in range(start, len(s)):
                if i > start and s[i] == s[i - 1]:
                    continue
                if r > 0 and s[i] == ')':  # Delete s[i]
                    dfs(s[:i] + s[i + 1:], i, l, r - 1)
                elif l > 0 and s[i] == '(':  # Delete s[i]
                    dfs(s[:i] + s[i + 1:], i, l - 1, r)

        l, r = getLeftAndRightCounts(s)
        dfs(s, 0, l, r)
        return ans



solution = Solution()
s = '(a)())()'
# s = '(v)())()'
# s = "(v)())()"
s = ')('
res = solution.removeInvalidParentheses(s)
print(res)