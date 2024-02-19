import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        def divided_con(a, l, r):
            print(a, l , r)
            if l>r:
                return -sys.maxsize

            mid, left_sum, right_sum, curr_sum = (l+r)//2, 0, 0, 0
            for i in range(mid-1, l-1, -1):
                curr_sum = curr_sum+a[i]
                left_sum = max(left_sum, curr_sum)

            curr_sum = 0
            for i in range(mid+1, r+1):
                curr_sum = curr_sum+a[i]
                right_sum = max(right_sum, curr_sum)



            return max(divided_con(nums, l, mid-1), divided_con(a, mid+1, r), left_sum+a[mid]+right_sum)



        mid = divided_con(nums, 0, len(nums)-1)
        return mid


nums = [-2,1,-3,4,-1,2,1,-5,4]
solution  = Solution()
resp = solution.maxSubArray(nums)
print(resp)


