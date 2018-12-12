from math import sqrt
count = 0

def is_prime(num):
    global count
    for n in range(2, int(sqrt(num))  ):
        count += 1
        if num % n == 0:
            return False
    return True

num_prime = 0

for k in range(2,300000+1):
    if is_prime(k):
        num_prime += 1


print("num_prime=", num_prime)
print("count=", count)

