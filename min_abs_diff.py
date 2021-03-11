import sys
array = [1, 2, 3, 4, 5]

end = 2 ** len(array)
min_abs = sys.maxsize
total = sum(array)
for i in range(end):
    one_server = 0
    for j in range(len(array)):
        if bin(i>>j)[-1]=='1':
            one_server += array[j]
    print(one_server)
    dif_abs = abs(total - 2 * one_server)
    if dif_abs < min_abs:
        min_abs = dif_abs
print(min_abs)


