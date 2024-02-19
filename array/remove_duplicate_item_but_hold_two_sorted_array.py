



class Solution:
    def __init__(self):
        print('hi')

    def remove_duplicate(self, nums, target):
        j = 0
        n = len(nums)
        count = 0
        for i in range(0, len(nums)-1):
            print(nums[i])

            if nums[i]!=nums[i+1]:

                if i>0 and nums[i]==nums[i-1]:
                    nums[j] = nums[i-1]
                    j += 1
                nums[j] = nums[i]
                j+=1


        print(nums)
        if nums[n-1]==nums[n-2]:
            nums[j] = nums[n - 1]
            j+=1

        nums[j] = nums[n-1]
        j+=1
        print(j)
        return j










nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 5]

nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 5]
nums = [0,0,1,1,1,1,2,3,3]


solution = Solution()
total = solution.remove_duplicate(nums, 2)

output = nums[:total]
print(output)