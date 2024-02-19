

arr1 = [ 1, 3, 4, 5]
arr2 = [2, 4, 6, 8, 9, 11]

class Solution:
    def merge(self, nums1, nums2):
        nums3 = []
        m = len(nums1)
        n = len(nums2)
        k = m+n
        i = 0
        x, y =0,0
        while i< k and x<m and y<n:
            print(i, x, y )
            if nums1[x]<nums2[y]:
                nums3.append(nums1[x])
                nums3.append(nums2[y])
                x+=1
                y+=1
            else:
                nums3.append(nums2[y])
                nums3.append(nums1[x])
                y += 1
                x+=1
            i+=1


        while x<m:
            nums3.append(nums1[x])
            x+=1
        while y<n:
            nums3.append(nums2[y])
            y+=1


        print(nums1)
        print(nums2)
        print(nums3)
        return nums3

solution = Solution()
solution.merge(arr1, arr2)





