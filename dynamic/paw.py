class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)

        if n & 1:
            return x * self.myPow(x, n - 1)

        return self.myPow(x * x, n // 2)



solution = Solution()
print(solution.myPow(2, 6))