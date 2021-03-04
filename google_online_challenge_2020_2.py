import sys

N = int(input())
queries = [None]*N
result = [0]
for i in range(N):
    queries[i] = list(map(int, input().split()))
for i in range(N):
    if queries[i][0] == 0:
        result.append(queries[i][1])
    elif queries[i][0] == 1:
        for j in range(len(result)):
            result[j] = result[j] ^ queries[i][1]
    else:
        print("Input correct values.")
        sys.out
for i in result:
    print(i, end=" ")
print()