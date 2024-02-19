class Solution:
    def mySqrt(self, x: int) -> int:

        # if 0 > x or x > 2 ** 31 - 1:
        #     return x
        # if x == 0 or x == 1:
        #     return x
        #
        # start = 1
        # end = x // 2
        #
        # mid = 0
        # output = 0
        # while start <= end:
        #
        #     mid = start + (end-start) // 2
        #     print(start, end, mid, mid * mid)
        #     if mid * mid > 2 ** 31 - 1:
        #         end -= mid // 2
        #     elif mid * mid == x:
        #         return mid
        #     elif mid * mid < x:
        #
        #         start = mid + 1
        #         output = mid
        #     else:
        #         end = mid - 1
        #
        # return output
        # Base cases
        if (x == 0 or x == 1):
            return x

        # Do Binary Search for floor(sqrt(x))
        start = 1
        end = x // 2
        while (start <= end):
            mid = (start + end) // 2

            # If x is a perfect square
            if (mid * mid == x):
                return mid

            # Since we need floor, we update
            # answer when mid*mid is smaller
            # than x, and move closer to sqrt(x)
            if (mid * mid < x):
                start = mid + 1
                ans = mid

            else:

                # If mid*mid is greater than x
                end = mid - 1

        return ans


x = 2147395599
solution = Solution()
output = solution.mySqrt(x)
print(output)