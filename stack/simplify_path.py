class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []

        for str in path.split('/'):
            if str in ('', '.'):
                continue
            if str == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(str)

        return '/' + '/'.join(stack)

s = "/a/./b/../../c/"  # output /c
s = "/home//foo/" # output "/home/foo"



solution = Solution()
out  = solution.simplifyPath(s)

print(out)