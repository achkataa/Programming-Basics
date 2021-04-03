import math
income = float(input())
grade = float(input())
min_salary = float(input())

social_scholarship = math.floor(min_salary * 35 / 100)
grade_scholarship = math.floor(grade * 25)

if grade >= 5.50:
    if income < min_salary:
        if grade_scholarship >= social_scholarship:
            print(f"You get a scholarship for excellent results {grade_scholarship} BGN")
        else:
            print(f"You get a Social scholarship {social_scholarship} BGN")
    else:
        print(f"You get a scholarship for excellent results {grade_scholarship} BGN")
elif grade > 4.50:
    if income < min_salary:
        print(f"You get a Social scholarship {social_scholarship} BGN")
    else:
        print(f"You cannot get a scholarship!")
else:
    print(f"You cannot get a scholarship!")


