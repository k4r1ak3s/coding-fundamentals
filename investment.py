import math

rate = 10 / 100
limit = 1000
deposit = 100

year = math.ceil(math.log(limit / deposit, rate + 1))

print(f'years to achieve {limit} = {year}')
print(f'checked sum of the deposit after {math.ceil(year)} years = {deposit * pow(rate + 1, year)}')