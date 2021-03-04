import random
A = list(range(10))
P = [None]*len(A)

for i in range(len(P)):
    P[i] = random.randint(1, len(P)**3)
print(P)

for i in range(1, len(P)):
    j = i - 1
    key = P[i]
    key2 = A[i]
    while key < P[j] and j>=0:
        P[j+1] = P[j]
        A[j+1] = A[j]
        j -= 1
    P[j+1] = key
    A[j+1] = key2

print(P)
print(A)