from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        nums = [x * x for x in nums]
        print(nums)

        def mergedata(data, left, right):
            print("merge data", left, right)
            i = 0
            j = 0
            k = 0
            while (i <len(left) and j <len(right)):
                if left[i]<right[j]:
                    data[k] = left[i]
                    k+=1
                    i+=1
                else:
                    data[k] = right[j]
                    k+=1
                    j+=1

            while (i <len(left)):
                data[k] = left[i]
                k += 1
                i += 1
            while (j <len(right)):
                data[k] = right[j]
                k += 1
                j += 1


        def mergesort(data):
            print(data)
            if len(data)>1:
                mid = len(data)//2
                l = data[:mid]
                r = data[mid:]
                mergesort(l)
                mergesort(r)
                mergedata(data, l, r)


        mergesort(nums)

        print('=====')
        print(nums)

        return nums

s = Solution()
input = [-4,-1,0,3,10]
s.sortedSquares(input)