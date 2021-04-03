hole_rent = int(input())

cake = hole_rent * 0.2
drinks = cake - cake * 45 / 100
animator = hole_rent * 1/3

money_needed = hole_rent + cake + drinks + animator
print(money_needed)