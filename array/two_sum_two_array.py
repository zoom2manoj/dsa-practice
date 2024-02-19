A = [1, 2, 1, 3, 4];


def heapify(n, i):
    rootLargest = i;
    lchild = 2 * i;
    rchild = (2 * i) + 1;

    if (lchild < n and A[lchild] > A[rootLargest]):
        rootLargest = lchild;

    if (rchild < n and A[rchild] > A[rootLargest]):
        rootLargest = rchild;

    if (rootLargest != i):
        t = A[i];
        A[i] = A[rootLargest];
        A[rootLargest] = t;
        # Recursion
        heapify(n, rootLargest);


def binarySearch(l, r, x):
    while (l <= r):
        m = l + (r - l) // 2;

        if (A[m] == x):
            return m;

        if (A[m] < x):
            l = m + 1;

        else:
            r = m - 1;

    return -1;


if __name__ == '__main__':

    B = [3, 1, 5, 1, 2];

    K = 8;

    n = len(A);
    print(A)
    print('====')
    # Building the heap
    for i in range(n // 2 - 1, 0, -1):
        heapify(n, i);
    print(A)
    print('====')

    for i in range(n):
        temp = K - B[i];
        if (binarySearch(0, n - 1, temp - 1) != -1):
            print("\nFound the elements.");
            break;
