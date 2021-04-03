n = int(input())
first_sum = 0
second_sum = 0

for number in range(1, n + 1):
    value = int(input())
    first_sum = first_sum + value
for number in range(1, n + 1):
    value = int(input())
    second_sum = second_sum + value

if first_sum == second_sum:
    print(f"Yes, sum = {first_sum}")
else:
    print(f"No, diff = {abs(first_sum - second_sum)}")