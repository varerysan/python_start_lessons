# Compute Eluler number 2.7__

e = 0
num = 10
coef = 1

for n in range(1,num):
    e += coef
    coef /= float(n)

print("e=", e)
