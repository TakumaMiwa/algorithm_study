k = int(input())
s = input()[:4]
s = list(map(int, s))
t = input()[:4]
t = list(map(int, t))
p_sum = 0
counts = [0] * 9
countt = [0] * 9
cards = [k] * 9
count = [0] * 9
for i in s:
    counts[i-1] += 1
    count[i-1] += 1
for i in t:
    countt[i-1] += 1
    count[i-1] += 1
for i in range(9):
    cards[i] -= count[i]

for i in range(9):
    for j in range(9):
        if i==j:
            prob = cards[i]*(cards[i]-1)
        else:
            prob = cards[i]*cards[j]
        counts[i]+=1
        countt[j]+=1
        scores = 0
        for l in range(9):
            scores += (l+1) * (10**counts[l])
        scoret = 0
        for l in range(9):
            scoret += (l+1) * (10**countt[l])
        if scores>scoret:
            p_sum += prob
        counts[i]-=1
        countt[j]-=1

print(p_sum/(sum(cards)*(sum(cards)-1)))