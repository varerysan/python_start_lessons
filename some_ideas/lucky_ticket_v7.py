# author: Valery Mosyagin

# Проверка счастливый билет или нет

all_sums = {}
for n in range(1000):    
    line = (str(n)).zfill(3)    
    part_sum = sum([int(s) for s in line])  
    all_sums[part_sum] = all_sums.get(part_sum, 0) + 1

total = sum([n*n for n in all_sums.values() ])
print("total=", total)
