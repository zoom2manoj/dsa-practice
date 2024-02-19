import heapq
from typing import List

#
# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         left = 0
#         right = len(arr)-k
#         while left<right:
#             mid = left+(right-left)//2
#
#             if x-arr[mid]>arr[mid+k]-x:
#                 left = mid+1
#             else:
#                 right =mid
#
#
#
#         return arr[left:left+k]
#
#



class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        max_h = []


        for item in arr:

            heapq.heappush(max_h, item)
            if len(max_h)>k:
                print(max_h)
                # d  = heapq.heappop(max_h)
                # heapq.
                # print('aaa ', d)

        res = []
        while len(arr)-k<len(max_h):
            item = heapq.heappop(max_h)
            res.append(item)

        return res








solution = Solution()
# arr = [1,2,3 ,4, 5]  # sorted
arr = [1,5,3 ,4, 2]
k = 4
x = 3
res = solution.findClosestElements(arr, k, x)
print(res)