

unsorted_list = [64, 34, 25, 12, 22, 11, 90]

def swap(data, i):
    temp = data[i]
    data[i] = data[i+1]
    data[i+1] = temp

def insert_sort(data):

    for i in range(len(data)):
        key = data[i]

        j = i-1
        while j>=0 and data[j]>data[j+1]:
            swap(data, j)
            print(j, data)
            j-=1

print(unsorted_list)
insert_sort(unsorted_list)
print(unsorted_list)
