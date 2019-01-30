import math
n = int(input("Number:"))

vals = []

max_val = int(math.sqrt(n)+2)

for k in range(2, max_val):
    while n % k == 0:
        vals.append(str(k))
        n = n // k

    if n == 1:
        break

if not vals:
    vals = [str(n)]

print( "*".join(vals) )