import math

record_in_seconds = float(input())
distance = float(input())
time_in_seconds_for_one_meter = float(input())

time_needed = distance * time_in_seconds_for_one_meter
delay = math.floor(distance / 15) * 12.5

total_time = time_needed + delay

if total_time < record_in_seconds:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    needed_time = total_time - record_in_seconds
    print(f"No, he failed! He was {needed_time:.2f} seconds slower.")