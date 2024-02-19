
class Solution:
    def reverse(self, x: int) -> int:

        flage = -1 if x<0 else 1
        x = abs(x)
        result = 0
        while x:
            print('x ', x, 'x%10', x%10,)
            result = result*10 + x%10
            x//=10

        print(flage*result)
        output = flage*result

        if 2**31 <= output <= 2**31 - 1:
            return 0

        return output

input = -123
solution = Solution()
output  = solution.reverse(input)

print(output)