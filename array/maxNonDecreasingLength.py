from typing import List


class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        print('hi')

        ans = 1
        dp1 = 1
        dp2 = 1
        for i in range(1, len(nums1)):
            dp11 = dp1 + 1 if nums1[i - 1] <= nums1[i] else 1
            dp21 = dp2 + 1 if nums2[i - 1] <= nums1[i] else 1
            dp12 = dp1 + 1 if nums1[i - 1] <= nums2[i] else 1
            dp22 = dp2 + 1 if nums2[i - 1] <= nums2[i] else 1

            dp1 = max(dp11, dp21)
            dp2 = max(dp12, dp22)
            ans = max(ans, dp1, dp2)
        return ans


nums1 = [2, 3, 1]
nums2 = [1, 2, 1]
solution = Solution()
res = solution.maxNonDecreasingLength(nums1, nums2)
print(res)
