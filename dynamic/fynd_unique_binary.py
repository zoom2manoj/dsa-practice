from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        for x in range(pow(2, n)):
            print(x, bin(x))
            data  = bin(x).replace('0b', '')

            if len(data)<n:
                s = '0'*(n-len(data))
                data = s+data
            if data not in nums:
                return data




solution  = Solution()
nums = ['01', '10']
nums = ["111","011","001"]
ss = solution.findDifferentBinaryString(nums)
print(ss)