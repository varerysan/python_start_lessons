from math import sqrt

def is_prime(num):
    return all( num % n != 0 for n in range(2, int(sqrt(num))+1) )


primes = [x for x in range(2,1001) if is_prime(x)]
print(primes)

