budget = float(input())
season = input()

destination = ""
expenses = 0
hotel_or_camp = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        hotel_or_camp = "Camp"
        expenses = budget * 0.3
    elif season == "winter":
        hotel_or_camp = "Hotel"
        expenses = budget * 0.7
elif budget > 100 and budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        hotel_or_camp = "Camp"
        expenses = budget * 0.4
    elif season == "winter":
        hotel_or_camp = "Hotel"
        expenses = budget * 0.8
elif budget > 1000:
    destination = "Europe"
    if season == "summer":
        hotel_or_camp = "Hotel"
        expenses = budget * 0.9
    elif season == "winter":
        hotel_or_camp = "Hotel"
        expenses = budget * 0.9



print(f"Somewhere in {destination}")
print(f"{hotel_or_camp} - {expenses:.2f}")




