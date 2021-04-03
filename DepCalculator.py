dep_sum = float(input())
dep_term = int(input())
annual_interest_percent = float(input())

total_sum = dep_sum + dep_term * ((dep_sum * annual_interest_percent) / 100) / 12
print(total_sum)