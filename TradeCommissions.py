city = input()
sales = float(input())

if city == "Sofia":
    if sales >= 0 and sales <= 500:
        print(f"{sales * 0.05:.2f}")
    elif sales > 500 and sales <= 1000:
        print(f"{sales * 0.07:.2f}")
    elif sales > 1000 and sales <= 10000:
        print(f"{sales * 0.08:.2f}")
    elif sales > 10000:
        print(f"{sales * 0.12:.2f}")
    elif sales < 0:
        print("error")
elif city == "Varna":
    if sales >= 0 and sales <= 500:
        print(f"{sales * 0.045:.2f}")
    elif sales > 500 and sales <= 1000:
        print(f"{sales * 0.075:.2f}")
    elif sales > 1000 and sales <= 10000:
        print(f"{sales * 0.10:.2f}")
    elif sales > 10000:
        print(f"{sales * 0.13:.2f}")
    elif sales < 0:
        print("error")
elif city == "Plovdiv":
    if sales >= 0 and sales <= 500:
        print(f"{sales * 0.055:.2f}")
    elif sales > 500 and sales <= 1000:
        print(f"{sales * 0.08:.2f}")
    elif sales > 1000 and sales <= 10000:
        print(f"{sales * 0.12:.2f}")
    elif sales > 10000:
        print(f"{sales * 0.145:.2f}")
    elif sales < 0:
        print("error")
else:
    print("error")





