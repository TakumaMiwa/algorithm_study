import sys



def sum_array(i, amount):
    global array, length, abs_min
    if i == length:
        value1 = abs(total - 2*amount)
        value2 = abs(total - 2*(amount+array[i]))
        abs_min = min(abs_min, value1, value2)
    else:
        sum_array(i+1, amount)
        sum_array(i+1, amount+array[i])

array = [1, 2, 3, 4, 5]
length = len(array) - 1
abs_min = sys.maxsize
total = sum(array)
sum_array(0, 0)
print(abs_min)
