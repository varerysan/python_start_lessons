# author: Valery Mosyagin
# решение квадратного уравнения

import math

a = float(input("Введите коэффициент a:"))
b = float(input("Введите коэффициент b:"))
c = float(input("Введите коэффициент c:"))

d = b*b - 4 * a * c

if d < 0:
    print("Корней нет")
elif d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("x1=", x1)
    print("x2=", x2)
else:
    x = -b / (2 * a)
    print("x=", x)
    
    
    
    