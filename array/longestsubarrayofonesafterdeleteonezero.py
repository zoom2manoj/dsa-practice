from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        last = 0
        second = 0
        for i in range(len(nums)):
            if nums[i]==0:
                if second!=i:
                    print(ans, second, last, i, nums[second+1:i])
                    ans = max(ans, len(nums[second+1:i])-1)
                    # print(ans)
                second = last
                last = i
            elif i==len(nums)-1:
                if second==0:
                    ans = max(ans, len(nums[second:i+1]))
                else:
                    ans = max(ans,  len(nums[second:i+1])-1)
                print(ans, second, last, i, nums[second + 1:i+1])

        return ans

# [0, 1, 1, 1, 0, 1, 1, 0, 1]
# 0, 1, 1, 1
# 1, 1, 1, 0, 1, 1,
# 1, 1, 0, 1
nums = [0,1,1,1,0,1,1,0,1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1]
nums = [0,1,1,1,0,1,1,0,1]
nums = [1,1,0,1]
# nums = [1,1,1]

print(nums)
solution = Solution()
res = solution.longestSubarray(nums)
print("\n", res)
