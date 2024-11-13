

list  = [11, 12, 22, 25, 34, 64, 90]
target = 12
counter = 0;

def binary_search(data, target):

    s = 0
    e = len(data)-1

    # print(s, e)
    while s<e:

        mid = (e+s)//2
        # print(mid)
        # print(data[:mid])
        # print((data[mid:]))

        if target==data[mid]:
            return mid
        elif target>data[mid]:
            s = mid+1
        else:
            e = mid-1

    return -1







out = binary_search(list, target)
print(out)







