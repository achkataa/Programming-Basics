length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent_taken_volume = float(input())

volume = length_cm * width_cm * height_cm
litres = volume * 0.001
percent = percent_taken_volume * 0.01
litres_needed = litres * (1 - percent)

print(litres_needed)

