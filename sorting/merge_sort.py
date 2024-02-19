

list1 = [44, 65, 2, 3, 58, 14, 57, 23, 10, 1, 7, 74, 48]

s = 0
e = len(list1)

def swap_item(data):
    temp = data[0]
    data[0] = data[1]
    data[1] = temp
    return data


def merge_sort(data):
    if len(data)>1:
        middle = len(data)//2
        left = data[:middle]
        right = data[middle:]

        merge_sort(left)
        merge_sort(right)

        a=b=c=0

        while a<len(left) and b<len(right):
            if left[a]<right[b]:
                data[c] = left[a]
                c+=1
                a+=1
            else:
                data[c] = right[b]
                c+=1
                b+=1

        while a<len(left):
            data[c] = left[a]
            c += 1
            a += 1

        while b<len(right):
            data[c] = right[b]
            c += 1
            b += 1
    print(data)

print(list1)
merge_sort(list1)
print(list1)