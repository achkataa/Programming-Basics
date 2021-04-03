import math
product = input()
city = input()
quantity = float(input())

price = 0

if product == "coffee" and city == "Sofia":
    price = 0.50
    print(price * quantity)
elif product == "coffee" and city == "Plovdiv":
    price = 0.40
    print(price * quantity)
elif product == "coffee" and city == "Varna":
    price = 0.45
    print(price * quantity)
elif product == "water" and city == "Sofia":
    price = 0.80
    print(price * quantity)
elif product == "water" and city == "Plovdiv":
    price = 0.70
    print(price * quantity)
elif product == "water" and city == "Varna":
    price = 0.70
    print(price * quantity)
elif product == "beer" and city == "Sofia":
    price = 1.20
    print(price * quantity)
elif product == "beer" and city == "Plovdiv":
    price = 1.15
    print(price * quantity)
elif product == "beer" and city == "Varna":
    price = 1.10
    print(price * quantity)
elif product == "sweets" and city == "Sofia":
    price = 1.45
    print(price * quantity)
elif product == "sweets" and city == "Plovdiv":
    price = 1.30
    print(price * quantity)
elif product == "sweets" and city == "Varna":
    price = 1.35
    print(price * quantity)
elif product == "peanuts" and city == "Sofia":
    price = 1.60
    print(price * quantity)
elif product == "peanuts" and city == "Plovdiv":
    price = 1.50
    print(price * quantity)
elif product == "peanuts" and city == "Varna":
    price = 1.55
    print(price * quantity)
