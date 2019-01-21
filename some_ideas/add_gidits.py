# складываем все цифры в числе

def add(number):
    return sum( int(d) for d in str(number) )

def shrink(number):
    while number > 9:
        number = add(number)
    return number


v = int(input("Input number:"))

k = add(v)

print("sum=", k)


k2 = shrink(v)

print("sum2=", k2)