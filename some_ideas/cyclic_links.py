#Cyclic links and print
# Author: Valery Mosyagin

a = [10, 20]
b = [a, 30]
a.append(b)
print("a=", a)
print("b=", b)