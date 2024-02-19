

# Returns true if arr[] can be
# partitioned in two subsets of
# equal sum, otherwise false


def findPartition(arr, n):
    sum = 0
    i, j = 0, 0

    # calculate sum of all elements
    for i in range(n):
        sum += arr[i]

    if sum % 2 != 0:
        return False

    part = [[True for i in range(n + 1)]
            for j in range(sum // 2 + 1)]

    # initialize top row as true
    for i in range(0, n + 1):
        part[0][i] = True

    # initialize leftmost column,
    # except part[0][0], as 0
    for i in range(1, sum // 2 + 1):
        part[i][0] = False

    print_dp(part)
    print('==== initial')
    # fill the partition table in
    # bottom up manner
    for i in range(1, sum // 2 + 1):
        print(' i iterate ')
        for j in range(1, n + 1):
            print_dp(part)
            print(i, j, arr)
            part[i][j] = part[i][j - 1]

            if i >= arr[j - 1]:
                print(part[i][j])
                print(part[i - arr[j - 1]][j - 1])
                part[i][j] = (part[i][j] or
                              part[i - arr[j - 1]][j - 1])
                print_dp(part)

        print_dp(part)
    return part[sum // 2][n]


def print_dp(part):
    for x in part:
        print(x)
    print('============')

# Driver Code
arr = [3, 1, 1, 2, 2, 1]
# arr = [ 1, 5, 11, 5]

n = len(arr)

# Function call
if findPartition(arr, n) == True:
    print("Can be divided into two",
          "subsets of equal sum")
else:
    print("Can not be divided into ",
          "two subsets of equal sum")

