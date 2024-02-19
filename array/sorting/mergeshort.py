


arr = [4, 65,2,  6, 8,0]
new_arra = []
def mergesort(data):


    if len(data)>1:
        mid = len(data)//2
        l = data[:mid]
        r = data[mid:]
        mergesort(l)
        mergesort(r)


        i= 0
        j = 0
        k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                data[k] = l[i]
                i+=1
            else:
                data[k] = r[j]
                j+=1
            k+=1
        while i<len(l):
            data[k] = l[i]
            i+=1
            k+=1
        while j<len(r):
            data[k] = r[j]
            j+=1
            k+=1





    # else:
    #     print(data)


    return 'data'


resp = mergesort(arr)

print(resp)
print(new_arra)
print(arr)

