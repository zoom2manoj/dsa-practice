from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        # print(nums)
        #
        # start =0
        # next = start+3
        # output = []
        # for i in range(next, len(nums)+1):
        #     print('i ', i)
        #     print(nums[start: next])
        #     print(nums[start: next], '=', sum(nums[start: next]))
        #
        #     if sum(nums[start: next])==0:
        #         output.append(nums[start: next])
        #     start+=1
        #     next+=1
        # print('output ', output)
        # return output
        #

        nums = sorted(nums)
        result = set()
        for index in range(0, len(nums) - 2):
            l = index + 1
            r = len(nums) - 1
            while (l < r):
                val = nums[index] + nums[l] + nums[r]
                if val == 0:
                    result.add(tuple(sorted((nums[index], nums[l], nums[r]))))
                    r -= 1
                    l += 1

                if val > 0:
                    r -= 1
                if val < 0:
                    l += 1

        return result

nums = [-1,0,1,2,-1,-4]
# [-1,0,1,2,-1,-4]
solution = Solution()
res = solution.threeSum(nums)
print(res)

# three item sum == 0

