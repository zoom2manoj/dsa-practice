from typing import List


class RainWaterTrapper:
    def trap(self, height: List[int]) -> int:
        if height == []:
            return 0
        left = [0 for i in range(len(height))]
        right = [0 for i in range(len(height))]
        total_water = 0

        left[0] = height[0]
        for i in range(1, len(height)):
            left[i] = max(left[i - 1], height[i])

        right[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])

        for i in range(len(height)):
            total_water += min(left[i], right[i]) - height[i]
            print(total_water)

        return total_water

s = [0,1,0,2,1,0,1,3,2,1,2,1]  # output 6
s = [4,2,0,3,2,5]  # output 9


rainWater = RainWaterTrapper()
resp = rainWater.trap(s)

print(resp)
