days = int(input())
cookers = int(input())
cakes_number = int(input())
waffles_number = int(input())
pancakes_number = int(input())

cakes_per_day = cakes_number * 45
waffles_per_day = waffles_number * 5.80
pancakes_per_day = pancakes_number * 3.20


sweets_number_per_day = (cakes_per_day + waffles_per_day + pancakes_per_day) * cookers
sweets_whole_event = sweets_number_per_day * days
money_after_expenses = sweets_whole_event - sweets_whole_event * 1/8
print(money_after_expenses)

