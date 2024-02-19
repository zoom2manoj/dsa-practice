from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # count = 0
        # output = []
        # for i in range(len(nums)):
        #     print('-', i)
        #     if i < len(nums) - 2 and nums[i] == nums[i + 1]:
        #         continue
        #     print(i)
        #     output.append(nums[i])
        #     count += 1
        count = 1
        current_item = nums[0]
        for index in range(1, len(nums)):
            # print(index)
            item = nums[index]
            if item > current_item:
                # print('current and item ', current_item, item)
                count += 1
                current_item = nums[index]
                nums[count - 1], nums[index] = nums[index], nums[count - 1]
                # print(nums)

            # if nums[index]>nums[index-1]:
            #     count+=1
            #     continue
            # else:
            #     nums[index-1], nums[index]

        # print('output', count, 'nums', nums)

        return count


data  = [1, 1, 2, 4, 5, 6, 6 , 7]
solution = Solution()
output = solution.removeDuplicates(data)
print(output)

