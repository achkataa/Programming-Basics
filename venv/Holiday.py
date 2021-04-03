money_needed = float(input())
current_money = float(input())

day_counter = 0
spending_days = 0

while current_money < money_needed and spending_days < 5:
    command = input()
    money = float(input())
    day_counter += 1
    if command == "save":
        current_money = current_money + money
        spending_days = 0
    elif command == "spend":
        current_money = current_money - money
        spending_days += 1
        if current_money < 0:
            current_money = 0

if spending_days == 5:
    print("You can't save the money.")
    print(day_counter)
if current_money >= money_needed:
    print(f"You saved the money for {day_counter} days.")


