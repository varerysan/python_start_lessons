# author: Valery Mosyagin
# разбор выражения квадратного уравнения
# 5x^2+7x-25=0
# 5*x*x - 10*x + 5 = 0
# 5*x**2 + 7*x -10 =0
#
#
#

import re

text = " 10*x^2 + 20*x - 7 = 0"
text = "-x^2-25=0"

t2 = re.sub(" ","",text)
print("t2=",t2)

t3,t4 = re.split("=",t2)
print("t3=", t3)
print("t4=", t4)

t5 = re.findall("[-\+]?[^\+-]+",t3)
print("t5=", t5)
print("-"*10)

coefs = {}

for t6 in t5:
    t7 = re.split("\*",t6)
    print("\nfor t6=", t6)
    print("t7=", t7)
    
    
