#find golden ratio
# author: Valery Mosyagin


f1 = 1
f2 = 1

for n in range(50):
    f = f1 + f2

    q = f2/f1
    print(q)
    f1 = f2
    f2 = f
