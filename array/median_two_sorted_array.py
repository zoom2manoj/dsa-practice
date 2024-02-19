from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # if len(nums2) > len(nums1):
        #     nums1, nums2 = nums2, nums1
        # m = len(nums1)
        # n = len(nums2)
        #
        # i = 0
        # k = m + n
        # mid = (m + n) // 2
        # print('mid ', mid)
        # odd_even_flage = True if (m + n) % 2 == 0 else False
        # x, y = 0, 0
        # print(nums1, nums2)
        # xx, yy = 0, 0
        # while i < m:
        #
        #     if i<m:
        #
        #         temp = xx if xx>yy else yy
        #         if x+y>=(m+n)//2:
        #             return (nums1[x]+temp)/2 if odd_even_flage else nums1[x-1]
        #
        #         xx = nums1[x]
        #         print(xx)
        #         if nums2[y]>nums1[x]:
        #             x+=1
        #
        #     if i<n:
        #         temp = xx if xx>yy else yy
        #         if x+y>=(m+n)//2:
        #             return (nums1[y]+temp)/2 if odd_even_flage else nums1[y-1]
        #
        #
        #         yy = nums2[y]
        #         print(yy)
        #         if nums1[x]>nums2[y]:
        #             y+=1
        #     i += 1
        #
        #     print('x, y, x+y mid, xx, yy', x, y, x+y, mid, xx, yy)
        #
        # return 0
        #

        n = len(nums1)
        m = len(nums2)
        if (n > m):
            return self.findMedianSortedArrays(nums2, nums1)  # Swapping to make A smaller

        start = 0
        end = n
        realmidinmergedarray = (n + m + 1) // 2

        while (start <= end):
            mid = (start + end) // 2
            leftAsize = mid
            leftBsize = realmidinmergedarray - mid

            # checking overflow of indices
            leftA = nums1[leftAsize - 1] if (leftAsize > 0) else float('-inf')
            leftB = nums2[leftBsize - 1] if (leftBsize > 0) else float('-inf')
            rightA = nums1[leftAsize] if (leftAsize < n) else float('inf')
            rightB = nums2[leftBsize] if (leftBsize < m) else float('inf')

            # if correct partition is done
            if leftA <= rightB and leftB <= rightA:
                if ((m + n) % 2 == 0):
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
                return max(leftA, leftB)

            elif (leftA > rightB):
                end = mid - 1
            else:
                start = mid + 1

first = [1, 3, 6, 8]
second = [5]

# first = [1, 2]
# second = [3, 4]

# first = []
# second = [1]

# first= [0,0,0,0,0]
# second = [-1,0,0,0,0,0,1]

# first = [1,3]
# second = [2]


solution = Solution()
output = solution.findMedianSortedArrays(first, second)
print('output ', output)
