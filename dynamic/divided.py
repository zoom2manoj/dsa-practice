

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        MAX = 2**31-1
        MIN = -MAX-1
        # Check for overflow
        if divisor == 0 or (dividend == MIN and divisor == -1):
            return MAX




        quotient=0
        sign = 1 if (dividend>0 and divisor>0) or (dividend<0 and divisor<0)  else -1
        a_divident = abs(dividend)
        a_divisor = abs(divisor)

        while a_divident>=a_divisor:

            shift = 0

            while a_divident>=(a_divisor<<shift):
                shift+=1
            # print('after shifting', shift)
            quotient+= (1<<(shift-1))
            # print('after shift shifting', shift)

            a_divident -= (a_divisor<<(shift-1))



        return sign*quotient

solution = Solution()
a = 10
b = 3
output  = solution.divide(a, b)
print(output)
