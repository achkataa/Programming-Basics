flower_type = input()
flowers_number = int(input())
budget = int(input())

flower_price = 0

if flower_type == "Roses":
    flower_price = 5
    total_price = flower_price * flowers_number
elif flower_type == "Dahlias":
    flower_price = 3.80
    total_price = flower_price * flowers_number
elif flower_type == "Tulips":
    flower_price = 2.80
    total_price = flower_price * flowers_number
elif flower_type == "Narcissus":
    flower_price = 3
    total_price = flower_price * flowers_number
elif flower_type == "Gladiolus":
    flower_price = 2.50
    total_price = flower_price * flowers_number

if flower_type == "Roses" and flowers_number > 80:
    total_price = total_price - total_price * 0.1
elif flower_type == "Dahlias" and flowers_number > 90:
    total_price = total_price - total_price * 0.15
elif flower_type == "Tulips" and flowers_number > 80:
    total_price = total_price - total_price * 0.15
elif flower_type == "Narcissus" and flowers_number < 120:
    total_price = total_price + total_price * 0.15
elif flower_type == "Gladiolus" and flowers_number < 80:
    total_price = total_price + total_price * 0.2


if budget >= total_price:
    print(f"Hey, you have a great garden with {flowers_number} {flower_type} and {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")




