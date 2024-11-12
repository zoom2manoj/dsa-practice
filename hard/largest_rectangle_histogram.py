from typing import List


class Solution:
    def calculate_max_area(self, index, heights):
        output = 0
        for i in range(index+1):
            min_value = min(heights[:i+1])
            
            output = max(output, min_value*i+1)
            print(i, min_value, heights[:i+1])
        print('===')
        return output

    def largestRectangleArea(self, heights: List[int]) -> int:
        print('data', heights)
        output = 0
        for index in range(len(heights)):
            # print(heights[index])calculate_max_area


            output = max(output, self.calculate_max_area(index, heights))


        return output








data = [2,1,5,6,2,3]
solution = Solution()
resp = solution.largestRectangleArea(data)
print(resp)



