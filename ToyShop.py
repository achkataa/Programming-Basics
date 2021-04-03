holiday_price = float(input())
puzzle_number = int(input())
dolls_number = int(input())
bears_number = int(input())
minions_number = int(input())
trucks_number = int(input())



puzzles = puzzle_number * 2.60
dolls = dolls_number * 3
bears = bears_number * 4.10
minions = minions_number * 8.20
trucks = trucks_number * 2

sum = puzzles + dolls + bears + minions + trucks
toys_count = puzzle_number + dolls_number + bears_number + minions_number + trucks_number

if toys_count >= 50:
    sum *= 0.75
sum *= 0.9
if sum >= holiday_price:
        print(f"Yes! {sum - holiday_price:.2f} lv left.")
else:
    print(f"Not enough money! {holiday_price - sum:.2f} lv needed.")










