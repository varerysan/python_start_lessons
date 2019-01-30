import math
import functools
import operator
n = int(input("Number:"))

start = n

vals = []
numbs = []

max_val = n+1


for k in range(2,n+1):
    while n % k == 0:
        vals.append(str(k))
        numbs.append(k)
        n = n // k

    if n == 1:
        break

if not vals:
    vals = [str(n)]

print( "*".join(vals) )

res = functools.reduce(operator.mul, numbs,1)
print("check=",res)
err = res - start

print("err=", err)
