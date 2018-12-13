def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

for k in range(2,101):
    if is_prime(k):
        print(k)


