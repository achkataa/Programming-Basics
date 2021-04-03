#•	Бюджет на групата – цяло число;
#•	Сезон –  текст: "Spring", "Summer", "Autumn" или "Winter";
#•	Брой рибари – цяло чис# ло.
budget = int(input())
season = input()
fishermen = int(input())

boat_price = 0

if season == "Spring":
    boat_price = 3000
elif season == "Summer" or season == "Autumn":
    boat_price = 4200
elif season == "Winter":
    boat_price = 2600

if fishermen <= 6:
    boat_price = boat_price - boat_price * 0.1
elif fishermen >= 7 and fishermen <= 11:
    boat_price = boat_price - boat_price * 0.15
elif fishermen >= 12:
    boat_price = boat_price - boat_price * 0.25

if (fishermen % 2) == 0 and season != "Autumn":
    boat_price = boat_price - boat_price * 0.05
else:
    boat_price = boat_price

if budget >= boat_price:
    print(f"Yes! You have {budget - boat_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {boat_price - budget:.2f} leva.")



