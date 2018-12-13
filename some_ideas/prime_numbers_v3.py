from math import sqrt
import cProfile

def is_prime_1(num):
    return all(  num % n != 0 for n in range(2, int(sqrt(num))+1)  )

def is_prime_2(num):
    return all(( num % n != 0 for n in range(2, int(sqrt(num))+1)) )

def is_prime_3(num):
    return all([ num % n != 0 for n in range(2, int(sqrt(num))+1)] )

def test_prime_v1(count):
    prime_list = [x for x in range(2,count+1) if is_prime_1(x)]

def test_prime_v2(count):
    prime_list = [x for x in range(2,count+1) if is_prime_2(x)]

def test_prime_v3(count):
    prime_list = [x for x in range(2,count+1) if is_prime_3(x)]

total = 300000

cProfile.run('test_prime_v1({})'.format(total))
cProfile.run('test_prime_v2({})'.format(total))
cProfile.run('test_prime_v3({})'.format(total))


