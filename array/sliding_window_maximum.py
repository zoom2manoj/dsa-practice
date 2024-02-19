from collections import deque
# def sliding_window_maximum(nums, k):
#     if k == 0:
#         return []
#
#     def add_to_dq(dq, nums, i):
#         while len(dq) and nums[dq[-1]] <= nums[i]:
#             dq.pop()
#         dq.append(i)
#         return
#
#     dq = deque()
#     for i in range(k):
#         add_to_dq(dq, nums, i)
#     result, start, end = [], 0, k - 1
#     while end < len(nums):
#         while True:
#             if dq[0] >= start:
#                 result.append(nums[dq[0]])
#                 break
#             else:
#                 dq.popleft()
#         start, end = start + 1, end + 1
#         if end < len(nums):
#             add_to_dq(dq, nums, end)
#     return result


def sliding_window_maximum(nums, k):
    if k == 0:
        return []
    start, end =  0, k-1
    result = []
    dq = deque()
    def add_dq(dqq, nums, end):
        while len(dqq) and nums[dqq[-1]]<=nums[end]:
            dqq.pop()
        dqq.append(end)
    for x in range(k):
        add_dq(dq, nums, x)
        print(dq)
    while end<len(nums):
        while True:
            if len(dq) and nums[dq[0]]>=nums[end]:
                print('hi')
                result.append(nums[dq[0]])
                break
            else:
                dq.popleft()
        print(dq)
        start+=1
        end+=1
        if end<len(nums):
            add_dq(dq, nums, end)
    return result


# Example usage:
numbers = [1, 3, -1, -3, 5, 3, 6, 7]
window_size = 3
max_in_subarrays = sliding_window_maximum(numbers, window_size)
print("Maximum elements in all subarrays of size", window_size, "are:", max_in_subarrays)
