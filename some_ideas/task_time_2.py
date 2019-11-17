import random
import operator

from datetime import datetime


def create(func, name, min_val, max_val):
    def common_test():
        a = random.randint(min_val, max_val)
        b = random.randint(min_val, max_val)
        print("{}{}{}=?".format(a,name,b))
        start = datetime.now()
        res = int(input("How many:"))
        end = datetime.now()
        delta = end - start
        if res == func(a,b):
            print("Correct")
        else:
            print("Wrong")
        print("Time=",delta.total_seconds(), "seconds")
    
    return common_test


def sub_func(a,b):
    return a-b


mul_test = create(operator.mul, "*", 2, 10)
add_test = create(lambda x, y: x + y , "+", 10, 100)
sub_test = create(sub_func, "-", 2, 20)
#div_test = create(operator.mul, "*", 2, 10)



while True:
    random.choice([mul_test, add_test, sub_test])()




