
def is_safe(result, row, col):
    # understand the row
    for i in range(row):
        if result[i][col]==1:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if result[i][j]==1:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col, 1, len(result))):
        if result[i][j] == 1:
            return False
    return True

def nqueen_utils(result, row):
    n = len(result)
    if row >= n:
        print(result)
        return True
    for col in range(n):


        if is_safe(result, row, col):
            result[row][col] = 1
            if nqueen_utils(result, row+1):
                return True
            result[row][col] = 0

    print(result)


    return False

def nqueens(n):


    result = [[0]*n for i in range(n)]

    if nqueen_utils(result, 0):
        print("solution exist")
    else:
        print("solution don't not exist")






    return result





n = 4
result = nqueens(n)
print(result)
