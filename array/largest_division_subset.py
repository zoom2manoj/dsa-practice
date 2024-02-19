
# Prints largest divisible subset
def findLargest(nums, n):

    nums.sort(reverse = False)

    divCount = [1 for i in range(n)]

    prev = [-1 for i in range(n)]

    max_ind = 0

    for i in range(1 ,n):
        for j in range(i):
            print(i, j, arr[i], arr[j], arr[i] % arr[j])
            if (arr[i] % arr[j] == 0):
                print(divCount, prev)
                if (divCount[i] < divCount[j] + 1):
                    divCount[i] = divCount[j ] +1
                    prev[i] = j

        if (divCount[max_ind] < divCount[i]):
            max_ind = i

    k = max_ind
    list = []
    print('kk ', prev)
    while (k >= 0):
        list.append(nums[k])
        print(k)
        k = prev[k]
    print(list)
    return list.sort(reverse=False)

# Driven code
if __name__ == '__main__':
    arr = [1, 2, 17, 4]
    arr = [4, 8, 10, 240]

    n = len(arr)
    findLargest(arr, n)
