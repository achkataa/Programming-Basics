import math
figure_type = input()


if figure_type == "square":
    a = float(input())
    area_square = math.pow(a, 2)
    print(f"{area_square:.3f}")
elif figure_type == "rectangle":
    a = float(input())
    b = float(input())
    print(f"{a * b:.3f}")
elif figure_type == "circle":
    a = float(input())
    area_circle = math.pi * (math.pow(a, 2))
    print(f"{area_circle:.3f}")
elif figure_type == "triangle":
    a = float(input())
    b = float(input())
    area_triangle = (a * b) / 2
    print(f"{area_triangle:.3f}")
