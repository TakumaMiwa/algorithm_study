import sys
pizzas = [850, 900]
toppings = [200, 250]
x = 1000

min_diff = sys.maxsize

pizzas.sort()
toppings.sort()
topping_max = toppings[-1] + toppings[-2]

for pizza in pizzas:
    if pizza > x:
        if abs(x-pizza)>abs(min_diff):
            break
        else:
            min_diff = pizza - x
    elif pizza + topping_max < x:
        if abs(pizza+topping_max-x) > abs(min_diff):
            continue

        else:
            min_diff = pizza+topping_max - x
    else:
        for topping in toppings:
            diff = pizza + topping - x
            if abs(diff) < abs(min_diff):
                min_diff = diff
        for i in range(len(toppings)-1):
            for j in range(i+1, len(toppings)):
                diff = pizza + toppings[i] + toppings[j] - x
                if abs(diff) < abs(min_diff):
                    min_diff = diff

print(min_diff+x)

