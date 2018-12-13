from math import sqrt
count = 0

max_test = 0

def is_prime(num):
    global count
    global max_test
    for n in range(2, int(sqrt(num))+1  ):
        count += 1
        if num % n == 0:
            if n > max_test:
                max_test = n
            return False
    return True

num_prime = 0

for k in range(2,1000000+1):
    if is_prime(k):
        num_prime += 1


print("num_prime=", num_prime)
print("count=", count)
print("max_test=", max_test)

