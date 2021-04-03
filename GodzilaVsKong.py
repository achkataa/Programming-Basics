import math
#Ред 1.	Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
#ед 2.	Брой на статистите – цяло число в интервала [1 … 500]
#Ред 3.	Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]

movie_budget = float(input())
statists_number = int(input())
one_statist_costume_price = float(input())

decor = movie_budget * 0.1
statists_costumes = statists_number * one_statist_costume_price

if statists_number > 150:
    costumes_discount = statists_costumes * 0.1
    costumes = statists_costumes - costumes_discount
    total_money = decor + costumes
    if total_money <= movie_budget:
        print("Action!")
        print(f"Wingard starts filming with {abs(movie_budget - total_money):.2f} leva left.")
    else:
        money_needed = abs(movie_budget - total_money)
        print("Not enough money!")
        print(f"Wingard needs {money_needed:.2f} leva more.")

elif statists_number <= 150:
    statists_costumes = statists_number * one_statist_costume_price
    total_money = decor + statists_costumes
    if movie_budget - total_money <= movie_budget:
        print("Action!")
        print(f"Wingard starts filming with {movie_budget - total_money:.2f} leva left.")
    else:
        money_needed = movie_budget - total_money
        print("Not enough money!")
        print(f"Wingard needs {money_needed:.2f} leva more.")

