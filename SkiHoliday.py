days = int(input())
room_type = input() #- "room for one person", "apartment" или "president apartment";
grade = input()

price = 0
nights = days - 1

if room_type == "room for one person":
    price = nights * 18.00
elif room_type == "apartment":
    price = nights * 25.00
elif room_type == "president apartment":
    price = nights * 35.00

if room_type == "apartment" and days < 10:
    price = price - price * 0.30
elif room_type == "apartment" and days >= 10 and days <= 15:
    price = price - price * 0.35
elif room_type == "apartment" and days > 15:
    price = price - price * 0.50
elif room_type == "president apartment" and days < 10:
    price = price - price * 0.10
elif room_type == "president apartment" and days >= 10 and days <= 15:
    price = price - price * 0.15
elif room_type == "president apartment" and days > 15:
    price = price - price * 0.20

if grade == "positive":
    price = price + 0.25 * price
elif grade == "negative":
    price = price - 0.10 * price

print(f"{price:.2f}")