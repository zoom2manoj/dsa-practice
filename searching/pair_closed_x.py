def bs(arr, l, r, target):
    if l > r:
        return l - 1

    mid = l + (r - l) // 2
    if arr[mid] == target:
        return mid

    if arr[mid] < target:
        return bs(arr, mid + 1, r, target)

    else:
        return bs(arr, l, mid - 1, target)


def find_pair_closed_target(ar1, ar2, m, n, x):
    min_diff = float('inf')
    closest_pair = (None, None)
    for i in range(len(ar1)):
        num = ar1[i]
        pos = bs(ar2, 0, len(ar2) - 1, x - num)

        if pos < len(ar2):
            diff = abs(ar2[pos] + num - x)
            if diff < min_diff:
                min_diff = diff
                closest_pair = (i, pos)
        if pos > 0:
            diff = abs(ar2[pos - 1] + num - x)
            if diff < min_diff:
                min_diff = diff
                closest_pair = (i, pos - 1)

    print(closest_pair, min_diff)


ar1 = [1, 4, 5, 7]
ar2 = [10, 20, 30, 40]
m = len(ar1)
n = len(ar2)
x = 38

output = find_pair_closed_target(ar1, ar2, m, n, x)
print(output)


# f O(n log m), it's binary search solutions