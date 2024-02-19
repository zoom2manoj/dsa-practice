

def first_missing_positive(nums):
    num_len = len(nums)
    record = [0 for _ in range(num_len + 1)]

    for i in range(num_len):
        if nums[i] <= 0 or nums[i] > num_len + 1:
            continue
        record[nums[i] - 1] = i + 1
    print(record)
    for j in range(num_len + 1):
        if record[j] == 0:
            return j + 1
    return -1


# Example usage:
# nums = [3, 4, -1, 1]
nums = [-10,-3,-100,-1000,-239,1]

result = first_missing_positive(nums)
print("The smallest missing positive integer is:", result)

