from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        def dfs(data, list):
            if len(data)==0:
                result.append(list)
            for i in range(len(data)):
                dfs(data[:i]+data[i+1:], list+[data[i]])
            # return data[]


        dfs(nums, [])
        return result


nums = [1,2,3]
solution = Solution()
print(solution.permute(nums))