





# Find whether we can reach to (c,d) from (a,b).
# Such that we can perform only two operation on (a,b) -> (a+b, b) or (a, a+b)


# a= 2, b =3  c= 5 d = 8  True case
# (2, 3)-->(5, 3)-->(5, 8)->         (5,8)
# a=2, b=3, c= 5, d= 5   false

# (2, 3)-->(5, 3) and (2, 5) --> (5, 3)/(5,8) and (2, 5)-- 7, 5,  2, 7  -->(5, 8)->
# (2, 3)

inputs = [2, 3]
# output = [5, 8]

output = [5, 5]
def calcuttion(data, output):
    a = data[0]
    b = data[1]
    # while True:
    data1 = []
    data1.append(data)
    for index in range(max(output[0], output[1])):
        x, y = data1[index][0], data1[index][1]
        print(x, y)
        if x==output[0] and y == output[1]:
            return True
        data1.append([x+y, y])
        data1.append([x , x+y])






    return False



res = calcuttion(inputs,output)
print(res)








