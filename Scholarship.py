import math
income_in_leva = float(input())
average_marks = float(input())
min_salary = float(input())

social_scholarship = math.floor(min_salary * 35 / 100)
marks_scholarship = math.floor(average_marks * 25)

if average_marks >= 5.50:
    if income_in_leva < min_salary:
        if marks_scholarship >= social_scholarship:
            print(f"You get a scholarship for excellent results {marks_scholarship} BGN")
        else:
            print(f"You get a Social scholarship {social_scholarship} BGN")
    else:
        print(f"You get a scholarship for excellent results {marks_scholarship} BGN")
elif average_marks > 4.50:
    if income_in_leva < min_salary:
        print(f"You get a Social scholarship {social_scholarship} BGN")
    else:
        print("You cannot get a scholarship!")

else:
    print("You cannot get a scholarship!")



