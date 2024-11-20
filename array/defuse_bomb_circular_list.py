from itertools import accumulate
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = []
        prefix_sum = list(accumulate(code))
        prefix_sum_double = [0]*2*n
        prefix_sum_double[0] = code[0]
        for i in range(1, 2*n):
            prefix_sum_double[i]+= prefix_sum_double[i-1]+code[i%n]

        if k > 0:
            for i in range(0, n):
                first = prefix_sum[i]
                if k <n - i:
                    second = prefix_sum[i + k]
                else:
                    second = prefix_sum[-1] + prefix_sum[abs(n -i - k)]
                total_value = second - first
                result.append(total_value)
        elif k < 0:
            print("=============", n)
            for i in range(0, n):
                # print(i+k)
                result.append(prefix_sum_double[n-1+(i)]-prefix_sum_double[n-1+(i+k)])
            print(result)




        else:
            result = [0] * len(code)
        return result


code = [5, 7, 1, 4]
k = 3

code = [2,4,9,3, 5, 6] # output [11, 8, 6, 13, 12, 8]
code = [2,4,9,3]
k = -2
solution = Solution()
output = solution.decrypt(code, k)
print(output)
