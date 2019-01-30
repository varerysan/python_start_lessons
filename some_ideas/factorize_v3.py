import math
n = int(input("Number:"))


vals = []

max_val = int(math.sqrt(n)+1)
print("from 2 to ", max_val-1)
for k in range(2,int(math.sqrt(n)+1)):
    print("check for ",k)
    while n % k == 0:
        vals.append(str(k))
        n = n / k

    if n == 1:
        break

if not vals:
    vals = [str(n)]

print( "*".join(vals) )