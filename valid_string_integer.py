


class Solution:
    def isNumber(self, S: str) -> bool:

        num, sign, exp, dec = False, False , False, False

        for c in S:
            if c=='-' or c=='+':
                if num or dec or exp:
                    return False
                sign = True
            elif c=='.':
                if dec or exp:
                    return False
                dec = True
            elif c=='e' or c=='E':
                if exp or not num:
                    return False
                exp = True
                sign = False
                num = False
                dec = False
            elif c>='0' and c<='9':
                num = True
            else:
                return False




        return num





solution = Solution()
data = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
for i in data:
    resp = solution.isNumber(i)
    print(i, resp)
print('==================')
data = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
for i in data:
    resp = solution.isNumber(i)
    print(i, resp)

