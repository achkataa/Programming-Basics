first_time = int(input())
second_time = int(input())
third_time = int(input())

time = first_time + second_time + third_time
minutes = time // 60
seconds = time % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")