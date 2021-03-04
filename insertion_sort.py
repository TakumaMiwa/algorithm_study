S = list(map(int, input().split()))

for i in range(1, len(S)):
    key = S[i]
    j = i - 1
    while j>=0 and S[j]>key:
        S[j+1] = S[j]
        j -= 1
    S[j+1] = key
print(S)
