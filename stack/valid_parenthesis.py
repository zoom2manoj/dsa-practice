
class Solution:
    def isValid(self, s: str) -> bool:
        parenthasis = ['(', ')', '{', '}', '[', ']']
        parenth_dict = { ')':'(', '}':'{',  ']':'['   }
        # parenth_dict = {'(':')', '{': '}', '[': ']'}
        stack = []
        for x in s:
            print(x)
            if x in parenthasis:
                if len(stack)>0 and x in parenth_dict and parenth_dict[x] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(x)

        print(stack)
        return True if len(stack)==0 else False


# s = "()"
s = "(){}}{"

solution = Solution()
response = solution.isValid(s)
print(response)