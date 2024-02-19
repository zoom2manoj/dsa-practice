from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


        lis = []
        def insert(num ):
            left = 0
            right = len(lis)-1

            while left <=right:
                mid = left + (right - left) // 2
                if lis[mid]>=num:
                    right = mid-1
                else:
                    left = mid+1

            if len(lis)==left:
                lis.append(num)
            else:
                lis[left]= num


        for x in nums:
            insert(x)
        return len(lis)


nums = [4,10,4,3,8,9]
# nums = [0,1,0,3,2,3]
solution = Solution()
output  = solution.lengthOfLIS(nums)
print(output)
