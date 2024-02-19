from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #
        #
        # count = 0
        # l = 0
        # r = len(nums )
        # s_second = len(nums)
        # while l<s_second:
        #
        #     print(l, r)
        #     item = nums[l]
        #     if item == val:
        #         if nums[r-1] == val:
        #             nums[r-1] = '-'
        #             r -= 1
        #             s_second-=1
        #             count += 1
        #         else:
        #             nums[l], nums[r-1] = nums[r-1], '-'
        #             l += 1
        #             r -= 1
        #             s_second-=1
        #             count += 1
        #     else:
        #         l+=1
        #         # count += 1
        #         s_second-=1
        #
        #
        # print(count)
        # print(nums)
        #
        # return count
        i = 0

        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        print(i, nums)
        return i

data = [0,1,2,2,3,0,4,2]
target = 2

# data = [3,2,2,3]
# target = 3

print(data)
solution =  Solution()
solution.removeElement(data, target)