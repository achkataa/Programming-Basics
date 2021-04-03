time = int(input())
day = input()

if time == 10 or time == 11 or time == 12 or time == 13 or time == 14 or time == 15 or time == 16 or time == 17 or time == 18:
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday":
        print("open")
    else:
        print("closed")
else:
    print("closed")