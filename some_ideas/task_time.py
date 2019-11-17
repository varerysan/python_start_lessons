import random
from datetime import datetime

def mul_test():
    a = random.randint(2,10)
    b = random.randint(2,10)
    print("{}*{}=?".format(a,b))
    start = datetime.now()
    res = int(input("How many:"))
    end = datetime.now()
    delta = end - start
    if res == a*b:
        print("Correct")
    else:
        print("Wrong")
    print("Time=",delta.total_seconds(), "seconds")
    

def add_test():
    a = random.randint(2,10)
    b = random.randint(2,10)
    print("{}+{}=?".format(a,b))
    start = datetime.now()
    res = int(input("How many:"))
    end = datetime.now()
    delta = end - start
    if res == a+b:
        print("Correct")
    else:
        print("Wrong")
    print("Time=",delta.total_seconds(), "seconds")


while True:
    random.choice([mul_test,add_test])()

#mul_test()



