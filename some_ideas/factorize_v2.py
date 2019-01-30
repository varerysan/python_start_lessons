n = int(input("Number:"))


vals = []

for k in range(2,n+1):
    while n % k == 0:
        vals.append(str(k))
        n = n / k

    if n == 1:
        break

print( "*".join(vals) )