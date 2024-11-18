from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        counter=0
        last_index = 0
        for index, item in enumerate(arr.copy()):
            if item ==0:
                arr.insert(index+counter, 0)
                counter+=1
            last_index = index

        arr = arr[:last_index+1]
        print(arr)





arr = [1,0,2,3,0,4,5,0]
solution = Solution()
output = solution.duplicateZeros(arr)
print(output)