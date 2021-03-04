def merge(A, p, q, r):
    L = A[p:q+1] + [1000]
    R = A[q+1:r+1] + [1000]
    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i]<=R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

A = [2, 4, 1, 5, 3, 8, 4, 9, 2, 5]
merge_sort(A, 0, 9)
print(A)
