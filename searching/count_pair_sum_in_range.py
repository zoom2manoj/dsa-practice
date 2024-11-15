from bisect import bisect_left, bisect_right


def count_range_sum(arr, L, R):
    n = len(arr)

    right = n - 1
    left = 0
    count = 0
    arr.sort()

    while right > 0:

        lt1 = bisect_left(arr, L - arr[right])
        start = lt1

        lt2 = bisect_right(arr, R - arr[right])
        lt2 -= 1
        end = lt2
        end = min(end, right - 1)

        if end - start >= 0:
            count += (end - start) + 1
        right -= 1

    return count


arr = [5, 1, 2, 4, 3]
L = 5
R = 8

# arr = [-2, 5, -1]
# L = -2
# R = 2

output = count_range_sum(arr, L, R)
print(output)
