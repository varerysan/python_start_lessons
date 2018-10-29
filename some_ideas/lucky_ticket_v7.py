# Проверка счастливый билет или нет

all_sums = {}
for n in range(1000):
    d1 = n % 10
    d2 = (n // 10) % 10
    d3 = n // 100
    part_sum = d1 + d2 + d3    
    all_sums[part_sum] = all_sums.get(part_sum, 0) + 1

total = sum([n*n for n in all_sums.values() ])
print("total=", total)
