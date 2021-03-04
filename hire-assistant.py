import random
best = 0
count = 0
hired = []
s = list(range(10))
random.shuffle(s)
for i in range(len(s)):
    if s[i]>best:
        best = s[i]
        hired.append(best)
print(s)
print(hired)