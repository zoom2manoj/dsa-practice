def two_pointer_tech(arr, target):
    left = 0
    right = len(arr) - 1
    arr.sort()
    while left < right:

        if target - arr[left] == arr[right]:
            return True
        elif target - arr[left] < arr[right]:
            right -= 1
        else:
            left += 1
    return False


arr = [0, -1, 2, -3, 1]
target = -2

output = two_pointer_tech(arr, target)
print(output)

# Two-Pointer Technique – O(n) time and O(1) space
